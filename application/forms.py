from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField
from datetime import datetime
from wtforms.validators import DataRequired, Length
from application.models import Events

class EventForm(FlaskForm):
    event_name = StringField('Event Name',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    event_date = DateField('Event Date', format='%m/%d/%Y',
        validators = [
            DataRequired()
        ]
    )
    location = StringField('Location',
        validators = [
            DataRequired(),
            Length(min=2, max=100)
        ]
    )
    description = StringField('Description',
        validators = [
            DataRequired(),
            Length(min=2, max=500)
        ]
    )
    submit = SubmitField('Add Event')


class UpdateEventForm(FlaskForm):
    event_name = StringField('Event Name',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    event_date = DateField('Event Date', format='%m/%d/%Y',
        validators = [
            DataRequired()
        ]
    )
    location = StringField('Location',
        validators = [
            DataRequired(),
            Length(min=2, max=100)
        ]
    )
    description = StringField('Description',
        validators = [
            DataRequired(),
            Length(min=2, max=500)
        ]
    )
    submit = SubmitField('Update')
