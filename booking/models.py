
from django.db import models
import uuid


class Booking(models.Model):
    booking = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    working_spaces = models.ManyToManyField('working_spaces.WorkingSpaces', through='BookingSpace')

    def __str__(self):
        return f'{self.booking} - {self.user}'

    class Meta:
        db_table = 'booking'


class BookingSpace(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    working_spaces = models.ForeignKey('working_spaces.WorkingSpaces', on_delete=models.CASCADE)
    booking_date = models.DateField(null=False, blank=False)
    start_time = models.TimeField(null=False, blank=False)
    end_time = models.TimeField(null=False, blank=False)

    def __str__(self):
        return f'{self.booking} - {self.working_spaces} - {self.booking_date}'

    class Meta:
        db_table = 'booking_space'
