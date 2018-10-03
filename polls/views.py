from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Question, Choice


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'detail.html', {'question': question})
    # return HttpResponse("질문 이거했수 %s" % question_id)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'results.html', {'question': question})

    # response = "질문의 답은 이것: %s"
    # return HttpResponse(response % question_id)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # POST 데이터가 올바르게 왔을 때만 redirect를 할 것임
        # 이거는 데이터가 두번 들어가는걸 막아준다.
        # 백버튼 눌른다던가 이런식으로 POST 두번 할 때...
        return HttpResponseRedirect(
            reverse('polls:results', args=(question_id,))
        )

    # return HttpResponse("여기에 투표하셨수: %s" % question_id)
