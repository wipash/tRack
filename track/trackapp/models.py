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
	crmID = models.CharField(max_length=100, blank=True, verbose_name='CRM Account Number')

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
	groupName = models.CharField(max_length=100, blank=True)
	totalU = models.SmallIntegerField(blank=True, null=True)
	uStart = models.SmallIntegerField(blank=True, null=True)
	uEnd = models.SmallIntegerField(blank=True, null=True)
	notes = models.TextField(blank=True)
