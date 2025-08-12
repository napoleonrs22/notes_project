from rest_framework import generics, status
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer, NoteCreateSerializer, NoteUpdateSerializer


class NoteListCreateView(generics.ListCreateAPIView):
    queryset = Note.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return NoteCreateSerializer
        return NoteSerializer


class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return NoteUpdateSerializer
        return NoteSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {'message': "Заметка удалена"},
            status=status.HTTP_204_NO_CONTENT
        )
