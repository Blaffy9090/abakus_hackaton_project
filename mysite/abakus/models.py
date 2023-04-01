from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    time = models.DateTimeField('date published')
    location = models.CharField(max_length=200)
    description = models.TextField()
    content = models.ImageField(upload_to='abakus/static/images', height_field='img_height', width_field='img_height')
    description1 = models.TextField()
    content1 = models.ImageField(upload_to='abakus/static/images2', height_field='img_height', width_field='img_height')
    img_width = 600
    img_height = 400

    # def save(self, *args, **kwargs):
    #     if self.pk is None:
    #         self.model = Question.objects.create(id=self.id)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name
