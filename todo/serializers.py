from rest_framework import serializers
from .models import Groups, ToDos


class GroupSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)

    class Meta:
        model = Groups
        fields = '__all__'


class TodoReadSerializer(serializers.ModelSerializer):
    groups = GroupSerializer()

    class Meta:
        model = ToDos
        fields = '__all__'


class TodosSerializer(serializers.ModelSerializer):

    class Meta:
        model = ToDos
        fields = '__all__'


