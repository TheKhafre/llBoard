from django.shortcuts import render

# Create your views here.
def index(request):
    """Learning Logs Homepage route"""
    return render(request,'learning_logs/index.html')
