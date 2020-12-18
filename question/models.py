from django.db import models


# Create your models here.

class Subject(models.Model):
    sno = models.AutoField(primary_key= True)
    subID = models.CharField(max_length=2)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.subID + ':' + self.name

class AllQues(models.Model):
    sno = models.AutoField(primary_key=True)
    subID = models.CharField(max_length=20)
    Question = models.TextField()
    optA = models.CharField(max_length=255, blank=True)
    optB = models.CharField(max_length=255, blank=True)
    optC = models.CharField(max_length=255, blank=True)
    optD = models.CharField(max_length=255, blank=True)
    ans = models.CharField(max_length=255, blank=True)
    mark = models.IntegerField()
    level = models.IntegerField()
    timeToSolve = models.CharField(max_length=100, blank=True)
    moreTimeTaken = models.CharField(max_length=100, blank=True)
    lessTimeTaken = models.CharField(max_length=100, blank=True)
    modMark = models.IntegerField()
    modLevel = models.IntegerField()
    teacherName = models.CharField(max_length=20, blank=True)
    subjID = models.CharField(max_length=20, blank=True)
    subjModel = models.CharField(max_length=50, blank=True)
    timeStamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.subID + ' : ' + self.Question + ' | ' + 'Mark: ' + str(self.mark) + ' | ' + 'Level: ' + str(self.level)


# ------------------------------------ MATH -----------------------------------------------


class MathQues(models.Model):
    sno = models.AutoField(primary_key=True)
    intQuesID = models.ForeignKey(AllQues, null=True, on_delete=models.CASCADE)
    Question = models.TextField()
    optA = models.CharField(max_length=255)
    optB = models.CharField(max_length=255)
    optC = models.CharField(max_length=255)
    optD = models.CharField(max_length=255)
    ans = models.CharField(max_length=10)
    mark = models.IntegerField()
    level = models.IntegerField()
    timeToSolve = models.CharField(max_length=100, blank=True)
    moreTimeTaken = models.CharField(max_length=100, blank=True)
    lessTimeTaken = models.CharField(max_length=100, blank=True)
    modMark = models.IntegerField()
    modLevel = models.IntegerField()
    teacherName = models.CharField(max_length=20)
    mathID = models.CharField(max_length=20, blank=True)
    mathModel = models.CharField(max_length=50, blank=True)
    timeStamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.Question + ' | ' + 'Mark: ' + str(self.mark) + ' | ' + 'Level: ' + str(self.level)



# ------------------------------------ PHYSICS -----------------------------------------------


class PhysicsQues(models.Model):
    sno = models.AutoField(primary_key=True)
    intQuesID = models.ForeignKey(AllQues, null=True, on_delete=models.CASCADE)
    Question = models.TextField()
    optA = models.CharField(max_length=255)
    optB = models.CharField(max_length=255)
    optC = models.CharField(max_length=255)
    optD = models.CharField(max_length=255)
    ans = models.CharField(max_length=10)
    mark = models.IntegerField()
    level = models.IntegerField()
    timeToSolve = models.CharField(max_length=100, blank=True)
    moreTimeTaken = models.CharField(max_length=100, blank=True)
    lessTimeTaken = models.CharField(max_length=100, blank=True)
    modMark = models.IntegerField()
    modLevel = models.IntegerField()
    teacherName = models.CharField(max_length=20)
    physicsID = models.CharField(max_length=20, blank=True)
    physicsModel = models.CharField(max_length=50, blank=True)
    timeStamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.Question + ' | ' + 'Mark: ' + str(self.mark) + ' | ' + 'Level: ' + str(self.level)



# --------------------------------------- CHEMISTRY -------------------------------------


class ChemistryQues(models.Model):
    sno = models.AutoField(primary_key=True)
    intQuesID = models.ForeignKey(AllQues, null=True, on_delete=models.CASCADE)
    Question = models.TextField()
    optA = models.CharField(max_length=255)
    optB = models.CharField(max_length=255)
    optC = models.CharField(max_length=255)
    optD = models.CharField(max_length=255)
    ans = models.CharField(max_length=10)
    mark = models.IntegerField()
    level = models.IntegerField()
    timeToSolve = models.CharField(max_length=100, blank=True)
    moreTimeTaken = models.CharField(max_length=100, blank=True)
    lessTimeTaken = models.CharField(max_length=100, blank=True)
    modMark = models.IntegerField()
    modLevel = models.IntegerField()
    teacherName = models.CharField(max_length=20)
    chemistryID = models.CharField(max_length=20, blank=True)
    chemistryModel = models.CharField(max_length=50, blank=True)
    timeStamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.Question + ' | ' + 'Mark: ' + str(self.mark) + ' | ' + 'Level: ' + str(self.level)



# --------------------------------------- ENGLISH ----------------------------------------


class EnglishQues(models.Model):
    sno = models.AutoField(primary_key=True)
    intQuesID = models.ForeignKey(AllQues, null=True, on_delete=models.CASCADE)
    Question = models.TextField()
    optA = models.CharField(max_length=255)
    optB = models.CharField(max_length=255)
    optC = models.CharField(max_length=255)
    optD = models.CharField(max_length=255)
    ans = models.CharField(max_length=10)
    mark = models.IntegerField()
    level = models.IntegerField()
    timeToSolve = models.CharField(max_length=100, blank=True)
    moreTimeTaken = models.CharField(max_length=100, blank=True)
    lessTimeTaken = models.CharField(max_length=100, blank=True)
    modMark = models.IntegerField()
    modLevel = models.IntegerField()
    teacherName = models.CharField(max_length=20)
    englishID = models.CharField(max_length=20, blank=True)
    englishModel = models.CharField(max_length=50, blank=True)
    timeStamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.Question + ' | ' + 'Mark: ' + str(self.mark) + ' | ' + 'Level: ' + str(self.level)






