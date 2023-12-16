from rest_framework.serializers import ModelSerializer
from.models import Users
from.models import File


class fileSerializer(ModelSerializer):
    class Meta:
        model=File
        fields='__all__'

class signupSerializer(ModelSerializer):
    class Meta:
        model=Users
        fields='__all__'

