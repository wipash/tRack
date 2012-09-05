from django.http import HttpResponse
from django.contrib import auth
from django.template.loader import get_template
from django.template import Context
from models import Customer, Network, VLAN, Rack, VLANRack, CustomerRack 


def trackapp_main(request):
	
	rackList = Rack.objects.all()
	
	t = get_template('main.html')
	html = t.render(Context({'racklist': rackList}))
	return HttpResponse(html)



