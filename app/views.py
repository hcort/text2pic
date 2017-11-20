from app import app
from flask import Response, jsonify
from flask import render_template
from flask import request
from app.text_handler import split_text

from app.forms import TestForm


@app.route('/text2pic', methods=['POST'])
def text2picture():
    # take text and image size and create
    # a black image with the text in it
    params = request.get_json()
    print(type(params))
    assert isinstance(params, dict)
    try:
        text = params["text"]
        height = params["height"]
        width = params["width"]
        h_margin = params.get("margin-height", 0)
        w_margin = params.get("margin-width", 0)
        font = params.get("font", 'arial.ttf')
        font_size = params.get("font-size", 32)
        response_text = split_text(text, width, height, h_margin, w_margin, font, font_size)
        return jsonify({'images': response_text})
    except KeyError:
        response_text = {'Parameter error', 'Missing text, heigh or width'}
        return Response(response_text, status=400, mimetype='application/json')


@app.route('/test', methods=['GET', 'POST'])
def test_form():
    form = TestForm(request.form)
    print('hello')
    # if request.method == 'POST':
    if form.validate_on_submit():
        text = request.form['text']
        image_width = int(request.form['image_width'])
        image_height = int(request.form['image_height'])
        v_margin = float(request.form['v_margin']) / 100
        h_margin = float(request.form['h_margin']) / 100
        font = request.form['font']
        font_size = int(request.form['font_size'])
        img_json = split_text(text, image_width, image_height, image_height * v_margin, image_width * h_margin, font, font_size)
        return render_template('testForm.html', form=form, json_files=img_json)
        # no longer sending image
        # img_file = os.path.join("", "static/image.png")
        # try:
        #     with open(img_file, 'wb') as out:  ## Open temporary file as bytes
        #         out.write(img.getvalue())           ## Read bytes into file
        #         out.close()
        # except Exception as ex:
        #     print('fuggggg' + str(ex))
        # print( img_file )
        # flash('Hello ' + text)
        # flash('/'+img_file)
    return render_template('testForm.html', form=form)
