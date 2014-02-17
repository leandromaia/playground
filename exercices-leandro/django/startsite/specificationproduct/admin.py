from django.contrib import admin
from specificationproduct.models import FeatureValue
from specificationproduct.models import Product
from specificationproduct.models import Feature

admin.site.register(FeatureValue)
admin.site.register(Product)
admin.site.register(Feature)