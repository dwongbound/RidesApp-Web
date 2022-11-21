import uuid

from django.db import models


class User(models.Model):

    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    GRADUATE = 'GR'
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (GRADUATE, 'Graduate'),
    ]

    # id field added for to be verbose, otherwise auto generates
    id = models.BigAutoField(primary_key=True, editable=False)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    middle_initial = models.CharField(max_length=1, blank=True)
    is_driver = models.BooleanField(default=False)
    profile_picture = models.ImageField(blank=True)
    email = models.EmailField(blank=True)
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=JUNIOR,
    )
    # TODO: Add history model and connect to user

    @property
    def display_name(self):
        # Returns the person's full name.
        return f"{self.first_name} {self.middle_initial}. {self.last_name}"
    
    def is_upperclass(self):
        return self.year_in_school in {self.JUNIOR, self.SENIOR}

    def __str__(self):
        # What would print if this class was called
        return f"{self.display_name} - {self.YEAR_IN_SCHOOL_CHOICES[self.year_in_school]} {'Driver' if self.is_driver else 'Rider'}"


class Event(models.Model):
    # id field added automatically. UUID field generated for REST purpopses
    uuid = models.UUIDField(editable=False, unique=True, default=uuid.uuid4)
    name = models.CharField(max_length=40)
    description = models.TextField(max_length=500)
    cost = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    start_time = models.DateTimeField()
    duration = models.DurationField()
    image = models.ImageField(blank=True)
    host = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="user or group who is hosting this event",
        verbose_name="user in charge"
    )
    event_link = models.CharField(help_text="link to event in tapestry website", max_length=100)
    street_address = models.CharField(default="1521 S Hill St.", max_length=50)
    city = models.CharField(default="Los Angeles", max_length=30)
    state = models.CharField(default="CA", max_length=2)
    zip_code = models.IntegerField(default=90015)

class EventUser(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    is_driver = models.BooleanField(default=False)
    accomodations = models.CharField(max_length=100, blank=True)
