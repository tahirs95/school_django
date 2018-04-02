from django.shortcuts import render
from .models import Student


def student_name(request):
    
	template_name = 'student_names.html'
	queryset = Student.objects.all()
	context = { 'names_list' : queryset}
	return render(request, template_name, context)
