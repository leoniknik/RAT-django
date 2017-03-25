from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.base_user import AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email, password, firstname, lastname, phone):
        if email and password and firstname and lastname and phone:
            user = self.model(email=self.normalize_email(email), firstname=firstname, lastname=lastname, phone=phone)
            user.set_password(password)
            user.save(using=self._db)
            return user

    def update_user(self, user_id, email, password, firstname, lastname, phone):
        user = User.objects.get(pk=user_id)
        user.email = self.normalize_email(email)
        user.set_password(password)
        user.firstname = firstname
        user.lastname = lastname
        user.phone = phone
        user.save(using=self._db)


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    phone = models.CharField(verbose_name='phone', max_length=11, default="")
    firstname = models.CharField(verbose_name='firstname', max_length=255, default="")
    lastname = models.CharField(verbose_name='lastname', max_length=255, default="")

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_full_name(self):
        return self.firstname + self.lastname

    def get_short_name(self):
        return self.firstname


class Vehicle(models.Model):
    VIN = models.CharField(verbose_name='VIN', max_length=17, default="")
    number = models.CharField(verbose_name='number', max_length=9, default="")
    brand = models.CharField(verbose_name='brand', max_length=255, default="")
    model = models.CharField(verbose_name='model', max_length=255, default="")
    year = models.CharField(verbose_name='year', max_length=4, default="")
    user = models.ForeignKey(User, null=True)

    @staticmethod
    def create_vehicle(VIN, number, brand, model, year, user_id):
        user = User.objects.get(pk=user_id)
        Vehicle.objects.create(VIN=VIN, number=number, brand=brand, model=model, year=year, user=user)

    @staticmethod
    def update_vehicle(vehicle_id, VIN, number, brand, model, year):
        vehicle = Vehicle.objects.get(pk=vehicle_id)
        vehicle.update_vehicle(VIN=VIN, number=number, brand=brand, model=model, year=year)


class CrashDescription(models.Model):
    code = models.CharField(verbose_name='code', max_length=24, default="", unique=True)
    full_description = models.TextField(verbose_name='full_description', default="")
    short_description = models.CharField(verbose_name='short_description', max_length=32, default="")


class Crash(models.Model):
    vehicle = models.ForeignKey(Vehicle, null=True)
    actual = models.BooleanField(verbose_name='actual', default=True, db_index=True)
    description = models.ForeignKey(CrashDescription, null=True)
    date = models.DateField(verbose_name='crash_date', null=True)


class Service(models.Model):
    name = models.CharField(verbose_name='name', max_length=100, default="")
    description = models.TextField(verbose_name='description', default="")
    address = models.CharField(verbose_name='address', max_length=100, default="")
    phone = models.CharField(verbose_name='phone', max_length=11, default="")


class Review(models.Model):
    service = models.ForeignKey(Service, null=True)
    date = models.DateField(verbose_name='review_date', null=True)
    user = models.ForeignKey(User, null=True)
    text = models.TextField(verbose_name='text', default="")


class Offer(models.Model):
    crash = models.ForeignKey(Crash, null=True)
    service = models.ForeignKey(Service, null=True)
    price = models.IntegerField(verbose_name='price', default=0)
    message = models.TextField(verbose_name='message', default="")
