from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from polls.models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]

    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    return render(request, 'detail.html', {'question': question})
    # return HttpResponse("질문 이거했수 %s" % question_id)


def results(request, question_id):
    response = "질문의 답은 이것: %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("여기에 투표하셨수: %s" % question_id)
