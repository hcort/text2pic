from flask import Flask
from flask import Response
from flask import request
from flask import send_file
#from flask.ext.api import status

from text_handler import split_text

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/text2pic', methods=['POST'])
def text2picture():
    # take text and image size and create
    # a black image with the text in it
    params = request.get_json()
    print( type(params) )
    assert isinstance(params, dict)
    try:
        text = params["text"]
        height = params["height"]
        width = params["width"]
        h_margin = params.get("margin-height", 0)
        w_margin = params.get("margin-width", 0)
        font = params.get("font", 'arial.ttf')
        font_size = params.get("font-size", 32)
        #return text + ". " + str(height) + "x" + str(width)
        img = split_text( text, width, height, h_margin, w_margin, font, font_size)
        return send_file(img, mimetype='image/gif')
    except KeyError:
        response_text = {'Parameter error', 'Missing text, heigh or width'}
 #       return content, status.HTTP_400_BAD_REQUEST
        return Response(response_text, status=400, mimetype='application/json')


if __name__ == '__main__':
    app.run()
