from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from classes.models import Classroom
from .serializers import ClassListSerializer, ClassDetailSerializer, ClassCreateUpdateSerializer

# Create your views here.
class ListView(ListAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassListSerializer

class DetailView(RetrieveAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'

class CreateView(CreateAPIView):
    serializer_class = ClassCreateUpdateSerializer

    def perform_create(self, serializer):
    	serializer.save(author=self.request.user)

class UpdateView(RetrieveUpdateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassCreateUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'

class DeleteView(DestroyAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassListSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'