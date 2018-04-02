from django.db import models

class Teacher(models.Model):
    t_id = models.AutoField(primary_key=True)
    t_name = models.TextField()

    def __str__(self):
        return self.t_name

class Student(models.Model):
    s_id = models.AutoField(primary_key=True)
    s_name = models.TextField()
    t_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.s_name
    