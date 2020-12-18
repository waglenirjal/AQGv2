import string

from django.http import JsonResponse
from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from aqg.decorators import teacher_only
from question.models import Subject, AllQues, MathQues, PhysicsQues, EnglishQues, ChemistryQues
from django.utils.timezone import now
from django.contrib import messages
import re
from builtins import zip


# Create your views here.

def timeCal(mr, le):
    if int(mr) == 1:
        if int(le) == 3:
            t = 1.5
        elif int(le) == 2:
            t = 1
        else:
            t = 0.5
    elif int(mr) == 2:
        if int(le) == 3:
            t = 3
        elif int(le) == 2:
            t = 2
        else:
            t = 1
    return t


@login_required
@teacher_only
def dashboardTView(request):
    return render(request, 'dashboard/teacher/Dashboard.html')


@login_required
@teacher_only
def selsub(request):
    return render(request, 'dashboard/teacher/TselSub.html')


@login_required
@teacher_only
def selsubforReview(request):
    return render(request, 'dashboard/teacher/TselSubReview.html')


# ------------------------------------ MATH ------------------------------------------

def mathCount():
    allMathQues = MathQues.objects.all()
    count = allMathQues.count()
    sno = allMathQues[count-1].pk
    # print(MathQues.objects.get(pk=5))
    return sno + 1



@login_required
@teacher_only
def mathSel(request):
    global intCosData
    intCosData = 0
    if request.method == 'POST':
        question = request.POST.get('questionArea')
        optA = request.POST.get('optA')
        optB = request.POST.get('optB')
        optC = request.POST.get('optC')
        optD = request.POST.get('optD')
        ans = request.POST.get('answer')
        mark = request.POST.get('mark')
        level = request.POST.get('level')

        if ans == 'optA':
            ans = optA
        elif ans == 'optB':
            ans = optB
        elif ans == 'optC':
            ans = optC
        elif ans == 'optD':
            ans = optD

        timeToSolve = timeCal(mark, level)

        teacherName = request.user.first_name + ' ' + request.user.last_name
        teacherID = request.user.id
        mathID = str(teacherID) + 'M' + str(mathCount())
        mathModel = 'M' + 'mk' + str(mark) + 'le' + str(level) + 'v' + str(mathCount())

        into_all = AllQues(subID='M', Question=question, optA=optA, optB=optB, optC=optC, optD=optD, ans=ans, mark=mark,
                           level=level, teacherName=teacherName, subjID=mathID,
                           timeStamp=now(), subjModel=mathModel, timeToSolve=timeToSolve, moreTimeTaken=0, lessTimeTaken=0, modMark = mark, modLevel= level)
        into_all.save()
        intQusId = AllQues.objects.get(pk=into_all.pk)
        add = MathQues(intQuesID= intQusId, Question=question, optA=optA, optB=optB, optC=optC, optD=optD, ans=ans, mark=mark, level=level,
                       teacherName=teacherName, timeStamp=now(), mathID=mathID, mathModel=mathModel,
                       timeToSolve=timeToSolve, moreTimeTaken=0, lessTimeTaken=0, modMark = mark, modLevel= level)
        add.save()

        messages.success(request, 'Question is added success')

    return render(request, 'dashboard/teacher/AddQuestion/addMath.html')


# ------------------------------------ PHYSICS ------------------------------------------

def physicsCount():
    allPhysicsQues = PhysicsQues.objects.all()
    count = allPhysicsQues.count()
    sno = allPhysicsQues[count - 1].pk
    return sno + 1


