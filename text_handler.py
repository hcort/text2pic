"""


"""
import os
import re
from PIL import Image, ImageDraw
from PIL import ImageFont


def split_text(text, width, height, h_margin, w_margin, font, font_size):
    # we need to know the vertical size of the text
    # and estimate the number of characters that can
    # fit in a given width
    words = re.split('(\s)', text)
    img = Image.new('RGB', (width, height))
    d = ImageDraw.Draw(img)
    # TODO select font and size from parameter
    font = ImageFont.truetype(font, font_size)
    space_width, space_height = d.textsize(' ', font=font)
    # FIXME what happens with HTML text (?)
    line_breaks = ['\n', '\r', '</p>', '<br>']
    lines = []
    line = ''
    len_line = 0
    max_len_width = width - (w_margin*2)
    for word in words:
        # add words to each line
        len_word, heigh_tword = d.textsize(word, font=font)
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
    # TODO margins
    start_px = h_margin
    end_px = height - (2*h_margin)
    for aline in lines:
        d.text((w_margin, start_px), aline, (255, 255, 255), font=font)
        # TODO what if I need several images?
        start_px += space_height
        if start_px > end_px:
            print("Text is bigger than image size")
            d.text((w_margin, start_px), '##### cropped text to fit image #####', color='red', font=font)
            break
    # FIXME create a filename on the fly
    text_file = os.path.join("", "image.png")
    img.save(text_file)
    return text_file
