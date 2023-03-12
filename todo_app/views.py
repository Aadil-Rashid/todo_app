from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from todo_app.models import TodoTable
from todo_app.serializers import TodoTableSeializer

# we will get data from db_tables here:
#  model => querysert ----> serilzer ----> 

class GetTodoView(ListAPIView):
    serializer_class = TodoTableSeializer
    def list(self, request):
        # import pdb                            #debugger
        # pdb.set_trace()
        parameters =self.request.query_params
        queryset = self.get_queryset(parameters)
        serializer = TodoTableSeializer(queryset, many=True)
        return Response({'data':serializer.data})
    
    def get_queryset(self, parameters):
        is_completed = parameters.get('is_completed')
        if is_completed is not None:
            # orm_query    (raw sql Query )
            queryset = TodoTable.objects.filter(completed=is_completed)
        else:
            queryset = TodoTable.objects.all()
            
        return queryset
    
    
from django.views.generic import ListView

class TodoView(ListView):
    model = TodoTable
    template_name = 'todo_view.html'
    context_object_name = 'todo_obj'

    def get(self, request, *args, **kwargs):
        my_model_objs = self.get_queryset()
        self.object_list = my_model_objs
        context = {self.context_object_name: my_model_objs}
        return self.render_to_response(context)
    