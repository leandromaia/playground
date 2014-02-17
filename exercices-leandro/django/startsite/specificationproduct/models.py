from django.db import models

class FeatureValue(models.Model):
    value = models.IntegerField(default=0)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    feature_value = models.ForeignKey(FeatureValue)

class Feature(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=256)
    feature_value = models.ForeignKey(FeatureValue)      

class ProductSpec(models.Model):
    name = models.CharField(max_length=100)
    product = models.ForeignKey(Product)
    feature = models.ForeignKey(Feature)