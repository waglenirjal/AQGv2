from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class PerStudentData(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    Mark = models.CharField(max_length=2)
    Level = models.CharField(max_length=20)
    NOQ = models.CharField(max_length=50, null=True)
    Physics = models.CharField(max_length=5, null=True)
    Chemistry = models.CharField(max_length=5, null=True)
    Math = models.CharField(max_length=5, null=True)
    English = models.CharField(max_length=5, null=True)

    def __str__(self):
        return str(self.User)


class PerQuestionForCertificates(models.Model):
    sno = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    QuesId = models.CharField(max_length=50, null=True)
    IntQuesID = models.CharField(max_length=255, blank=True)
    Solved = models.BooleanField(default=False, null=True)
    SolvedTimes = models.CharField(max_length=50, null=True)
    TimeTaken = models.CharField(max_length=50, null=True)


    def __str__(self):
        return str(self.user) + ' | ' + str(self.QuesId) + ' | ' + str(self.Solved)


class levelUpDec(models.Model):
    sno = models.AutoField(primary_key= True)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    level = models.IntegerField(null=True)
    percentage = models.CharField(max_length=50, null=True)

    def __str__(self):
        return str(self.User) + ' | '  + str(self.percentage) + '%'  + ' | ' + 'Level: ' + str(self.level)


class PerStudentCache(models.Model):
    sno = models.AutoField(primary_key=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Did = models.CharField(max_length=22, null=True)
    QuesID = models.CharField(max_length=255, blank=True)
    IntQuesID = models.CharField(max_length=255, null=True)
    Question = models.TextField()
    ans = models.CharField(max_length=255, blank=True)
    UserAns = models.CharField(max_length=255, blank=True)
    Solved = models.BooleanField(null=True, default=False)
    QTime = models.CharField(max_length=255, blank=True)
    TimeTaken = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return str(self.User) + ' | ' + str(self.IntQuesID) + ' | ' + str(self.Solved) + ' | ' + str(self.Did) + ' | ' + str(self.TimeTaken)


class Bookmarked(models.Model):
    sno = models.AutoField(primary_key=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    QuesID = models.CharField(max_length=255, blank=True)
    IntQuesID = models.CharField(max_length=255, null=True)
    Question = models.TextField()
    optA = models.CharField(max_length=255, blank=True)
    optB = models.CharField(max_length=255, blank=True)
    optC = models.CharField(max_length=255, blank=True)
    optD = models.CharField(max_length=255, blank=True)
    ans = models.CharField(max_length=255, blank=True)


    def __str__(self):
        return str(self.User) + ' | ' + str(self.IntQuesID) + ' | ' + str(self.Question)