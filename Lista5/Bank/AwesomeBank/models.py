from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator
from django.utils import timezone


# Create your models here.
class PreparedTransfer(models.Model):
    regex_validator = RegexValidator(regex='[0-9]{26}', message='Wrong account number - not enough numbers')
    sender = models.ForeignKey(User, null=False, editable=False, on_delete=models.PROTECT)
    recipient_name = models.CharField(null=False, blank=False, max_length=80)
    recipient_account = models.CharField(validators=[regex_validator], null=False, max_length=26)
    title = models.CharField(null=False, blank=False, max_length=256)
    amount = models.DecimalField(null=False, decimal_places=2, max_digits=10, validators=[MinValueValidator(0.01)])
    date = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)


class Transfer(models.Model):
    sender = models.ForeignKey(User, null=False, editable=False, on_delete=models.PROTECT)
    recipient_name = models.CharField(null=False, blank=False, max_length=80)
    recipient_account = models.CharField(null=False, max_length=26)
    title = models.CharField(null=False, blank=False, max_length=256)
    amount = models.DecimalField(null=False, decimal_places=2, max_digits=10)
    date = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)
