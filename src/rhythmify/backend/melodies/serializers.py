from rest_framework import serializers 
from melodies.models import Chant
 
 
class ChantSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Chant
        fields = ('id',
                  'title',
                  'volpiano',
                  'full_text')