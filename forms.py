from wtforms import Form, StringField
from wtforms.validators import DataRequired


class TaskForm(Form):
    name =  StringField('name', validators=[DataRequired()])
