from rest_framework import serializers


class String_(serializers.Serializer):
    
    argument_1 = serializers.CharField(max_length=300)
