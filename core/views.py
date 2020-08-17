from django.http import JsonResponse
from django.shortcuts import render

# third party imports
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PostSerializer
from .models import Post



class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'title': 'title',
            'link': 'link'
        }
        return Response(data)
    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)

# def test_view(request):
#     data = {
#         'title': 'title',
#         'link': 'link'
#     }
#     return JsonResponse(data)

