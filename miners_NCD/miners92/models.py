from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=225)
    nationality = models.CharField(max_length=225)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()


    def __str__(self):
        return self.email

class WorkerCluster(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    num_workers = models.IntergerField()


class PerformanceMetrics(models.Model):
    worker_cluster = models.ForeignKey(WorkerCluster, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    hashrate = models.FloatField()
    efficiency = models.FloatField()


class Metric(models.Model):
    name = models.CharField(max_length=225)
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)


class Alert(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    alert_type = models.CharField(max_length=225)
    message = models.TextField()