@login_required
@teacher_only
def physicsSel(request):
    global intCosData
    intCosData = 0

    if request.method == 'POST':
        question = request.POST.get('questionArea')
        optA = request.POST.get('optA')
        optB = request.POST.get('optB')
        optC = request.POST.get('optC')
        optD = request.POST.get('optD')
        ans = request.POST.get('answer')
        mark = request.POST.get('mark')
        level = request.POST.get('level')

        if ans == 'optA':
            ans = optA
        elif ans == 'optB':
            ans = optB
        elif ans == 'optC':
            ans = optC
        elif ans == 'optD':
            ans = optD

        timeToSolve = timeCal(mark, level)

        teacherName = request.user.first_name + ' ' + request.user.last_name
        teacherID = request.user.id
        physicsID = str(teacherID) + 'P' + str(physicsCount())
        physicsModel = 'P' + 'mk' + str(mark) + 'le' + str(level) + 'v' + str(physicsCount())

        into_all = AllQues(subID='P', Question=question, optA=optA, optB=optB, optC=optC, optD=optD, ans=ans, mark=mark,
                           level=level, teacherName=teacherName,
                           subjID=physicsID, timeStamp=now(), subjModel=physicsModel, timeToSolve=timeToSolve, moreTimeTaken=0, lessTimeTaken=0, modMark = mark, modLevel= level)
        into_all.save()
        intQusId = AllQues.objects.get(pk=into_all.pk)
        add = PhysicsQues(intQuesID= intQusId, Question=question, optA=optA, optB=optB, optC=optC, optD=optD, ans=ans, mark=mark,
                          level=level,
                          teacherName=teacherName, timeStamp=now(), physicsID=physicsID, physicsModel=physicsModel, timeToSolve=timeToSolve, moreTimeTaken=0, lessTimeTaken=0, modMark = mark, modLevel= level)
        add.save()



    messages.success(request, 'Question is added success')
    return render(request, 'dashboard/teacher/AddQuestion/addPhysics.html')


# ------------------------------------ CHEMISTRY ------------------------------------------

def chemistryCount():
    allChemistryQues = ChemistryQues.objects.all()
    count = allChemistryQues.count()
    sno = allChemistryQues[count-1].pk
    return sno + 1


@login_required
@teacher_only
def chemistrySel(request):
    global intCosData
    intCosData = 0
    if request.method == 'POST':
        question = request.POST.get('questionArea')
        optA = request.POST.get('optA')
        optB = request.POST.get('optB')
        optC = request.POST.get('optC')
        optD = request.POST.get('optD')
        ans = request.POST.get('answer')
        mark = request.POST.get('mark')
        level = request.POST.get('level')

        if ans == 'optA':
            ans = optA
        elif ans == 'optB':
            ans = optB
        elif ans == 'optC':
            ans = optC
        elif ans == 'optD':
            ans = optD

        timeToSolve = timeCal(mark,level)

        teacherName = request.user.first_name + ' ' + request.user.last_name
        teacherID = request.user.id
        chemistryID = str(teacherID) + 'C' + str(chemistryCount())
        chemistryModel = 'C' + 'mk' + str(mark) + 'le' + str(level) + 'v' + str(chemistryCount())

        into_all = AllQues(subID='C', Question=question, optA=optA, optB=optB, optC=optC, optD=optD, ans=ans, mark=mark,
                           level=level, teacherName=teacherName,
                           subjID=chemistryID, timeStamp=now(), subjModel=chemistryModel, timeToSolve=timeToSolve, moreTimeTaken=0, lessTimeTaken=0, modMark = mark, modLevel= level)
        into_all.save()
        intQusId = AllQues.objects.get(pk=into_all.pk)
        add = ChemistryQues(intQuesID=intQusId, Question=question, optA=optA, optB=optB, optC=optC, optD=optD, ans=ans, mark=mark,
                            level=level, timeToSolve=timeToSolve,
                            teacherName=teacherName, timeStamp=now(), chemistryID=chemistryID,
                            chemistryModel=chemistryModel, moreTimeTaken=0, lessTimeTaken=0, modMark = mark, modLevel= level)
        add.save()

    messages.success(request, 'Question is added success')
    return render(request, 'dashboard/teacher/AddQuestion/addChemistry.html')


# ------------------------------------ ENGLISH ------------------------------------------

def englishCount():
    allEnglishQues = EnglishQues.objects.all()
    count = allEnglishQues.count()
    sno = allEnglishQues[count-1].pk
    return sno + 1


