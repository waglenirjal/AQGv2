from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import requests

from django.contrib.auth.models import User
from aqg.decorators import student_only
from Register.models import UserDetail
import re, random
from django.core.paginator import Paginator
from Dashboard.models import PerStudentData, levelUpDec, PerStudentCache, PerQuestionForCertificates, Bookmarked
from question.models import Subject, AllQues, MathQues, PhysicsQues, EnglishQues, ChemistryQues
from django.http import JsonResponse


# Create your views here.

outQues =[]
numQues = []
outQues1 = []
outQues2 = []
DataToShow1 = []
DataToShow2 = []
anslist = []
mainAns = []
perAns = []
timekeeper = []
mark = 0
level = 0

def saveAns(request):
    ans = request.GET['ans']
    print(ans)

@login_required
@student_only
def dashboardView(request):
    global outQues1, outQues2, anslist, mainAns, perAns,timekeeper
    outQues1 = []
    outQues2 = []
    anslist = []
    mainAns = []
    perAns = []
    timekeeper = []
    name = request.user

    glevel = request.user.userdetail.glevel
    print('Name : ')
    print(name)
    print(f'Level : '+ glevel)
    levelUpDecide(name, glevel)
    UserMe = request.user
    PSC = PerStudentCache.objects.all()
    if PSC.exists():
        for i in PSC:
            if i.User == UserMe:
                i.delete()

    return render(request, 'dashboard/student/dashHome.html')


def blogs(request):
    return render(request, 'dashboard/blogs.html')

def resources(request):
    return render(request, 'dashboard/Resources/All.html')

def resPhy(request):
    return render(request, 'dashboard/Resources/Physics.html')

def resChe(request):
    return render(request, 'dashboard/Resources/Chemistry.html')

def resMath(request):
    return render(request, 'dashboard/Resources/Math.html')

def resEng(request):
    return render(request, 'dashboard/Resources/English.html')

def bookmark(request):
    booked = Bookmarked.objects.filter(User=request.user)
    lenOfBook = len(booked)
    num = 0
    paramss = {'booked':booked, 'num':num}
    return render(request, 'dashboard/student/bookmark.html', paramss)

@csrf_exempt
def book(request):
    ques_tag = request.POST.get('ques_tag')
    print(ques_tag)
    userMe = request.user
    print(userMe)
    print(userMe.id)
    allQuestion = AllQues.objects.filter(pk=ques_tag)
    booked = Bookmarked.objects.filter(User=userMe,IntQuesID=ques_tag)
    print(allQuestion)
    print('booked')
    print(booked)
    if not booked:
        print('lol entered')
        for i in allQuestion:
            book = Bookmarked(User=userMe,QuesID=i.subjID,IntQuesID=i.pk,Question=i.Question,optA=i.optA,optB=i.optB,optC=i.optC,optD=i.optD,ans=i.ans)
            book.save()
    else:
        print('I am here')
        pass
    return HttpResponse('DOne')


@csrf_exempt
def delbook(request):
    quesID = request.POST.get('quesID')
    print('quesID')
    print(quesID)
    toDel = Bookmarked.objects.filter(User=request.user, IntQuesID=int(quesID))
    print(toDel)
    toDel.delete()
    return render(request, 'dashboard/student/bookmark.html')


@login_required
@student_only
def qBankView(request):
    print('hello')
    global outQues, numQues, mark, level
    outQues = []
    numQues = []
    mark = 0
    level = 0
    PSD = PerStudentData.objects.all()
    print(PSD)

    if PSD.exists():
        print('I have entered here')
        ddata = PerStudentData.objects.get(User=request.user)
        ddata.delete()

    if request.method == 'POST':
        Physics = request.POST.get('physicsSel')
        Chemistry = request.POST.get('chemistrySel')
        Math = request.POST.get('mathSel')
        English = request.POST.get('englishSel')
        mark = request.POST.get('markSel')
        level = request.POST.get('levelSel')
        numQues = request.POST.get('numQues')

        Pon = Con = Eon = Mon = 0
        if Physics == 'on':
            Pon = 1
        if Chemistry == 'on':
            Con = 1
        if Math == 'on':
            Mon = 1
        if English == 'on':
            Eon = 1

        sdata = PerStudentData(User=request.user, Mark=mark, Level=level, NOQ=numQues, Physics=Pon, Chemistry=Con, Math=Mon, English=Eon)
        sdata.save()

        return redirect('perQuestionView')

    return render(request, 'dashboard/student/QBank.html')



