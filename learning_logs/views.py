from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm

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


def new_topic(request):
    # creating new topic for user
    if request.method != 'POST':
        # i.e no data was submitted, go ahead to create a new one
        form = TopicForm()
    else:
        # if data was submitted, then process it
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
        
    # show an invalid form if any error
    context = {'form':form}
    return render(request, 'learning_logs/new_topic.html', context)