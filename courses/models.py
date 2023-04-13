from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=200)
    language = models.CharField(max_length=100)
    price = models.CharField(max_length=10)

    # für die Anzeige im admin Bereich
    def __str__(self):
        return self.name
    
class Geburtstag(models.Model):
    vorname = models.CharField(max_length=100)
    nachname = models.CharField(max_length=100)
    rufname = models.CharField(max_length=100)
    geburtstag = models.CharField(max_length=100)

    # für die Anzeige im admin Bereich
    def __str__(self):
        return self.vorname