@login_required
@student_only
def perQuestionView(request):
    global outQues, numQues, mark, level, mainAns

    if len(outQues) == 0:
        print('I am inside here --------------------------------------------------------------------')
        data = PerStudentData.objects.filter(User=request.user)
        for i in data:
            Pon = int(i.Physics)
            Con = int(i.Chemistry)
            Mon = int(i.Math)
            Eon = int(i.English)
            numQues = i.NOQ
            print(f'NOQ' + str(numQues))
            mark = i.Mark
            print(f'Mark : '+ str(mark))
            level = i.Level
            print(f'Level : '+ str(level))

        pQuesCol = []
        cQuesCol = []
        mQuesCol = []
        eQuesCol = []
        outQues = []

        Ton = Pon + Con + Mon + Eon
        numQuesNew = int(int(numQues) / Ton)

        if Pon == 1:
            pQc = numQuesNew
            if mark == 'All':
                if level == 'All':
                    pattern = '^Pmk[1,2]le[1,2,3]v[0-9]+$'
                else:
                    pattern = f'^Pmk[1,2]le{level}v[0-9]+$'
            else:
                if level == 'All':
                    pattern = f'^Pmk{mark}le[1,2,3]v[0-9]+$'
                else:
                    pattern = f'^Pmk{mark}le{level}v[0-9]+$'

            print('Pattern ---------------------------------------------------------------------')
            print(pattern)

            data = PhysicsQues.objects.all()
            for x in data:
                if re.match(pattern, x.physicsModel):
                    pQuesCol.append(x)

            cp = len(pQuesCol)
            print(pQuesCol)
            print(cp)
            print(f'Phy : ' + str(pQc))
            if (pQc == 2 or pQc == 12 or pQc == 3 or pQc == 33 or pQc == 6 or pQc == 16):
                pQc = pQc + 1

            print(f'Phy Later: ' + str(pQc))
            print('-----------------------------------------------------------')
            for i in range(int(pQc)):
                n = random.randrange(cp)
                y = pQuesCol[n]
                outQues.append(y)
            print('Out from Physics')

        if Con == 1:
            cQc = numQuesNew

            # pattern = f'^Cmk{mark}le{level}v[0-9]+$'
            if mark == 'All':
                if level == 'All':
                    pattern = '^Cmk[1,2]le[1,2,3]v[0-9]+$'
                else:
                    pattern = f'^Cmk[1,2]le{level}v[0-9]+$'
            else:
                if level == 'All':
                    pattern = f'^Cmk{mark}le[1,2,3]v[0-9]+$'
                else:
                    pattern = f'^Cmk{mark}le{level}v[0-9]+$'

            data = ChemistryQues.objects.all()
            print('Pattern ---------------------------------------------------------------------')
            print(pattern)
            for x in data:
                if re.match(pattern, x.chemistryModel):
                    cQuesCol.append(x)

            cc = len(cQuesCol)
            print(f'CC: ' + str(cc))
            print(f'Che: ' + str(cQc))
            if (cQc == 3 or cQc == 33) and Pon != 1:
                cQc = cQc + 1
            elif (cQc == 2 or cQc == 12 or cQc == 6 or cQc == 16):
                cQc = cQc + 1

            print(f'Che Later: ' + str(cQc))
            print('----------------------------------------------------------------------')
            for i in range(int(cQc)):
                n = random.randrange(cc)
                y = cQuesCol[n]
                outQues.append(y)
            print('Out from Chemistry')

        if Mon == 1:
            mQc = numQuesNew

            # pattern = f'^Mmk{mark}le{level}v[0-9]+$'
            if mark == 'All':
                if level == 'All':
                    pattern = '^Mmk[1,2]le[1,2,3]v[0-9]+$'
                else:
                    pattern = f'^Mmk[1,2]le{level}v[0-9]+$'
            else:
                if level == 'All':
                    pattern = f'^Mmk{mark}le[1,2,3]v[0-9]+$'
                else:
                    pattern = f'^Mmk{mark}le{level}v[0-9]+$'

            data = MathQues.objects.all()
            print('Pattern ---------------------------------------------------------------------')
            print(pattern)
            for x in data:
                if re.match(pattern, x.mathModel):
                    mQuesCol.append(x)

            cm = len(mQuesCol)
            print(f'Math: ' + str(mQc))
            if (mQc == 6 or mQc == 16) and (Pon != 1 or Con != 1):
                mQc = mQc + 1

            print(f'Math Later: ' + str(mQc))

            for i in range(int(mQc)):
                n = random.randrange(cm)
                y = mQuesCol[n]
                outQues.append(y)
            print('Out from Math')

        if Eon == 1:

            # pattern = f'^Emk{mark}le{level}v[0-9]+$'
            if mark == 'All':
                if level == 'All':
                    pattern = '^Emk[1,2]le[1,2,3]v[0-9]+$'
                else:
                    pattern = f'^Emk[1,2]le{level}v[0-9]+$'
            else:
                if level == 'All':
                    pattern = f'^Emk{mark}le[1,2,3]v[0-9]+$'
                else:
                    pattern = f'^Emk{mark}le{level}v[0-9]+$'

            data = EnglishQues.objects.all()
            print('Pattern ---------------------------------------------------------------------')
            print(pattern)
            for x in data:
                if re.match(pattern, x.englishModel):
                    eQuesCol.append(x)

            ce = len(eQuesCol)
            print(f'English : ' + str(numQuesNew))
            for i in range(int(numQuesNew)):
                n = random.randrange(ce)
                y = eQuesCol[n]
                outQues.append(y)
            print('Out from English')

        print('Out Ques -------------')
        print(outQues)

    if mainAns == []:
        for i in outQues:
            mainAns.append(i.ans)

    print('Main Ans ------*******************************************************************')
    print(mainAns)

    paginator = Paginator(outQues, 1)
    page = request.GET.get('page')
    pagQues = paginator.get_page(page)
    print(outQues)

    ziip = zip(range(1,int(numQues)+1), pagQues)
    params = {'dataz':pagQues, 'datas':ziip, 'mark':mark, 'level':level, 'noq':numQues}
    return render(request, 'dashboard/student/perQuestion.html', params)



