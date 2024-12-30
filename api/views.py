from rest_framework.viewsets import ModelViewSet
from .serializers import ToDoSerializer, ColumnSerializer, TaskSerializer, ValidateTaskPositionSerializer
from .models import ToDo, Column, Task
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class ToDoViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ToDo.objects.filter(user=self.request.user)

class ColumnViewSet(ModelViewSet):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer
    permission_classes = [IsAuthenticated]

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]


    @action(methods=['patch'], detail=True)
    def change_task_position(self, request, pk=None):
        self.permission_classes = [IsAuthenticated]
        if pk is None:
            return Response({'error': 'An Id is missing!'}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            task = Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return Response({'error': 'Invalid Id'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ValidateTaskPositionSerializer(data=request.data)
        if serializer.is_valid():
            new_position = serializer.validated_data.get('position')

            # Buscar a nova coluna com base na posição dentro do ToDo
            try:
                new_column = Column.objects.get(position=new_position, todo=task.column.todo)
            except Column.DoesNotExist:
                return Response({'error': 'No column found with the given position!'}, status=status.HTTP_404_NOT_FOUND)
            
            if task.column is new_column:
                return Response({'error': 'Task is already within this column'}, status=status.HTTP_400_BAD_REQUEST)

            # Atualizar a coluna da tarefa
            task.column = new_column
            task.save()

            return Response({'success': 'Task moved to new column!'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            
        