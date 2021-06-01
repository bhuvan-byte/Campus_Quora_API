from django.urls import path
from .views import *
urlpatterns = [
    path('question',Question.as_view(),name="question"),

]
