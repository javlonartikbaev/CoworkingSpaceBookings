from django.db import models
import uuid


class TypeOfWorkingSpaces(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'type_of_working_spaces'


class WorkingSpaces(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name_of_space = models.CharField(max_length=100)
    type_of_space = models.ForeignKey(TypeOfWorkingSpaces, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена за час")
    description = models.TextField()
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name_of_space} - {self.type_of_space}'

    class Meta:
        db_table = 'working_spaces'


class ImageWorkingSpaces(models.Model):
    image = models.ImageField(upload_to='working_spaces/')
    working_space = models.ForeignKey(WorkingSpaces, on_delete=models.CASCADE)

    class Meta:
        db_table = 'image_working_spaces'
