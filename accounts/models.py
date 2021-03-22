from django.db import models


# Create your models here.
     #def __str__(self):
     	#return self.name
class customer(models.Model):
	name = models.CharField(max_length = 200,null = True)
	#fathername = models.CharField(max_length = 200, null = True)
	email = models.CharField(max_length = 200, null = True)
	phone_no = models.CharField(max_length = 200, null = True)
	date_enter = models.DateTimeField(auto_now_add= True, null = True)

	def __str__(self):
		return self.name 

class Tags (models.Model):
	name = models.CharField(max_length = 200, null = True)

	def __str__(self):
		return self.name

class products(models.Model):
	CATEGORY = (
		('Indoor','Indoor'),
		('Outdoor','Outdoor'),
		)
	name = models.CharField(max_length = 200,null = True)
	price= models.FloatField(max_length = 200, null = True)
	category = models.CharField(max_length = 200, null = True, choices=CATEGORY)
	description= models.CharField(max_length = 200, null = True)
	date_enter = models.DateTimeField(auto_now_add= True, null = True)
	tags = models.ManyToManyField(Tags)

	def __str__(self):
		return self.name

class orders(models.Model):
	STATUS = (
		('Pending','Pending'),
		('Out for delivery','Out for delivery'),
		('Delivered','Delivered')
		)
	
	customer= models.ForeignKey(customer, null = True,on_delete=models.SET_NULL)
	products= models.ForeignKey(products, null = True, on_delete=models.SET_NULL)
	status = models.CharField(max_length = 200, null = True, choices=STATUS)
	#phone_no = models.CharField(max_length = 200, null = True)
	date_enter = models.DateTimeField(auto_now_add= True, null = True)
	