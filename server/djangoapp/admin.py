from django.contrib import admin
# from .models import related models
from .models import CarMake, CarModel


# Register your models here.


# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 5

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'name', 'description']
    inlines = [CarModelInline]

# CarMakeAdmin class with CarModelInline
class CarMakeInline(admin.StackedInline):
    model = CarMake
    extra = 5

class CarMakeAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'name', 'description']
    inlines = [CarMakeInline]



# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)