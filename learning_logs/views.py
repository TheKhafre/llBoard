from django.shortcuts import render
from .models import Topic

# Create your views here.
def index(request):
    """Learning Logs Homepage route"""
    return render(request,'learning_logs/index.html')

def topics(request):
    """Topics page route"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """ defining view for individual topic and entries """
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}

    return render(request, 'learning_logs/topic.html', context)
