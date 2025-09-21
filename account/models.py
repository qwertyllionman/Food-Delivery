from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass
    """
    role (enum(Customer, Deliver, Admin, Operator)) = user roli 
    """
