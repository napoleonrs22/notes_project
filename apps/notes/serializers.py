from rest_framework import serializers
from django.utils.html import escape
from .models import Note


class NoteSerializer(serializers.ModelSerializer):


    class Meta: 
        model = Note
        fields =['id', 'title', 'content', 'created_at','updated_at']
        readonly_fields = ['id', 'created_at','updated_at']

    def validate_title(self,value):
        if not value.strip():
            raise serializers.ValidateError('Заголовок не может быть пустым')
        return escape(value.strip())

    def validate_content(self,value):
        if not value.strip():
            raise serializers.ValidateError('Содержание не может быть пустым')
        return escape(value.strip())
    

class NoteCreateSerializer(NoteSerializer):
    pass


class NoteUpdateSerializer(NoteSerializer):
    title = serializers.CharField(required=False)
    content = serializers.CharField(required=False)