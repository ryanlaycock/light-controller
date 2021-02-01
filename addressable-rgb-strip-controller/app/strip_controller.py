import board
import neopixel

num_of_leds = 300
pixels = neopixel.NeoPixel(board.D18, num_of_leds, auto_write=False)


def set_light_solid(min_val, max_val, rgb):
    print('Setting lights between ', min_val, ' and ', max_val, ' to ', rgb)
    for i in range(min_val, max_val):
        pixels[i] = (int(rgb[0]), int(rgb[1]), int(rgb[2]))
    pixels.show()
    print('Lights set')
