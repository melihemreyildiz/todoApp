from rest_framework import generics
from .models import Groups, ToDos
from rest_framework.permissions import IsAuthenticated
from .serializers import GroupSerializer, TodosSerializer,TodoReadSerializer
from rest_framework import filters


class GroupGenerate(generics.ListCreateAPIView):
    queryset = Groups.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class GroupDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Groups.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]


class ToDoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDos.objects.all()
    serializer_class = TodosSerializer
    permission_classes = [IsAuthenticated]


class TodoGenerate(generics.ListCreateAPIView):
    queryset = ToDos.objects.all()
    serializer_class = TodosSerializer
    permission_classes = [IsAuthenticated]
    read_serializer_class = TodoReadSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['groups__title', 'priority', 'due_date']

    def get_serializer_class(self):
        read_serializer_class = getattr(self, 'read_serializer_class', None)

        if read_serializer_class and self.request.method == 'GET':
            return read_serializer_class
        else:
            return self.serializer_class
