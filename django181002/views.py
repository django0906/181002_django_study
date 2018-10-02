from django.shortcuts import redirect


def index(request):
    '''
    polls로 리디렉션
    :param request:
    :return:
    '''
    return redirect('/polls/')