@login_required
@teacher_only
def englishSel(request):
    global intCosData
    intCosData = 0
    if request.method == 'POST':
        question = request.POST.get('questionArea')
        optA = request.POST.get('optA')
        optB = request.POST.get('optB')
        optC = request.POST.get('optC')
        optD = request.POST.get('optD')
        ans = request.POST.get('answer')
        mark = request.POST.get('mark')
        level = request.POST.get('level')

        if ans == 'optA':
            ans = optA
        elif ans == 'optB':
            ans = optB
        elif ans == 'optC':
            ans = optC
        elif ans == 'optD':
            ans = optD

        timeToSolve = timeCal(mark, level)

        teacherName = request.user.first_name + ' ' + request.user.last_name
        teacherID = request.user.id
        englishID = str(teacherID) + 'E' + str(englishCount())
        englishModel = 'E' + 'mk' + str(mark) + 'le' + str(level) + 'v' + str(englishCount())

        into_all = AllQues(subID='E', Question=question, optA=optA, optB=optB, optC=optC, optD=optD, ans=ans, mark=mark,
                           level=level, teacherName=teacherName, timeToSolve=timeToSolve,
                           subjID=englishID, timeStamp=now(), subjModel=englishModel, moreTimeTaken=0, lessTimeTaken=0, modMark = mark, modLevel= level)
        into_all.save()
        intQusId = AllQues.objects.get(pk=into_all.pk)
        add = EnglishQues(intQuesID=intQusId, Question=question, optA=optA, optB=optB, optC=optC, optD=optD, ans=ans, mark=mark,
                          level=level, timeToSolve=timeToSolve,
                          teacherName=teacherName, timeStamp=now(), englishID=englishID, englishModel=englishModel, moreTimeTaken=0, lessTimeTaken=0, modMark = mark, modLevel= level)
        add.save()


    messages.success(request, 'Question is added success')

    return render(request, 'dashboard/teacher/AddQuestion/addEnglish.html')


# ------------------------------------ SHOW ONLY MINE ------------------------------------------

@login_required
@teacher_only
def allMyPhysics(request):
    new = []
    idd = request.user.id
    pattern = f'^{idd}P[0-9]+$'
    all = PhysicsQues.objects.all()
    print('all:')
    print(all)
    for x in all:
        if re.match(pattern, x.physicsID):
            print('x:')
            print(x)
            new.append(x)
    data = {'all': new}
    print('New:')
    print(new)
    return render(request, 'dashboard/teacher/ReviewQuestion/physics.html', data)


@login_required
@teacher_only
def allMyChemistry(request):
    new = []
    idd = request.user.id
    pattern = f'^{idd}C[0-9]+$'
    all = ChemistryQues.objects.all()
    for x in all:
        if re.match(pattern, x.chemistryID):
            new.append(x)
    data = {'all': new}
    return render(request, 'dashboard/teacher/ReviewQuestion/chemistry.html', data)


@login_required
@teacher_only
def allMyMath(request):
    new = []
    idd = request.user.id
    pattern = f'^{idd}M[0-9]+$'
    all = MathQues.objects.all()
    for x in all:
        if re.match(pattern, x.mathID):
            new.append(x)
    data = {'all': new}
    return render(request, 'dashboard/teacher/ReviewQuestion/math.html', data)


@login_required
@teacher_only
def allMyEnglish(request):
    new = []
    idd = request.user.id
    pattern = f'^{idd}E[0-9]+$'
    all = EnglishQues.objects.all()
    for x in all:
        if re.match(pattern, x.englishID):
            new.append(x)
    data = {'all': new}
    return render(request, 'dashboard/teacher/ReviewQuestion/english.html', data)


@login_required
@teacher_only
def allMyQues(request):
    new = []
    idd = request.user.id
    pattern = f'^{idd}[P, M, C, E][0-9]+$'
    all = AllQues.objects.all()
    for x in all:
        if re.match(pattern, x.subjID):
            new.append(x)
    data = {'all': new}
    return render(request, 'dashboard/teacher/ReviewQuestion/ownQues.html', data)


# ------------------------------------ ALL QUESTIONS ------------------------------------------

@login_required
@teacher_only
def allQues(request):
    all = AllQues.objects.all()
    c = all.count()
    zipping = zip(range(1,c+1), all)
    data = {'all': all, 'count': c, 'zip':zipping}
    return render(request, 'dashboard/teacher/ReviewQuestion/allQuesColl.html', data)


# ------------------------------------ EDIT -------------------------------------------

