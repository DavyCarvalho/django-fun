from django.db import models

class Person(models.Model):
    id = models.AutoField(primary_key=True)
    SHIRT_SIZES = (('S', 'Small'),
                  ('M', 'Medium'),
                  ('L', 'Large'),)
    first_name = models.CharField("Person's first name",max_length=30)
    last_name = models.CharField("Persons Last name",max_length=30)
    age = models.IntegerField("Person's age", default=False, blank=True)
    shirt_size = models.CharField("Person's shirt size", max_length=1, choices=SHIRT_SIZES, default=False, blank=True)

class Musician(Person):
    instrument = models.CharField(max_length=100)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()