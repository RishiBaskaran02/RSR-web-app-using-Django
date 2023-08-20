from django.contrib import admin
from APP.models import signin
from APP.models import OfficeSignin
from APP.models import Adminsignin
from APP.models import Verification
from APP.models import Product

# Register your models here.

admin.site.register(signin)
admin.site.register(OfficeSignin)
admin.site.register(Adminsignin)
admin.site.register(Verification)
admin.site.register(Product)
