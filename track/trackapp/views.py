from django.http import HttpResponse
from django.contrib import auth
from django.template.loader import get_template
from django.template import Context
from models import Customer, Network, VLAN, Rack, VLANRack, CustomerRack 


def trackapp_main(request):
	
	rackList = Rack.objects.all()
	customerList = Customer.objects.all()
	vlanList = VLAN.objects.all()
	networkList = Network.objects.all()

	disp = {}

	for rack in rackList
		dnumber = rack.number
		


	t = get_template('main.html')
	html = t.render(Context({'racklist': rackList}))
	return HttpResponse(html)


def searchRack():
	pass

def searchNetwork():
	pass

def searchCustomer():
	pass

def searchVLAN():
	pass
