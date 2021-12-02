from django.contrib import admin

from .models import Product,Customer,cartitem,Address,rating

admin.site.site_header="my web"
admin.site.site_title="my title"
# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display = ('productname', )
    #list_display=['productname','price','image','category','description']
    readonly_fields = ('thumbnail_preview',)

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    # thumbnail_preview.short_description = 'Thumbnail Preview'
    # thumbnail_preview.allow_tags = True

admin.site.register(Product, AdminProduct)

class AdminCustomer(admin.ModelAdmin):
    list_display=['first_name','email']
    radio_fields={'gender':admin.VERTICAL}
    search_fields=('full_name',)


admin.site.register(Customer, AdminCustomer)

admin.site.register(cartitem)

admin.site.register(Address)
admin.site.register(rating)
