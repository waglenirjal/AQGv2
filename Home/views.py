from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required, PermissionDenied
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from question.models import PhysicsQues, AllQues

from aqg.decorators import student_only, role_required
from django.contrib.auth.models import User

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string


# Create your views here.

def handleSHome(request):
    return render(request, 'home/index.html')

def indexView(request):
    return render(request, 'home/index.html')

def csView(request):
    return render(request, 'comingsoon.html')

def handleSLogin(request):
    if request.method == 'POST':
        # get the post parameters
        print('i am here ')
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpass']


        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged In')
            if request.GET.get('next', None):
                return HttpResponseRedirect(request.GET['next'])
            return redirect('indexView')
        else:
            messages.error(request, 'Invalid: try again')
            return redirect('indexView')

    return render(request, 'login/login.html')

@login_required
# role_required(allowed_roles=['Teacher'])
@student_only
def handleSLogout(request):
    logout(request)
    messages.success(request, 'Success: Log Out')
    return redirect('indexView')


def loadLive(request):
    global intCosData
    intCosData = 0
    return render(request, 'test/testLive.html')

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


    print('------------------------------')
    # txt1 = 'What is your name?'
    # data = cosineSim(txt1, data1)
    #return JsonResponse({'lol': '404'})
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

