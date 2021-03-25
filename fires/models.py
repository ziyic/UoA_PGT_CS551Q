from django.db import models


class Region(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=100)
    ISOCODE = models.TextField(max_length=3)
    UNSDCODE = models.IntegerField()
    CIESINCODE = models.IntegerField()
    Population = models.IntegerField(null=True)
    Area_sqkm = models.FloatField()

    def __str__(self):
        return f'{self.id},{self.name},{self.ISOCODE},{self.UNSDCODE},' \
               f'{self.CIESINCODE},{self.Population},{self.Area_sqkm}'


class FireType(models.Model):
    id = models.AutoField(primary_key=True)
    type_name = models.TextField()

    def __str__(self):
        return f'{self.id},{self.type_name}'


class FireTCC(models.Model):
    region = models.ForeignKey(Region, on_delete=models.DO_NOTHING)
    type = models.ForeignKey(FireType, on_delete=models.DO_NOTHING)
    year = models.IntegerField()
    amount = models.FloatField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['region', 'type', 'year'], name='unique_fire')
        ]

    def __str__(self):
        return f'{self.region},{self.year},{self.type},{self.amount}'
