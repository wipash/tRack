from django.db import models

# Create your models here.

class Rack(models.Model):
	number = models.SmallIntegerField()
	floor = models.SmallIntegerField()
	size = models.SmallIntegerField()

	def __unicode__(self):
		return str(self.number)

	
class Customer(models.Model):
	name = models.CharField(max_length=100)
	crmID = models.CharField(max_length=100)

	def __unicode__(self):
		return str(self.name)
	
	
class VLAN(models.Model):
	customer = models.ForeignKey('Customer')
	number = models.SmallIntegerField()
	name = models.CharField(max_length=50)

	def __unicode__(self):
		return str(self.number)


class Network(models.Model):
	network = models.GenericIPAddressField()
	subnet = models.SmallIntegerField()
	vlan = models.ForeignKey('VLAN')
	
	def __unicode__(self):
		return u'%s/%s' % (self.network, self.subnet)


class VLANRack(models.Model):
	rack = models.ForeignKey('Rack')
	vlan = models.ForeignKey('VLAN')
	
class CustomerRack(models.Model):
	rack = models.ForeignKey('Rack')
	customer = models.ForeignKey('Customer')
	groupName = models.CharField(max_length=100)
	totalU = models.SmallIntegerField()
	uStart = models.SmallIntegerField()
	uEnd = models.SmallIntegerField()
	notes = models.TextField()
