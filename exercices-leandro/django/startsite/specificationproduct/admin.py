from django.contrib import admin
from specificationproduct.models import Feature, FeatureValue 
from specificationproduct.models import Product, ProductSpec

class FeatureInLine(admin.StackedInline):    
    model = Feature
    extra = 1

class FeatureValueAdmin(admin.ModelAdmin):
    fieldsets = [        
        ('Valor', {'fields': ['value']})
    ]
    inlines = [FeatureInLine]
    list_display = ['value']

class ProductSpecInLine(admin.StackedInline):
    fieldsets = [
        (None, {'fields': ['name','feature']})
    ]
    model = ProductSpec
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Valores Basicos', {'fields': ['name','price', 'feature_value']})]
    inlines = [ProductSpecInLine]
    list_display = ('name', 'price','feature_value')

admin.site.register(FeatureValue, FeatureValueAdmin)
admin.site.register(Product, ProductAdmin)