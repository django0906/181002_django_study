from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import Question, Choice


# ListView, DetailView는 제너릭 뷰다.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    # 이것도 제공해주는 함수.
    # 기존 함수에서처럼 일일이 작업할 해줄 필요없이
    # 간단하게 작업이 가능.
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]


# Detail같은 경우에도 존재.
# 필요한 요소들이 알아서 오버라이딩함.
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
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
