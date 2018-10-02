from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # name=detail을 한 이유는 템플릿 수정에서 polls:detail이 가능하기 때문.
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]