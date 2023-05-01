class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    display_name = StringField('Display Name', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Sign Up')
