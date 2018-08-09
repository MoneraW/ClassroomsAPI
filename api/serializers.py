from rest_framework import serializers
from classes.models import Classroom

class ClassListSerializerView(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['subject', 'year', 'teacher']

class ClassDetailSerializerView(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['name', 'subject', 'year', 'teacher']

class ClassCreateSerializerView(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['name', 'subject', 'year', 'teacher']
