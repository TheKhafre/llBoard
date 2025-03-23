from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm, EntryForm

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

def new_entry(request, topic_id):
    # create entries for topic
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # that means no data was entered; create new form
        form = EntryForm()
    else:
        # data was submitted and needs to be processed
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
        
    # display a blank form for any other exception
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)