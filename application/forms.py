from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.html5 import DateTimeField
from datetime import datetime
from wtforms.validators import DataRequired, Length, Email, ValidationError
from application.models import Events

class EventForm(FlaskForm):
    event_name = StringField('Event Name',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    event_date = DateTimeField('Event Date', format='%d/%m/%Y',default=datetime.utcnow ,
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
    event_date = DateTimeField('Event Date', format='%d/%m/%Y %H:%M',default=datetime.utcnow ,
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

class OrganiserForm(FlaskForm):
    first_name = StringField('First Name',
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    last_name = StringField('Last Name', 
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ]
    )
    email = StringField('Email',
        validators = [
            DataRequired(),
            Email()
        ]
    )
    submit = SubmitField('Add Organiser')

