from django.contrib import admin
from .models import Staff, TransferHistory
# Register your models here.


#register and adds a search button to the staff page in the admin section
@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    search_fields = ['name'] #searches by name

#register the
admin.site.register(TransferHistory)

#changes the default view site url in the admin to the homepage of the transfers
admin.site.site_url = "/transfers"