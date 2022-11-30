from datetime import date

from rest_framework import serializers


class MinAgeValidator:
    def __init__(self, value: int):
        self.__value = value

    def __call__(self, age: date):
        if date.today().year - age.year < self.__value:
            raise serializers.ValidationError(f"User's age must be more than {self.__value}")


class CheckEmailNotDomainValidator:
    def __init__(self, value: str):
        self.__value = value

    def __call__(self, email: str):
        if email.split('@')[1] == self.__value:
            raise serializers.ValidationError(f"Cannot register user by domain name {self.__value}")
