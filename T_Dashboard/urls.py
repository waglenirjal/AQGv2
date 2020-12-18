from django.contrib import admin
from django.urls import path
from T_Dashboard import views

urlpatterns = [
    path('', views.dashboardTView, name='teacherDashboardView'),
    path('selsub/', views.selsub, name='addQuestion'),
    path('selsub/M/', views.mathSel, name='addMathQuestion'),
    path('selsub/P/', views.physicsSel, name='addPhysicsQuestion'),
    path('selsub/C/', views.chemistrySel, name='addChemistryQuestion'),
    path('selsub/E/', views.englishSel, name='addEnglishQuestion'),
    path('selsubReview/', views.selsubforReview, name='selectSubjectReview'),
    path('selsubReview/P/', views.allMyPhysics, name='myPhysicsReview'),
    path('selsubReview/C/', views.allMyChemistry, name='myChemistryReview'),
    path('selsubReview/E/', views.allMyEnglish, name='myEnglishReview'),
    path('selsubReview/M/', views.allMyMath, name='myMathReview'),
    path('selsubReview/A/', views.allQues, name='allQuesReview'),
    path('selsubReview/O/', views.allMyQues, name='myQuesReview'),
    path('editSelected/<int:id>', views.editQues, name='EditMyQues'),
    path('deleteSelected/<int:id>', views.deleteQues, name='DeleteMyQues'),
    path('testLoadCache/', views.testLoadCache, name='testLoadCache'),
    path('testWriteCache/', views.testWriteCache, name='testWriteCache'),
]
