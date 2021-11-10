# app/models.py
from banjo.models import Model, StringField

class Person(Model):
    name = StringField()
    email_address = StringField()
