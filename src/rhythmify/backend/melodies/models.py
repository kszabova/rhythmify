from django.db import models


class Chant(models.Model):
    id = models.IntegerField(blank=True, primary_key=True)
    corpus_id = models.TextField(blank=True, null=True)
    incipit = models.TextField(blank=True, null=True)
    cantus_id = models.TextField(blank=True, null=True)
    mode = models.TextField(blank=True, null=True)
    finalis = models.TextField(blank=True, null=True)
    differentia = models.TextField(blank=True, null=True)
    siglum = models.TextField(blank=True, null=True)
    position = models.TextField(blank=True, null=True)
    folio = models.TextField(blank=True, null=True)
    sequence = models.FloatField(blank=True, null=True)
    marginalia = models.TextField(blank=True, null=True)
    cao_concordances = models.FloatField(blank=True, null=True)
    feast_id = models.TextField(blank=True, null=True)
    genre_id = models.TextField(blank=True, null=True)
    office_id = models.TextField(blank=True, null=True)
    source_id = models.TextField(blank=True, null=True)
    melody_id = models.TextField(blank=True, null=True)
    drupal_path = models.TextField(blank=True, null=True)
    full_text = models.TextField(blank=True, null=True)
    full_text_manuscript = models.TextField(blank=True, null=True)
    volpiano = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chant'
