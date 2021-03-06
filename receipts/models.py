from django.db import models
from django.db.models.signals import post_save

from utils import tesseract

from django.conf import settings

def get_default_merchant():
	Merchant.objects.get_or_create(name="Miscellaneous")[0]
def get_default_category():
	Category.objects.get_or_create(name="Miscellaneous")[0]
def get_default_account():
	Account.objects.get_or_create(name="Miscellaneous")[0]


class Payment(models.Model):
	date_created = models.DateTimeField(auto_now_add=True)
	date = models.DateField()
	bought_from = models.ForeignKey('Merchant', default=get_default_merchant)
	description = models.TextField(blank=True)
	category = models.ForeignKey('Category', default=get_default_category)
	account_to_credit = models.ForeignKey('Account', default=get_default_account)
	price = models.DecimalField(max_digits=9, decimal_places=2)
	image = models.ImageField(upload_to='receipts/%Y/%m/%d', blank=True)

	def __unicode__(self):
		return "%s | %s | %s" % (
				self.date,
				self.bought_from,
				self.description)

class Receipt(models.Model):
	date_created = models.DateTimeField(auto_now_add=True)
	receipt = models.ForeignKey('Payment')
	description = models.TextField(blank=True)

def scan_receipts_for_text(sender, instance, created, **kwargs):
	if created and instance.image:
		image_path = settings.PROJECT_PATH + instance.image.url
		print "Scanning image path:%s for text" % (image_path)
		if image_path is not '':
			try:
				image_text = tesseract.image_file_to_string(image_path, graceful_errors=True)
				receipt_text = Receipt(receipt=instance, text=image_text)
				receipt_text.save()
			except Exception, e:
				print "An error occurred while processing the image"	
		else:
			print "No image to scan :("

post_save.connect(scan_receipts_for_text, sender=Payment, dispatch_uid="get_image_text")

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
