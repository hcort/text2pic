"""


"""
import os
import re
import time
from PIL import Image, ImageDraw, ImageFont
from flask import url_for, app


def fill_lines(words, max_len_width, image_draw, font, space_width):
    lines = []
    # FIXME what happens with HTML text (?)
    line_breaks = ['\n', '\r']
    len_line = 0
    line = ''
    for word in words:
        # add words to each line
        len_word, heigh_tword = image_draw.textsize(word, font=font)
        if (len_line+len_word) >= max_len_width:
            lines.append(line)
            line = ""
            len_line = 0
        if word in line_breaks:
            lines.append(line)
            line = ""
            len_line = 0
        else:
            line += word
            len_line += (space_width+len_word)
    if len(line) > 0:
        lines.append(line)
    return lines


def save_file(image_draw):
    # create unique file name
    filename = str(time.time()) + '.png'
    fullname = os.path.join('static', filename)
    image_draw.save(fullname)
    return filename


def split_text(text, width, height, h_margin, w_margin, font, font_size):
    # we need to know the vertical size of the text
    # and estimate the number of characters that can
    # fit in a given width
    words = re.split('(\s)', text)
    img = Image.new('RGB', (width, height))
    image_draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font, font_size)
    space_width, space_height = image_draw.textsize(' ', font=font)
    max_len_width = width - (w_margin*2)
    lines = fill_lines(words, max_len_width, image_draw, font, space_width)
    start_px = h_margin
    end_px = height - (2*h_margin)
    json_object = []
    for aline in lines:
        image_draw.text((w_margin, start_px), aline, (255, 255, 255), font=font)
        start_px += space_height
        if start_px > end_px:
            # save this image to file
            filename = save_file(img)
            json_object.append({'filename': url_for('static',filename=filename)})
            # create a new one
            img = Image.new('RGB', (width, height))
            image_draw = ImageDraw.Draw(img)
            start_px = h_margin
    # save last image
    if start_px > h_margin:
        filename = save_file(img)
        json_object.append({'filename': url_for('static',filename=filename)})
    return json_object
