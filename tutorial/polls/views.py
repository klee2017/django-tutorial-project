from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError

from polls.models import Question, Choice


def index(request):
    questions = Question.objects.all()
    context = {
        'questions': questions,
    }
    return render(request, 'polls/index.html', context)


def question_detail(request, pk):
    context = {
        'question': Question.objects.get(pk=pk)
    }
    return render(request, 'polls/question.html', context)


def vote(request, pk):
    if request.method == 'POST':
        # 누군가 form의 action에 있는 question_pk 값을 변형해서 보냈을 경우 발생 가능
        try:
            question = Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            return redirect('index')

        try:
            # 누군가 input의 value에 있는 choice_pk 값을 변형해서 보냈을 경우
            # Choice.DoesNotExist발생 가능
            choice_pk = request.POST['choice_pk']
            choice = Choice.objects.get(pk=choice_pk)
            choice.votes += 1
            choice.save()
        except MultiValueDictKeyError:
            pass
        except Choice.DoesNotExist:
            pass
        finally:
            return redirect('question_detail', pk=question.pk)
    return HttpResponse('Permission denied', status=403)