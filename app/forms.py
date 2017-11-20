from flask_wtf import Form
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, NumberRange


class TestForm(Form):
    text = StringField('Insert text:', validators=[DataRequired()])
    image_width = IntegerField('Image width (px):', validators=[DataRequired()])
    image_height = IntegerField('Image height (px):', validators=[DataRequired()])
    v_margin = IntegerField('Vertical margin (%):',
                            validators=[DataRequired(), NumberRange(0, 45, "Margin must be <50%")], default='15')
    h_margin = IntegerField('Horizontal margin (%):',
                            validators=[DataRequired(), NumberRange(0, 45, "Margin must be <50%")], default='15')
    font = StringField('Font:', validators=[DataRequired()], default='arial.ttf')
    font_size = IntegerField('Font size:', validators=[DataRequired()], default='32')
