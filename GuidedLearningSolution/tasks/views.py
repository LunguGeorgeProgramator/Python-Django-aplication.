from django.shortcuts import render
from django.http import HttpResponse


content_text_list = [
    {
        'titlu': 'Merge 1',
        'desc': 'Merge 2',
    },
    {
        'titlu': 'Merge 4',
        'desc': 'Merge 5',
    }
]


def home(request):
    context = {
        'content_data': content_text_list,
        'title_page': 'Tasks'
    }
    return render(request, 'tasks/tasks.html', context)


def details(request):
    return HttpResponse("<p>User details page.</p>")

