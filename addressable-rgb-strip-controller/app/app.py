from flask import Flask, request, jsonify
from flask_cors import CORS
import strip_controller

app = Flask(__name__)
CORS(app)

required_section_fields = [
    'start',
    'end',
    'function',
    'red',
    'green',
    'blue'
]


@app.route('/strip', methods=['GET'])
def get_strip():
    print("Getting strip settings")


@app.route('/strip', methods=['POST'])
def post_strip():
    strip = request.json['strip']
    errors = []
    for section in strip:
        print('POST for section:', section)
        errors = valid_section(section)

        if section['function'] == "solid":
            strip_controller.set_light_solid(
                section['start'],
                section['end'],
                [
                    section['red'],
                    section['green'],
                    section['blue']
                ]
            )
        else:
            errors.append('invalid function: ' + section['function'])

    if len(errors) != 0:
        return jsonify({"errors": errors}), 422

    return jsonify(), 200


def valid_section(section):
    errors = []
    for required in required_section_fields:
        if section[required] is None:
            errors.append(str(required) + ' is none')
    return errors


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)

