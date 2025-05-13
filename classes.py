from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    captain_username = StringField('Id капитана', validators=[DataRequired()])
    captain_password = PasswordField('Пароль капитана', validators=[DataRequired()])
    austronavt_username = StringField('Id астронавта', validators=[DataRequired()])
    austronavt_password = PasswordField('Пароль астронавта', validators=[DataRequired()])
    submit = SubmitField('Доступ')