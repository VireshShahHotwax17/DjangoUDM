from django.db import models

# Create your models here.
class EnumerationType(models.Model):
    enumTypeId = models.CharField(primary_key = True, max_length = 100)
    description = models.CharField(max_length = 200)

    class Meta:
        db_table = 'EnumerationType'

class Enumeration(models.Model):
    enumId = models.CharField(primary_key = True, max_length = 100)
    enum_type_id = models.ForeignKey(
        'EnumerationType', on_delete=models.SET_NULL, null=True, blank=True, db_column='ENUM_TYPE_ID'
    )
    parent_enum_id = models.CharField(max_length=40, null=True, blank=True)
    enum_code = models.CharField(max_length=255, null=True, blank=True)
    sequence_num = models.DecimalField(max_digits=20, decimal_places=0, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'Enumeration'
    