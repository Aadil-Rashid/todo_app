from rest_framework import serializers
from todo_app.models import TodoTable


class TodoTableSeializer(serializers.ModelSerializer):
    date_obj = serializers.SerializerMethodField()
    
    class Meta:
        model = TodoTable
        fields = ('id', 'title', 'description', 'completed', 'date_obj')
        
    def get_date_obj(self, obj):
        formated_date = obj.date.strftime('%d %b, %Y (%H:%M:%S) %p ')
        return formated_date