@login_required
@student_only
def mockTestView(request):

    global outQues1, outQues2, mainAns


    if len(outQues1) == 0:
        phyData = PhysicsQues.objects.all()
        phymk1 = []
        phymk2 = []
        patternMk1 = '^Pmk1le[1,2,3]v[0-9]+$'
        patternMk2 = '^Pmk2le[1,2,3]v[0-9]+$'
        for x in phyData:
            if re.match(patternMk1, x.physicsModel):
                phymk1.append(x)
            if re.match(patternMk2, x.physicsModel):
                phymk2.append(x)
        cp1 = len(phymk1)
        cp2 = len(phymk2)
        for i in range(10):
            n = random.randrange(cp1)
            y = phymk1[n]
            outQues1.append(y)
        for i in range(15):
            n = random.randrange(cp2)
            y = phymk2[n]
            outQues2.append(y)


        cheData = ChemistryQues.objects.all()
        chemk1 = []
        chemk2 = []
        patternMk1 = '^Cmk1le[1,2,3]v[0-9]+$'
        patternMk2 = '^Cmk2le[1,2,3]v[0-9]+$'
        for x in cheData:
            if re.match(patternMk1, x.chemistryModel):
                chemk1.append(x)
            if re.match(patternMk2, x.chemistryModel):
                chemk2.append(x)
        cp1 = len(chemk1)
        cp2 = len(chemk2)
        for i in range(12):
            n = random.randrange(cp1)
            y = chemk1[n]
            outQues1.append(y)
        for i in range(4):
            n = random.randrange(cp2)
            y = chemk2[n]
            outQues2.append(y)


        mathData = MathQues.objects.all()
        mathmk1 = []
        mathmk2 = []
        patternMk1 = '^Mmk1le[1,2,3]v[0-9]+$'
        patternMk2 = '^Mmk2le[1,2,3]v[0-9]+$'
        for x in mathData:
            if re.match(patternMk1, x.mathModel):
                mathmk1.append(x)
            if re.match(patternMk2, x.mathModel):
                mathmk2.append(x)
        cp1 = len(mathmk1)
        cp2 = len(mathmk2)
        for i in range(10):
            n = random.randrange(cp1)
            y = mathmk1[n]
            outQues1.append(y)
        for i in range(15):
            n = random.randrange(cp2)
            y = mathmk2[n]
            outQues2.append(y)


        engData = EnglishQues.objects.all()
        engmk1 = []
        engmk2 = []
        patternMk1 = '^Emk1le[1,2,3]v[0-9]+$'
        patternMk2 = '^Emk2le[1,2,3]v[0-9]+$'
        for x in engData:
            if re.match(patternMk1, x.englishModel):
                engmk1.append(x)
            if re.match(patternMk2, x.englishModel):
                engmk2.append(x)
        cp1 = len(engmk1)
        cp2 = len(engmk2)
        for i in range(14):
            n = random.randrange(cp1)
            y = engmk1[n]
            outQues1.append(y)
        for i in range(4):
            n = random.randrange(cp2)
            y = engmk2[n]
            outQues2.append(y)

        for i in outQues2:
            outQues1.append(i)

        for i in outQues1:
            anslist.append(i.ans)

    sn = len(outQues1)
    print(outQues1)
    print(anslist)

    mainAns = anslist
    ziip = zip(range(1, sn+1), outQues1)

    params = {'all': ziip, 'lol': outQues1}



    return render(request, 'dashboard/student/mockTest.html', params)


