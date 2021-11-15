from django.db.models import Model, CharField, DateTimeField, FloatField, ForeignKey, SET_NULL, ManyToManyField

# Create your models here.


class Gender(Model):
	CATEGORY = (('Male', 'Male'), ('Female', 'Female'))
	category = CharField(max_length=200, null=True, choices=CATEGORY)

	def __str__(self):
		return self.category


class SportCategory(Model):
	category = CharField(max_length=200, null=True)

	def __str__(self):
		return self.category


class OutdoorIndoor(Model):
	CATEGORY = (('Indoor', 'Indoor'), ('Outdoor', 'Outdoor'))
	category = CharField(max_length=200, null=True, choices=CATEGORY)

	def __str__(self):
		return self.category


class Rental(Model):
	available = CharField(max_length=200, null=True)

	def __str__(self):
		return self.available


class Status(Model):
	CATEGORY = (('Available', 'Available'), ('Unavailable', 'Unavailable'))
	status = CharField(max_length=200, null=True, choices=CATEGORY)

	def __str__(self):
		return self.status


class Product(Model):
	name = CharField(max_length=200, null=True)
	price = FloatField(null=True)
	status = ForeignKey(Status, null=True, on_delete=SET_NULL)
	rental_price = FloatField(null=True)
	rental = ForeignKey(Rental, null=True, on_delete=SET_NULL)
	item_type = ManyToManyField(OutdoorIndoor)
	category = ManyToManyField(SportCategory)
	gender = ManyToManyField(Gender)
	description = CharField(max_length=200, null=True)
	date_created = CharField(max_length=200, null=True)

	def __str__(self):
		return self.name
