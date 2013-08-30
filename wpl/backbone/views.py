from django.shortcuts import render

def todo(request):
	return render(request, 'backbone/todo.html')
