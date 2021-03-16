from rest_framework import serializers 
from melodies.models import Chant
 
 
class ChantSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Chant
        fields = ('id', 'corpus_id', 'incipit', 'cantus_id',
            'mode', 'finalis', 'differentia', 'siglum', 'position', 
            'folio', 'sequence', 'marginalia', 'cao_concordances', 
            'feast_id', 'genre_id', 'office_id', 'source_id', 'melody_id', 
            'drupal_path', 'full_text', 'full_text_manuscript', 'volpiano', 'notes')