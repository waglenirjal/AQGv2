from django.contrib import admin
from .models import Subject, AllQues, MathQues, PhysicsQues, EnglishQues, ChemistryQues

# Register your models here.

admin.site.register(AllQues)
admin.site.register(Subject)
admin.site.register(MathQues)
admin.site.register(PhysicsQues)
admin.site.register(EnglishQues)
admin.site.register(ChemistryQues)

