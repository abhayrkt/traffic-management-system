from django.contrib import admin
from .models import challan,user,p_user,diversion, news, media,enquiry,City

# Register your models here
admin.site.register(challan)
admin.site.register(user)
admin.site.register(p_user)
admin.site.register(diversion)
admin.site.register(news)
admin.site.register(media)
admin.site.register(enquiry)
admin.site.register(City)