@login_required
@student_only
def mockTestInstructView(request):
    return render(request, 'dashboard/student/mockInstruct.html')


@login_required
@student_only
def result(request):
    global perAns, mainAns, timekeeper
    score = 0
    byNum = len(mainAns)
    print(byNum)
    for i in range(len(perAns)):
        if perAns[i] == mainAns[i]:
            score += 1
    percent = '{:.2%}'.format(score / byNum)
    params = {'score': score, 'lst': perAns, 'ans': mainAns, 'percent': percent, 'by':byNum, 'time':timekeeper}
    return render(request, 'dashboard/student/result.html', params)

@csrf_exempt
def dataz(request):
    global perAns
    if request.method == 'POST':
        data = request.POST.getlist('ans')
        print('Answer list')
        print(data)
        perAns = data
        return JsonResponse({'status':'Save', 'stuData':data})
    else:
        return JsonResponse({'status': 0})
    message = 'Received Hai message'
    return HttpResponse(message)

@csrf_exempt
def saveQans(request):
    global perAns
    global timekeeper
    data = request.POST.get('ans')
    timerr = request.POST.get('time')
    ques_tag = request.POST.get('ques_tag')
    print(ques_tag)
    print('DATAAAAA')
    print(data)
    print(timerr)

    #PerStudentCache.objects.filter(Did=int(ques_tag)-1).update(UserAns=data, TimeTaken=timerr)

    perAns.append(data)
    timekeeper.append(timerr)

    print('lst')
    print(perAns)
    message = 'Received Hai message'
    return HttpResponse(message)

@csrf_exempt
def save1ans(request):
    global perAns
    global timekeeper
    data = request.POST.get('ans')
    timerr = request.POST.get('time')
    ques_tag = request.POST.get('ques_tag')
    print(ques_tag)
    print('DATAAAAA')
    print(data)
    print(timerr)

    PerStudentCache.objects.filter(Did=int(ques_tag)-1).update(UserAns=data, TimeTaken=timerr)

    perAns.append(data)
    timekeeper.append(timerr)

    print('lst')
    print(perAns)
    message = 'Received Hai message'
    return HttpResponse(message)


def CerfTestWel(request):
    global DataToShow1, DataToShow2
    DataToShow1 = []
    DataToShow2 = []
    userMe = request.user
    DataBase = PerStudentCache.objects.all()
    print('UserMe')
    print(userMe.id)
    for i in DataBase:
        print('Database')
        print(i.User.pk)

    return render(request, 'dashboard/student/Certificate/welcome.html')


