from rest_framework import serializers

from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    """
    we need to transform our data, from the models, into JSON that will
    be outputted at the URLs. Therefore we need a serializer.
    """

    class Meta:
        model = Todo
        fields = ('id', 'title', 'body') #the specific field it we want to expose

