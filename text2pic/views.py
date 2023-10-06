import os
from datetime import datetime
from flask import Response, jsonify, send_file, url_for, send_from_directory
from flask import request
from text2pic.text_handler import split_text, split_text_zip
from flask import Blueprint

site = Blueprint('text2pic', __name__)


@site.route('/text2pic', methods=['GET', 'POST'])
def text2picture():
    """

    Main entry point. Creates an image that contains text (white font on black background)

    If the text is too big to fit in a single image it will  be split among several files

    Input:
        - text
        - height, width: dimensions for the image
        - margin-height, margin-width (OPTIONAL): a margin around the text
        - font, font-size (OPTIONAL)

    :return: it returns a JSON object with a list of the generated files (one or many)
    """
    if request.method == 'GET':
        str_date_time = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
        response_text = split_text(folder=site.static_folder, text=f'Hello world from text2picture\nCurrent time: {str_date_time}',
                                   width=400, height=400, h_margin=100, w_margin=100, font='arial.ttf', font_size=48)
        return jsonify({'images': response_text})
    params = request.get_json()
    assert isinstance(params, dict)
    try:
        text = params["text"]
        height = params["height"]
        width = params["width"]
        h_margin = params.get("margin-height", 0)
        w_margin = params.get("margin-width", 0)
        font = params.get("font", 'arial.ttf')
        font_size = params.get("font-size", 32)
        response_text = split_text(site.static_folder, text, width, height, h_margin, w_margin, font, font_size)
        return jsonify({'images': response_text})
    except KeyError:
        response_text = {'Parameter error', 'Missing text, heigh or width'}
        return Response(response_text, status=400, mimetype='application/json')


@site.route('/text2piczip', methods=['GET', 'POST'])
def text2picturezip():
    """

    Main entry point. Creates an image that contains text (white font on black background)

    If the text is too big to fit in a single image it will  be split among several files

    Input:
        - text
        - height, width: dimensions for the image
        - margin-height, margin-width (OPTIONAL): a margin around the text
        - font, font-size (OPTIONAL)

    :return: it returns a gzip object with the generated files (one or many)
    """
    try:
        if request.method == 'GET':
            str_date_time = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
            zipfile = split_text_zip(folder=site.static_folder, text=f'Hello world from text2picture\nCurrent time: {str_date_time}',
                                       width=400, height=400, h_margin=100, w_margin=100, font='arial.ttf', font_size=48)
        else:
            params = request.get_json()
            assert isinstance(params, dict)
            text = params["text"]
            height = params["height"]
            width = params["width"]
            h_margin = params.get("margin-height", 0)
            w_margin = params.get("margin-width", 0)
            font = params.get("font", 'arial.ttf')
            font_size = params.get("font-size", 32)
            zipfile = split_text_zip(site.static_folder, text, width, height, h_margin, w_margin, font, font_size)
        return send_from_directory('static', zipfile)# , mimetype='application/zip')
    except KeyError:
        response_text = {'Parameter error', 'Missing text, heigh or width'}
        return Response(response_text, status=400, mimetype='application/json')