def CerfTest(request):
    global DataToShow1, DataToShow2, mainAns
    glevel = request.user.userdetail.glevel
    #glevel = 1
    print('Glevel')
    print(glevel)
    if len(DataToShow1) == 0:
        callMeForQues(glevel)
        print('Done Call Me')
        for i in DataToShow2:
            DataToShow1.append(i)

        for i in DataToShow1:
            mainAns.append(i.ans)
        print(mainAns)
        l=0
        for i in DataToShow1:
            print(i.intQuesID.pk)
            #PerStudentCache(User=User, QuesID=, Question=, ans=, UserAns=, Solved=,QTime=, TimeTaken=)intQusId = AllQues.objects.get(pk=into_all.pk)
            saveMe = PerStudentCache(User=request.user, Did=l, QuesID=i.sno, Question=i.Question, ans=i.ans, QTime=i.timeToSolve, IntQuesID=i.intQuesID.pk)
            print('Done')
            l = l+1
            saveMe.save()

    noq = len(DataToShow1)

    paginator = Paginator(DataToShow1, 1)
    page = request.GET.get('page')
    pagQues = paginator.get_page(page)

    # ziip = zip(range(1, int(numQues) + 1), pagQues)
    params = {'dataz': pagQues, 'level':glevel, 'noq':noq}

    return render(request, 'dashboard/student/Certificate/perCerfQues.html', params)


def CerfResult(request):
    global perAns, mainAns, timekeeper
    score = 0
    userMe = request.user
    DataBase = PerStudentCache.objects.all()
    byNum = len(mainAns)
    print(byNum)

    #no = 0
    for d in DataBase:
        if (d.UserAns == d.ans):
            PerStudentCache.objects.filter(User=userMe.id).update(Solved=True)
            score += 1
            #no = no + 1

    # for i in DataBase:
    #     print(i.Did)
    #
    # for j in range(len(perAns)):
    #     print('hello3')
    #     if perAns[j] == mainAns[j]:
    #         print('I ma here hai guyz')
    #         PerStudentCache.objects.filter(User=userMe.id, Did=no).update(UserAns=perAns[j], Solved=True, TimeTaken=timekeeper[j])
    #         score += 1
    #         no = no+1
    #     else:
    #         print('Ma yaha pugye I ma here hai guyz')
    #         PerStudentCache.objects.filter(User=userMe.id, Did=no).update(TimeTaken=timekeeper[j])
    #         no = no+1

    name1 = PerStudentCache.objects.filter(User=userMe.id)
    name3 = PerQuestionForCertificates.objects.all()
    print('oggy')
    name4 = PerQuestionForCertificates.objects.filter(user=userMe.id)

    for i in name1:
        checkif = PerQuestionForCertificates.objects.filter(user=userMe.id, IntQuesID=i.IntQuesID)
        print(checkif)
        if checkif:
            for x in checkif:
                if i.IntQuesID == x.IntQuesID:
                    count = int(x.SolvedTimes)
                    if i.Solved == True:
                        count = count + 1
                        print('a')
                        PerQuestionForCertificates.objects.filter(IntQuesID=i.IntQuesID).update(Solved=i.Solved,
                                                                                                SolvedTimes=count,
                                                                                                TimeTaken=i.TimeTaken)
                    else:
                        print('b')
                        PerQuestionForCertificates.objects.filter(IntQuesID=i.IntQuesID).update(TimeTaken=i.TimeTaken)
        else:
            if i.Solved == True:
                print('c')
                saveMe = PerQuestionForCertificates(user=userMe, QuesId=i.QuesID, IntQuesID=i.IntQuesID,
                                                    Solved=i.Solved, SolvedTimes=1, TimeTaken=i.TimeTaken)
                saveMe.save()
            else:
                print('d')
                saveMe = PerQuestionForCertificates(user=userMe, QuesId=i.QuesID, IntQuesID=i.IntQuesID,
                                                    Solved=i.Solved, SolvedTimes=0, TimeTaken=i.TimeTaken)
                saveMe.save()

    percentToSent = int((score / byNum)*100)
    percent = '{:.2%}'.format(score / byNum)
    print(percentToSent)
    glevel = request.user.userdetail.glevel
    levelUpping = levelUpDec(User=userMe, level=glevel, percentage=percentToSent)
    levelUpping.save()
    params = {'score': score, 'lst': perAns, 'ans': mainAns, 'percent': percent, 'by': byNum, 'time': timekeeper}
    return render(request, 'dashboard/student/result.html', params)


