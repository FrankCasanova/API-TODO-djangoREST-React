from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer

# Create your views here.

# In traditional Django
# views
# are used to customize what data to send to the templates. In Django
# REST Framework views do the same thing but for our serialized data.

class ListTodo(generics.ListAPIView):
    """
    here, we list all our todos
    """
    queryset = Todo.objects.all() #we get all todos
    serializer_class = TodoSerializer #send all todos to the serializer, for transform to JSON
    

class DetailTodo(generics.RetrieveAPIView):
    """
    here, retrieve one todo, to see in detail its contain
    """    
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer