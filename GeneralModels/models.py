from django.db import models

# Create your models here.

# ----------- Enumeration Entities-------------------
class EnumerationType(models.Model):
    enumTypeId = models.CharField(primary_key = True, max_length = 100)
    description = models.CharField(max_length = 200)


    class Meta:
        db_table = 'EnumerationType'


class Enumeration(models.Model):
    enumId = models.CharField(primary_key = True, max_length = 100)
    enumTypeId = models.ForeignKey(
        'EnumerationType', on_delete=models.SET_NULL, null=True, blank=True, db_column='ENUM_TYPE_ID'
    )
    parent_enum_id = models.CharField(max_length=40, null=True, blank=True)
    enumCode = models.CharField(max_length=255, null=True, blank=True)
    sequenceId = models.DecimalField(max_digits=20, decimal_places=0, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)


    class Meta:
        db_table = 'Enumeration'


# ------------- Uom Entities -------------------
class UomType(models.Model):
    uomTypeId = models.CharField(primary_key = True, max_length = 100)
    parentTypeId = models.ForeignKey('self', on_delete = models.CASCADE)
    hasTable = models.CharField(max_length = 1)
    description = models.CharField(max_length = 50)


    class Meta:
        db_table = 'UomType'


class Uom(models.Model):
    uomId = models.CharField(primary_key = True, max_length = 100)
    uomTypeId = models.ForeignKey(UomType, on_delete = models.CASCADE)
    abbreviation = models.CharField(max_length = 10)
    numericCode = models.IntegerField()
    description = models.CharField(max_length = 100)


    class Meta:
        db_table = 'Uom'