def callMeForQues(level):
    global DataToShow1,DataToShow2
    glevel = int(level)
    print('looooool')
    print(glevel)

    if glevel == 1:
        print('level1')
        PhyQuesCall(1,1,11)
        # PhyQuesCall(1,2,2)
        # PhyQuesCall(2,1,16)

        # CheQuesCall(1,1,12)
        # CheQuesCall(1,2,4)
        # CheQuesCall(2,1,4)
        #
        # MathQuesCall(1,1,11)
        # MathQuesCall(1,2,2)
        # MathQuesCall(2,1,16)
        #
        # EngQuesCall(1,1,14)
        # EngQuesCall(1,2,4)
        # EngQuesCall(2,1,4)

        print('DataToShow1')
        print(len(DataToShow1))
        print('DataToShow2')
        print(len(DataToShow2))

    elif glevel == 2:
        print('level2')
        PhyQuesCall(1, 1, 3)
        PhyQuesCall(1, 2, 11)
        PhyQuesCall(2, 1, 3)
        PhyQuesCall(2, 2, 13)

        CheQuesCall(1, 1, 3)
        CheQuesCall(1, 2, 12)
        CheQuesCall(2, 1, 1)
        CheQuesCall(2, 2, 3)

        MathQuesCall(1, 1, 2)
        MathQuesCall(1, 2, 11)
        MathQuesCall(2, 1, 3)
        MathQuesCall(2, 2, 13)

        EngQuesCall(1, 1, 4)
        EngQuesCall(1, 2, 14)
        EngQuesCall(2, 1, 1)
        EngQuesCall(2, 2, 3)

        print('DataToShow1')
        print(len(DataToShow1))
        print('DataToShow2')
        print(len(DataToShow2))

    elif glevel == 3:
        PhyQuesCall(1, 2, 2)
        PhyQuesCall(1, 3, 9)
        PhyQuesCall(2, 2, 16)
        PhyQuesCall(2, 3, 4)

        CheQuesCall(1, 2, 3)
        CheQuesCall(1, 3, 10)
        CheQuesCall(2, 2, 4)
        CheQuesCall(2, 3, 1)

        MathQuesCall(1, 2, 2)
        MathQuesCall(1, 3, 9)
        MathQuesCall(2, 2, 16)
        MathQuesCall(2, 3, 4)

        EngQuesCall(1, 2, 3)
        EngQuesCall(1, 3, 12)
        EngQuesCall(2, 2, 4)
        EngQuesCall(2, 3, 1)

        print('DataToShow1')
        print(len(DataToShow1))
        print('DataToShow2')
        print(len(DataToShow2))

    elif glevel == 4:
        PhyQuesCall(1, 3, 9)
        PhyQuesCall(2, 2, 4)
        PhyQuesCall(2, 3, 19)

        CheQuesCall(1, 3, 10)
        CheQuesCall(2, 2, 2)
        CheQuesCall(2, 3, 5)

        MathQuesCall(1, 3, 9)
        MathQuesCall(2, 2, 4)
        MathQuesCall(2, 3, 19)

        EngQuesCall(1, 3, 12)
        EngQuesCall(2, 2, 2)
        EngQuesCall(2, 3, 5)

        print('DataToShow1')
        print(len(DataToShow1))
        print('DataToShow2')
        print(len(DataToShow2))

    elif glevel == 5:
        pass
    else:
        pass


def PhyQuesCall(mark, level, num):
    global DataToShow1, DataToShow2
    m = int(mark)
    l = int(level)
    nn = int(num)
    phyData = PhysicsQues.objects.all()
    phymkl = []
    patternMkL = f'^Pmk{m}le{l}v[0-9]+$'

    for x in phyData:
        if re.match(patternMkL, x.physicsModel):
            phymkl.append(x)

    cp1 = len(phymkl)

    if m == 1:
        for i in range(nn):
            n = random.randrange(cp1)
            y = phymkl[n]
            DataToShow1.append(y)
    elif m == 2:
        for i in range(nn):
            n = random.randrange(cp1)
            y = phymkl[n]
            DataToShow2.append(y)


