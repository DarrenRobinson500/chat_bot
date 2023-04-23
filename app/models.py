from django.db import models

class Label(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Past(models.Model):
    question = models.CharField(max_length=250)
    answer = models.TextField(max_length=5000)
    label = models.ForeignKey(Label, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.question

    def clean_text(self):
        if self.answer[0:1] == "?":
            self.answer = self.answer[2:]
            self.save()
        return

class User(models.Model):
    label = models.ForeignKey(Label, null=True, on_delete=models.SET_NULL)


