from django.shortcuts import render, HttpResponse
from django.utils.timezone import now
from django.contrib import messages
from Dashboard.models import PerQuestionForCertificates
from question.models import AllQues, PhysicsQues, MathQues,EnglishQues,ChemistryQues

# Create your views here.

def mathCount():
    allMathQues = MathQues.objects.all()
    count = allMathQues.count()
    print(count)
    return count+1



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


def expertV1(request):
    print('Expert v1.1')
    data1 = PerQuestionForCertificates.objects.all()
    data2 = AllQues.objects.all()
    for i in data2:
        print('Expert v1.1.data2')
        moreTime = 0
        lessTime = 0
        mtt = 0
        ltt = 0
        timeToSolve = i.timeToSolve
        myMark = int(i.mark)
        myLevel = int(i.level)
        mySub = i.subID
        print(i.pk)
        idi = i.pk
        data3 = data1.filter(IntQuesID=idi)
        data5 = data1.filter(IntQuesID=idi, Solved=True)
        data4 = data1.filter(IntQuesID=idi, Solved=False)
        totalNoData = len(data3)
        print('Total')
        print(totalNoData)
        FalseNoData = len(data4)
        print('False')
        print(FalseNoData)
        if totalNoData and FalseNoData:
            FalsePercent = (FalseNoData/totalNoData)*100
            if FalseNoData > 20 and FalsePercent > 70:
                print('Expert v1.1.False')
                if myLevel == 1:
                    pass
                else:
                    myLevel = myLevel - 1
                    reLeveling(mySub, idi, myLevel)


        for j in data5:
            print('Expert v1.1.data5')
            if j.TimeTaken:
                print('TimeTaken')
                test1 = round(float(j.TimeTaken))
                print(test1)
                print(test1/60)
                print(float(timeToSolve))
                if (test1/60) > float(timeToSolve):
                    moreTime = moreTime + 1
                    mtt = mtt + (test1/60)
                    #PerQuestionForCertificates.objects.filter(IntQuesID=i.IntQuesID).update(TimeTaken=i.TimeTaken)

                elif (test1/60) < float(timeToSolve):
                    lessTime = lessTime + 1
                    ltt = ltt + (test1 / 60)

        AllQues.objects.filter(pk=idi).update(moreTimeTaken= moreTime, lessTimeTaken= lessTime)

        if moreTime > 20:
            print('Expert v1.1.moreTIme')
            percent = round((moreTime/totalNoData)*100)
            if percent > 70:
                avgTime = mtt/moreTime
                newLevel = reCalculate(myMark, avgTime)
                reLeveling(mySub, i.IntQuesID, newLevel)


        if lessTime > 20:
            print('Expert v1.1.lessTime')
            percent = round((lessTime / totalNoData) * 100)
            if percent > 70:
                avgTime = ltt / lessTime
                newLevel = reCalculate(myMark, avgTime)
                reLeveling(mySub, i.IntQuesID, newLevel)

    return HttpResponse('Done')