def CheQuesCall(mark, level, num):
    global DataToShow1, DataToShow2
    m = int(mark)
    l = int(level)
    nn = int(num)
    cheData = ChemistryQues.objects.all()
    chemkl = []
    DataToShow = []
    patternMkL = f'^Cmk{m}le{l}v[0-9]+$'

    for x in cheData:
        if re.match(patternMkL, x.chemistryModel):
            chemkl.append(x)

    cp1 = len(chemkl)

    if m == 1:
        for i in range(nn):
            n = random.randrange(cp1)
            y = chemkl[n]
            DataToShow1.append(y)
    elif m == 2:
        for i in range(nn):
            n = random.randrange(cp1)
            y = chemkl[n]
            DataToShow2.append(y)


def MathQuesCall(mark, level, num):
    global DataToShow1, DataToShow2
    m = int(mark)
    l = int(level)
    nn = int(num)
    mathData = MathQues.objects.all()
    mathmkl = []
    DataToShow = []
    patternMkL = f'^Mmk{m}le{l}v[0-9]+$'

    for x in mathData:
        if re.match(patternMkL, x.mathModel):
            mathmkl.append(x)

    cp1 = len(mathmkl)

    if m == 1:
        for i in range(nn):
            n = random.randrange(cp1)
            y = mathmkl[n]
            DataToShow1.append(y)
    elif m == 2:
        for i in range(nn):
            n = random.randrange(cp1)
            y = mathmkl[n]
            DataToShow2.append(y)


def EngQuesCall(mark, level, num):
    global DataToShow1, DataToShow2
    m = int(mark)
    l = int(level)
    nn = int(num)
    engData = EnglishQues.objects.all()
    engmkl = []
    DataToShow = []
    patternMkL = f'^Emk{m}le{l}v[0-9]+$'

    for x in engData:
        if re.match(patternMkL, x.englishModel):
            engmkl.append(x)

    cp1 = len(engmkl)

    if m == 1:
        for i in range(nn):
            n = random.randrange(cp1)
            y = engmkl[n]
            DataToShow1.append(y)
    elif m == 2:
        for i in range(nn):
            n = random.randrange(cp1)
            y = engmkl[n]
            DataToShow2.append(y)


def levelUpDecide(UserId, levelId):
    data = levelUpDec.objects.all()
    count = 0
    for i in data:
        #print('1')
        if i.User == UserId:
            #print('2')
            print(f'i.level : '+ str(i.level))
            print(f'levelId : '+ str(levelId))
            if int(i.level) == int(levelId):
                #print('3')
                if int(i.percentage) >= 80:
                    print('I am in')
                    count = count + 1
                    print(f'count : ' + str(count))
    if count >= 5:
        print('Ready to Level Up to ')
        print(int(levelId)+1)
        data1 = levelUpDec.objects.filter(User=UserId, level=levelId)
        data1.delete()
        levelId = int(levelId)+1
        UserDetail.objects.filter(user=UserId).update(glevel=levelId)



    else:
        print(f'You are not ready. '+ str(levelId))



def reCalculate(mark, time):
    nTime = round(time)
    if mark == 2:
        if nTime > 2:
            return 3
        elif nTime > 1:
            return 2
        else:
            return 1
    else:
        if time > 1:
            return 3
        elif nTime > 0.5:
            return 2
        else:
            return 1


def reLeveling(mySub, id, level):
    AllQues.objects.filter(pk=id).update(level=level)
    if mySub == 'P':
        PhysicsQues.objects.filter(intQuesID=id).update(level=level)
    elif mySub == 'C':
        ChemistryQues.objects.filter(intQuesID=id).update(level=level)
    elif mySub == 'M':
        MathQues.objects.filter(intQuesID=id).update(level=level)
    elif mySub == 'E':
        EnglishQues.objects.filter(intQuesID=id).update(level=level)



