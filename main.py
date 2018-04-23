from passgen import generate
from flask import Flask, request, jsonify
import os
app = Flask(__name__)


@app.route('/password')
def password():
    def parameters(param, default): return int(
        request.args.get(param, default))
    length = parameters('length', 10)
    digits = parameters('digits', 2)
    special_chars = parameters('special_chars', 2)
    options = parameters('options', 3)
    vowel_conversion = parameters('covert_vowels', 1)
    try:
        password_options = [generate(
            length, digits, special_chars, vowel_conversion) for _ in range(options)]
        return jsonify({'passwords': password_options})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def run():
    port =  int(os.environ['PORT']) if 'PORT' in os.environ else 8080
    debug = True if 'DEBUG' in os.environ else False
    print('Now serving on port {}'.format(port))
    try:
        app.run(port=port, debug=debug)
    except KeyboardInterrupt:
        print('Shutting Down..')


if __name__ == '__main__':
    run()
