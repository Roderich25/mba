#!/usr/bin/env python3
from marshmallow import Schema, fields, post_load, ValidationError, validates, validate


class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def __repr__(self):
        return f"{self.name} is {self.age} years old."


class PersonSChema(Schema):
    name = fields.String(validate=validate.Length(min=2))
    age = fields.Integer()
    email = fields.Email()
    # location = fields.String(required=True)

    @validates('age')
    def validate_age(self, age):
        if age > 120:
            raise ValidationError("Too old!")

    @post_load
    def create_person(self, data, **kwargs):
        return Person(**data)


input_data = {}
input_data['name'] = input("What's your name?\n")
input_data['age'] = input("What's your age?\n")
input_data['email'] = input("What's your e-mail?\n")


try:
    schema = PersonSChema()
    person = schema.load(input_data)
    # print(person)
    result = schema.dump(person)
    print(result)
except ValidationError as e:
    print(e)
    print(e.valid_data)
