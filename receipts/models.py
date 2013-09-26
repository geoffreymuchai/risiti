from django.db import models

class Receipt(models.Model):
	date = models.DateField()
	bought_from = models.ForeignKey('Merchant')
	description = models.TextField()
	category = models.ForeignKey('Category')
	account_to_credit = models.ForeignKey('Account')
	price = models.DecimalField(max_digits=9, decimal_places=2)
	recepient_image = models.ImageField()

class Merchant(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	total_amount_debited = models.DecimalField(max_digits=9, decimal_places=2)

class Category(models.Model):
	name = models.CharField(max_length=255)
	value = models.CharField(max_length=255)

class Account(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	account_type = models.CharFields(max_length=255)
	amount = models.DecimalField(max_digits=9, decimal_places=2)


