from wtforms.fields import StringField
from wtforms.widgets import TextArea
from flask_wtf import FlaskForm


class simpleForm(FlaskForm):
    name = StringField("Name")
