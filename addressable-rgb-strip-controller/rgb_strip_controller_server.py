from concurrent import futures
import logging
import board
import neopixel

import grpc

import rgb_strip_commands_pb2
import rgb_strip_commands_pb2_grpc


class RGBStripCommandService(rgb_strip_commands_pb2_grpc.RGBStripCommandServicer):

    def __init__(self):
        num_of_leds = 300
        self.pixels = neopixel.NeoPixel(board.D18, num_of_leds, auto_write=False)
        pass

    def TurnOn(self, request, context):
        logging.info("Received TurnOn request")
        self.set_light(request.leds)

        return request

    def set_light(self, rgb_leds):
        for rgb_led in rgb_leds:
            logging.debug("Setting LED num: "+str(rgb_led.num)+" RGB: "+str(rgb_led.red)+","+str(rgb_led.green)+","+ str(rgb_led.blue))
            self.pixels[rgb_led.num] = rgb_led.red, rgb_led.green, rgb_led.blue
        self.pixels.show()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    rgb_strip_commands_pb2_grpc.add_RGBStripCommandServicer_to_server(RGBStripCommandService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(level="DEBUG")
    logging.warning("Initiating server")
    print("Running server")
    serve()
