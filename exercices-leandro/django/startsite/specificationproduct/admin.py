from django.contrib import admin
from specificationproduct.models import Product, Feature, FeatureValue

class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Campos de Valores', {'fields': ['price','feature_value']}),
    ]    

class FeatureAdmin(admin.StackedInline):
    fieldsets = [
        ('Nome',               {'fields': ['name']}),
        ('Descricao', {'fields': ['description']}),
        ('Valor da Feature', {'fields': ['feature_value']})
    ] 
    model = Feature
    extra = 1

class FeatureValueAdmin(admin.ModelAdmin):
    fieldsets = [        
        ('Valor', {'fields': ['value']})
    ]
    inlines = [FeatureAdmin]

admin.site.register(Product, ProductAdmin)
admin.site.register(FeatureValue, FeatureValueAdmin)
