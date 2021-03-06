from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.core.urlresolvers import reverse
from django.conf import settings

class Reading(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL)
  reading = models.FloatField()
  when = models.DateTimeField(auto_now_add=True)

  READING_TYPES = (
    ('WGHT', 'Weight'),
    ('HEHT', 'Height'),
    ('BLSG', 'Blood Sugar'),
    ('PLSE', 'Pulse'),
    ('BPRS', 'Blood Pressure'),
  )

  type = models.CharField(max_length=4, choices=READING_TYPES)

  def get_absolute_url(self):
    return reverse('user_detail')

class Activity(models.Model):
  group = models.ForeignKey(Group)
  when = models.DateTimeField()
  where = models.CharField(max_length=255)

  def get_absolute_url(self):
    return reverse('user_detail')

class PhysicalActivity(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL)
  intensity = models.FloatField()
  duration = models.FloatField()
  when = models.DateTimeField(auto_now_add=True)

  ACTIVITY_TYPES = (
    ('JOG', 'Jogging'),
    ('RUN', 'Running'),
    ('SWIM', 'Swimming'),
    ('CYCL', 'Cycling'),
    ('YOGA', 'Yoga'),
    ('SKI', 'Skiing'),
    ('HUNT', 'Being Hunted'),
  )

  type = models.CharField(max_length=4, choices=ACTIVITY_TYPES)
  def get_absolute_url(self):
    return reverse('user_detail')

class User(AbstractUser):
  BOOLEAN_CHOICES = (
      (None, "I do not know now"),
      (True, "Yes"),
      (False, "No")
  )
  BOOLEAN_CHOICES_SEX = (
      (None, "Prefer not to say"),
      (True, "Female"),
      (False, "Male")
  )
  # True = Female, False = Male
  sex = models.NullBooleanField(null=True, blank=True, choices=BOOLEAN_CHOICES_SEX)

  age = models.IntegerField(null=True, blank=True)

  history = models.NullBooleanField(null=True, blank=True, choices=BOOLEAN_CHOICES)

  ETHNICITY_OPTIONS = (
    ('WHT', 'White'),
    ('AFA', 'African American'),
    ('API', 'Asian/Pacific Islanders'),
    ('NA', 'Native American'),
    ('HIS', 'Hispanic/Latino'),
    ('OT', 'Other'),
  )
  ethnicity = models.CharField(max_length=4, choices=ETHNICITY_OPTIONS, null=True, blank=True)

  history_blood_pressure = models.NullBooleanField(null=True, blank=True, choices=BOOLEAN_CHOICES)

  physically_active = models.NullBooleanField(null=True, blank=True, choices=BOOLEAN_CHOICES)

  def __unicode__(self):
    if self.first_name == "":
      return self.name
    return self.first_name

  def get_absolute_url(self):
    return reverse('user_detail')


