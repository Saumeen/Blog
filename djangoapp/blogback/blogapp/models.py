from django.db import models


class Movie(models.Model):
    title= models.CharField(max_length=32)
    desc= models.CharField(max_length=256)
    year = models.IntegerField()


class BlogHome(models.Model):
    name = models.CharField(max_length=64)
    aboutme  = models.CharField(max_length=256)

    class Meta:
        db_table ='wdb_bloghome'