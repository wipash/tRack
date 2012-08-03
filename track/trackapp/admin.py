from django.contrib import admin
from track.trackapp.models import Rack, Customer, VLAN, Network

admin.site.register(Rack)
admin.site.register(Customer)
admin.site.register(VLAN)
admin.site.register(Network)
