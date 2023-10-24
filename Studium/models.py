from django.db import models

class Idea(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()


class Flashcard(models.Model):
    content = models.TextField()
    answer = models.TextField()
    category = models.CharField(max_length=50)
    level = models.IntegerField()
    rating = models.FloatField()
    comment = models.TextField(blank=True, null=True) # *empty value
    created_date = models.DateTimeField(auto_now_add=True) # a date and time with an automatic value setting

    def __str__(self):
        return self.content # returning the single content


