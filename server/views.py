from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .logic import matching_algo


@api_view(['POST'])
def listen(request):

    if request.method == 'POST':
        deserialized = String_(data=request.data)
        
        if deserialized.is_valid():
            likes = deserialized.data['argument_1']
            answer = matching_algo(likes)

            return Response(answer, status=status.HTTP_200_OK)

        else:
            return Response(deserialized.errors)