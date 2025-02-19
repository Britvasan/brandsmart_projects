from django.urls import path
from . import views

app_name = 'card_app'

urlpatterns = [
    path('',views.index, name='index'),
    path('news_form/', views.news_form, name='news_form'),
    path('news_activities/',views.news_activities, name='news_activities'),
    path('magazine_form/', views.magazine_form, name='magazine_form'),
    path('magazine_activities/', views.magazine_activities, name='magazine_activities'),
    path('social_form/', views.social_form, name='social_form'),
    path('social_activities/', views.social_activities, name='social_activities'),
    path('slides_form/', views.slides_form, name='slides_form'),
    path('slides_activities/', views.slides_activities, name='slides_activities'),
    path('others_form/', views.others_form, name='others_form'),
    path('others_activities/', views.others_activities, name='others_activities'),
    path('update_task/<int:task_id>/<str:task_type>/', views.update_task, name='update_task'),
    path('all_activities/', views.all_activities, name='all_activities')
]