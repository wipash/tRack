from django.db import models

# Create your models here.

class Rack(models.Model):
	number = models.SmallIntegerField()
	floor = models.SmallIntegerField()
	size = models.SmallIntegerField()
	
class Customer(models.Model):
	name = models.CharField(max_length=100)
	crmID = models.CharField(max_length=100)
	
	
class VLAN(models.Model):
	customer = models.ForeignKey('Customer')
	number = models.SmallIntegerField()
	name = models.CharField(max_length=50)

class Network(models.Model):
	network = GenericIPAddressField(protocol=both, unpack_ipv4=false)
	subnet = IPAddressField()
	vlan = models.ForeignKey('VLAN')
	
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