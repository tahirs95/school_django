from django.urls import path
from . import views



app_name = 'classroom'
urlpatterns = [
    
    path(r'view/',views.student_name, name='student_view'),

]
