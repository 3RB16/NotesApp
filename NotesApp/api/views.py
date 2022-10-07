from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .models import Note
from .serializers import NoteSerializer

# Create your views here.


class NoteList(APIView):
    def get(self , request):
        serializer = NoteSerializer(Note.objects.all() , many = True)
        return Response(serializer.data , status = status.HTTP_200_OK)

    def post(self , request):
        serializer = NoteSerializer(data = request.data)
        if serializer.valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED)
        return Response(serializer.errors , status = status.HTTP_404_NOT_FOUND)

    def delete(self , request):
        Note.objects.all().delete()
        return Response(data = {'message' : 'Notes deleted!!'} , status = status.HTTP_200_OK)



class NoteDetail(APIView):
    def get(self, request , pk):
        try:
            serializer = NoteSerializer(Note.objects.get(pk = pk))
        except Note.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        return Response(serializer.data , status = status.HTTP_200_OK)
    
    def put(self , request , pk):
        serializer = NoteSerializer(data = request.data, instance=Note.objects.get(pk = pk))
        if serializer.valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED)
        return Response(serializer.errors , status = status.HTTP_404_NOT_FOUND)

    def delete(self , request , pk):
        try:
            Note.objects.get(pk = pk).delete()
        except Note.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        return Response(data = {'message': 'Note deleted!!!'} , status = status.HTTP_200_OK) 
