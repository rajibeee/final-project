from django.db import models

class BookDetails(models.Model):
	details=models.TextField()
	title=models.CharField(max_length=50)
	Author_First=models.CharField(max_length=30)
	Author_Last=models.CharField(max_length=30)
	