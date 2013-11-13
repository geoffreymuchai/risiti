from django.db import models


def get_default_merchant():
	Merchant.objects.get_or_create(name="Miscellaneous")[0]
def get_default_category():
	Category.objects.get_or_create(name="Miscellaneous")[0]
def get_default_account():
	Account.objects.get_or_create(name="Miscellaneous")[0]

class Receipt(models.Model):

	date_created = models.DateTimeField(auto_now_add=True)
	date = models.DateField()
	bought_from = models.ForeignKey('Merchant', default=get_default_merchant)
	description = models.TextField()
	category = models.ForeignKey('Category', default=get_default_category)
	account_to_credit = models.ForeignKey('Account', default=get_default_account)
	price = models.DecimalField(max_digits=9, decimal_places=2)
	image = models.ImageField(upload_to='receipts/%Y/%m/%d')

	def __unicode__(self):
		return "%s | %s | %s" % (
				self.date,
				self.bought_from,
				self.description)

class Merchant(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField(blank=True)
	total_amount_debited = models.DecimalField(max_digits=9, decimal_places=2, default=0.0)

	def __unicode__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=255)
	value = models.CharField(max_length=255)

	def __unicode__(self):
		return self.name

class Account(models.Model):
	name = models.CharField(max_length=255, unique=True)
	description = models.TextField(blank=True)
	account_type = models.CharField(max_length=255, default="Miscellaneous")
	amount = models.DecimalField(max_digits=9, decimal_places=2, default=0.0)

	def __unicode__(self):
		return self.name


