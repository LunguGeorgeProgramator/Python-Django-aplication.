from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from guide.database.DataBaseClass import DataBase
from django.views.generic import TemplateView
from guide.forms import IndexFrom


class GuideViews(TemplateView, DataBase):
    template_name = "guide/tasks.html"

    def set_context(self):
        content_text_list = []
        for row in self.get_results_guides():
            content_text_list.append(
                {
                    'id': row[0],
                    'desc': row[1],
                }
            )
        return content_text_list

    def get(self, request):
        name = request.GET.get('name')
        form = IndexFrom()
        context = {
            'content_data': self.set_context(),
            'form': form,
            'name_get_var': name
        }
        return render(request, self.template_name, context)

    def post(self, request):
        text = ''
        id_guide = request.POST.get('id_guide')
        if id_guide:
            self.remove_guide(id_guide)
        insert_guide_form = IndexFrom(request.POST)
        if insert_guide_form.is_valid():
            text = insert_guide_form.cleaned_data['desc']
            self.insert_new_guides(text)
            insert_guide_form = IndexFrom()
            # return redirect(":")
            return HttpResponseRedirect('/GuidedLearningSolution/')
        context = {
            'content_data': self.set_context(),
            'text': text,
            'form': insert_guide_form
        }
        return render(request, self.template_name, context)

    # def post(self, request):
    #     form = IndexFrom(request.POST)
    #     if form.is_valid():
    #         text = form.cleaned_data['id_guide']
    #         form = IndexFrom()
    #         # return redirect(":")
    #         return HttpResponseRedirect('/GuidedLearningSolution/')
    #     context = {
    #         'content_data': self.set_context(),
    #         'text': text,
    #         'form': form
    #     }
    #     return render(request, self.template_name, context)
