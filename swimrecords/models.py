from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


def stroke_check(stroke):
    list_of_swims = ['front crawl', 'butterfly', 'breast', 'back', 'freestyle']
    if stroke not in list_of_swims:
        raise ValidationError(f"{stroke} is not a valid stroke")


def distance_check(distance):
    limit = 50
    if distance <= limit:
        raise ValidationError(f"Ensure this value is greater than or equal to {limit}.")


def record_date_check(record_date):
    now = timezone.now()
    if record_date > now:
        raise ValidationError("Can't set record in the future.")


def record_broken_check(record_broken_date):
    if record_broken_date < timezone.now():
        raise ValidationError("Can't break record before record was set.")


def test_relay_true_false(value):
    if value != bool or value is None:
        raise ValidationError("Can't set anything but booleans for relays.")


class SwimRecord(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    team_name = models.CharField(max_length=255)
    relay = models.BooleanField(default=False, validators=[test_relay_true_false])
    stroke = models.CharField(max_length=255, validators=[stroke_check])
    distance = models.IntegerField(validators=[distance_check])
    record_date = models.DateTimeField(validators=[record_date_check])
    record_broken_date = models.DateTimeField(validators=[record_broken_check])
