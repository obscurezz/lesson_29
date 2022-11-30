from rest_framework import serializers


class IsPublishedNotTrueValidator:
    def __init__(self):
        self.__status = False

    def __call__(self, value: bool):
        if value != self.__status:
            raise serializers.ValidationError("Just created ad cannot be already published")
