from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from classes.models import Classroom
from .permission import IsTeacher
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .serializers import ClassListSerializerView, ClassDetailSerializerView, ClassCreateSerializerView
# Create your views here.

class ClassesListView(ListAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassListSerializerView
    permission_classes = [AllowAny]

class ClassesDetailView(RetrieveAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassDetailSerializerView
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'
    permission_classes = [AllowAny]

class ClassesUpdateView(RetrieveUpdateAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassCreateSerializerView
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'
    permission_classes = [IsAuthenticated, IsAdminUser]

class ClassesDeleteView(DestroyAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassListSerializerView
    lookup_field = 'id'
    lookup_url_kwarg = 'classroom_id'
    permission_classes = [IsAuthenticated, IsAdminUser]

class ClassesCreateView(CreateAPIView):
    serializer_class = ClassCreateSerializerView
    permission_classes = [IsAuthenticated, IsTeacher]

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)



