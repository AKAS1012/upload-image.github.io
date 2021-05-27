from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Assets
from .serializers import AssetsSerializer
from rest_framework import status


class AssetAPI(APIView):

    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            stu = Assets.objects.get(id=id)
            serializer = AssetsSerializer(stu)
            return Response(serializer.data)
        stu = Assets.objects.all()
        serializer = AssetsSerializer(stu, many=True)
        serializer_data = serializer.data
        return Response(serializer_data)

    def post(self, request, format=None):
        serializer = AssetsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        id = pk
        stu = Assets.objects.get(pk=id)
        serializer = AssetsSerializer(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data created'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None, format=None):
        id = pk
        stu = Assets.objects.get(pk=id)
        serializer = AssetsSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data created'})
        return Response(serializer.errors)
