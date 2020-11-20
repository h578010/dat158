from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SelectField, SelectField, RadioField, BooleanField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class DataForm(FlaskForm):

    budget = IntegerField('Budget', validators=[DataRequired()])
    popularity = FloatField('Popularity, 1-300')
    collection = BooleanField(label='Part of a movie collection')
    homepage = BooleanField(label='Has its own webpage')
    tagline = BooleanField(label='Has a tagline')
    titles = BooleanField(label='Original title matches English title')
    original_lang = BooleanField(label='Original language is English')
    release_month = IntegerField('Release month')
    release_day = IntegerField('Release day')
    release_year = IntegerField('Release year')
    languages = IntegerField(label='Number of languages spoken')
    genres = IntegerField(label='Number of genres')
    cast = IntegerField(label='Numbers of actors')
    
    submit = SubmitField('Submit')