def editQues(request, id):
    question = AllQues.objects.get(pk=id)
    print(question)
    QuesID = question.subID
    data = {'data': question, 'QuesID':id}

    if request.method == 'POST':
        question = request.POST.get('questionArea')
        optA = request.POST.get('optA')
        optB = request.POST.get('optB')
        optC = request.POST.get('optC')
        optD = request.POST.get('optD')
        ans = request.POST.get('answer')
        mark = request.POST.get('mark')
        level = request.POST.get('level')

        if ans == 'optA':
            ans = optA
        elif ans == 'optB':
            ans = optB
        elif ans == 'optC':
            ans = optC
        elif ans == 'optD':
            ans = optD

        timeToSolve = timeCal(mark, level)

        AllQues.objects.filter(pk=id).update(Question=question, optA=optA, optB=optB, optC=optC, optD=optD, ans=ans, mark=mark,
                           level=level, timeStamp=now(), timeToSolve=timeToSolve, moreTimeTaken=0, lessTimeTaken=0, modMark = mark, modLevel= level)
        if QuesID == 'P':
            PhysicsQues.objects.filter(intQuesID=id).update(Question=question, optA=optA, optB=optB, optC=optC, optD=optD, ans=ans,
                                                 mark=mark,
                                                 level=level, timeStamp=now(), timeToSolve=timeToSolve, moreTimeTaken=0,
                                                 lessTimeTaken=0, modMark=mark, modLevel=level)
        elif QuesID == 'C':
            ChemistryQues.objects.filter(intQuesID=id).update(Question=question, optA=optA, optB=optB, optC=optC,
                                                            optD=optD, ans=ans,
                                                            mark=mark,
                                                            level=level, timeStamp=now(), timeToSolve=timeToSolve,
                                                            moreTimeTaken=0,
                                                            lessTimeTaken=0, modMark=mark, modLevel=level)
        elif QuesID == 'M':
            MathQues.objects.filter(intQuesID=id).update(Question=question, optA=optA, optB=optB, optC=optC,
                                                            optD=optD, ans=ans,
                                                            mark=mark,
                                                            level=level, timeStamp=now(), timeToSolve=timeToSolve,
                                                            moreTimeTaken=0,
                                                            lessTimeTaken=0, modMark=mark, modLevel=level)
        else:
            EnglishQues.objects.filter(intQuesID=id).update(Question=question, optA=optA, optB=optB, optC=optC,
                                                            optD=optD, ans=ans,
                                                            mark=mark,
                                                            level=level, timeStamp=now(), timeToSolve=timeToSolve,
                                                            moreTimeTaken=0,
                                                            lessTimeTaken=0, modMark=mark, modLevel=level)

        messages.success(request, 'Edit Successful')
        return redirect('/teacher/dashboard/selsubReview/')


    return render(request, 'dashboard/teacher/ReviewQuestion/edit/editQues.html', data)


def deleteQues(request, id):
    question = AllQues.objects.get(pk=id)
    print(id)
    question.delete()
    messages.error(request, 'Delete Successful')
    return redirect('/teacher/dashboard/selsubReview/')


data1 = ''
@csrf_exempt
def testLoadCache(request):
    global data1
    lol = request.POST.get('ans')
    data1 = lol
    return HttpResponse('Good Job')

intCosData = 0

@csrf_exempt
def testWriteCache(request):
    global data1, intCosData
    print(data1)
    mark = 0
    level = 0
    QuesData = AllQues.objects.all()
    for i in QuesData:
        cosData = cosineSim(i.Question, data1)
        if cosData != 0.0:
            if cosData >= intCosData:
                intCosData = cosData
                mark = i.mark
                print('mark')
                print(mark)
                level = i.level
                print('level')
                print(level)
                print(i.Question)
                print(cosData)

    return JsonResponse({'mark': mark, 'level': level})


def cosineSim(d1, d2):
    # print(d1)
    # print(d2)
    remPunD1 = remove_punct(d1)
    remPunD2 = remove_punct(d2)
    cosineSimulation = similarityMeasure(remPunD1, remPunD2)
    # print('cosineSimulation')
    # print(cosineSimulation)
    return cosineSimulation



def similarityMeasure(d1, d2):
    x = d1.lower()
    y = d2.lower()
    tok_x = word_tokenize(x)
    tok_y = word_tokenize(y)
    sw = stopwords.words('english')
    l1 = []
    l2 = []
    x_set = {w for w in tok_x if not w in sw}
    y_set = {w for w in tok_y if not w in sw}
    rvector = x_set.union(y_set)
    for w in rvector:
        if w in x_set:
            l1.append(1)  # create a vector
        else:
            l1.append(0)
        if w in y_set:
            l2.append(1)
        else:
            l2.append(0)
    c = 0
    for i in range(len(rvector)):
        c += l1[i] * l2[i]
    cosine = c / float((sum(l1) * sum(l2)) ** 0.5)
    return cosine


def remove_punct(txt):
    txt_nopunt="".join([c for c in txt if c not in string.punctuation])
    return txt_nopunt

