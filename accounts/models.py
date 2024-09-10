from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Country(models.Model):
    name = models.CharField(max_length=30)
    abbr = models.CharField(max_length=5)
    is_active = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
        db_table = 'countries'

    
class Profile(models.Model):
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.BigIntegerField(blank=True,null=True,unique=True)
    country = models.ForeignKey(to=Country , on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True,null=True)

class Device(models.Model):
    DEVICE_WEB , DEVICE_IOS , DEVICE_ANDROID , DEVICE_DESKTOP = 1 , 2 , 3 , 4
    DEVICE_TYPE_CHOICE = (
        (DEVICE_WEB , 'web'),
        (DEVICE_IOS , 'ios'),
        (DEVICE_ANDROID , 'android'),
        (DEVICE_DESKTOP , 'desktop')
    )

    user = models.ForeignKey(to=settings.AUTH_USER_MODEL , related_name='devices' , on_delete=models.CASCADE)
    device_uuid = models.UUIDField('device UUID' , null=True)
    last_login = models.DateTimeField('last login date' , null=True)
    device_type = models.PositiveSmallIntegerField(choices=DEVICE_TYPE_CHOICE , default=DEVICE_WEB)
    device_os = models.CharField('device os' , max_length=20 , blank=True)
    device_model = models.CharField('device model', max_length=50, blank=True)
    app_version = models.CharField('app version', max_length=20, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)



