from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
import datetime
from django.views import generic
from .models import Choice, Question
#urls.py will tell different web addresses to render different html templates.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        #return the last five published questions
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)  #Checks to see if an object exists. If so, return the matching lookup parameters.
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice']) #selected_choice checks if the previously referred to object has the choice you're
                                                                             #looking for. Request.post lets you access submitted data by keyname.

    except (KeyError, Choice.DoesNotExist):                                  #Catch the exception that the KeyError doesnt exist.
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,))) #HttpResponseRedirect should always be used after incrementing data.
                                #The reverse function will look for the function which has the name attribute results in polls urls.py

'''
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #utput = ', '.join([q.question_text for q in latest_question_list])
    #return HttpResponse("Hello, world. You're at the polls index.")  # ex: /polls/

    context = {'latest_question_list':latest_question_list}
    #return HttpResponse(output)
    return render(request, 'polls/index.html', context)   #The render method takes an object as the first parameter

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request,'polls/results.html', {'question': question})
                                                        #Ex polls/5/results
                                                         #The HTML to be rendered as the second parameter, and a dictionary as the third

def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/detail.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)  #Checks to see if an object exists. If so, return the matching lookup parameters.
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice']) #selected_choice checks if the previously referred to object has the choice you're
                                                                             #looking for. Request.post lets you access submitted data by keyname.

    except (KeyError, Choice.DoesNotExist):                                  #Catch the exception that the KeyError doesnt exist.
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,))) #HttpResponseRedirect should always be used after incrementing data.
                                #The reverse function will look for the function which has the name attribute results in polls urls.py
'''
