from django.contrib import admin
from django.urls import path
from Dashboard import views

urlpatterns = [
    path('', views.dashboardView, name='dashboardView'),
    path('qbank', views.qBankView, name='qBankView'),
    path('mocktest', views.mockTestView, name='mockTestView'),
    path('mockinstruct', views.mockTestInstructView, name='mockTestInstructView'),
    path('start', views.perQuestionView, name='perQuestionView'),
    path('saveans', views.saveAns, name='saveAnswer'),
    path('result', views.result, name='resultReport'),
    path('resultCerf', views.CerfResult, name='CerfresultReport'),
    path('dataz', views.dataz, name='dataz'),
    path('savemyans', views.save1ans, name='saveONEans'),
    path('saveQans', views.saveQans, name='saveQans'),
    path('welcomeCF', views.CerfTestWel, name='WelcomeAtCerf'),
    path('cerfTest', views.CerfTest, name='CerfTest'),
    path('blogs', views.blogs, name='Blogs'),
    path('resources', views.resources, name='resources'),
    path('resources/P', views.resPhy, name='resPhy'),
    path('resources/C', views.resChe, name='resChe'),
    path('resources/E', views.resEng, name='resEng'),
    path('resources/M', views.resMath, name='resMath'),
    path('book', views.book, name='BookmarkCache'),
    path('delbook', views.delbook, name='Delete_Bookmark'),
    path('bookmark', views.bookmark, name='Bookmark'),
]
