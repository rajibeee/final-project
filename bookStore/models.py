from django.db import models

class BookDetails(models.Model):
	details=models.TextField()
	title=models.CharField(max_length=100)
	Author_First=models.CharField(max_length=50)
	Author_Last=models.CharField(max_length=50)
	price=models.FloatField()
	quanity_remaining=models.IntegerField()
	photo=models.ImageField(null=True,blank=True)
	timeAdded=models.DateTimeField(auto_now=True)
