from django.db import models

class Persona(models.Model):
	nombre = models.CharField(max_length=255)
	email = models.EmailField()

	def __unicode__(self):
		return self.nombre