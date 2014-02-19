from django.contrib import admin
from specificationproduct.models import Product, FeatureValue 

class ProductInLine(admin.StackedInline):    
    model = Product
    extra = 1

class FeatureValueAdmin(admin.ModelAdmin):
    fieldsets = [        
        ('Valor', {'fields': ['value']})
    ]
    inlines = [ProductInLine]

admin.site.register(FeatureValue, FeatureValueAdmin)