from django.db import models


# Create your models here.

# create the User model
class User(models.Model):
    # id = models.CharField(max_length=200)
    real_name = models.CharField(max_length=200)
    tz = models.CharField(max_length=200)

    def __str__(self):
        return self.id


# Create the ActivityPeriod model
class ActivityPeriod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.CharField(max_length=200)
    end_time = models.CharField(max_length=200)

    def __str__(self):
        return self.user_id
