from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from guide.database.DataBaseClass import DataBase
from django.views.generic import TemplateView
from guide.forms import IndexFrom, DetailsFrom


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


class GuideDetails(TemplateView, DataBase):
    template_name = "guide/details.html"

    def set_context(self, id_guide):
        content_text_list = []
        for row in self.get_results_guide_steps(id_guide):
            content_text_list.append(
                {
                    'id_step': row[0],
                    'id': row[1],
                    'step_content': row[2],
                    'step_selector': row[3],
                    'step_next': row[4],
                    'id_guide': row[5],
                }
            )
        return content_text_list

    def create_guide_steps(self, insert_guide_steps, id_guide):
        id = insert_guide_steps.cleaned_data['id']
        step_content = insert_guide_steps.cleaned_data['step_content']
        step_selector = insert_guide_steps.cleaned_data['step_selector']
        step_next = insert_guide_steps.cleaned_data['step_next']
        self.insert_new_guide_step(id, step_content, step_selector, step_next, id_guide)

    def modify_guide_steps(self, insert_guide_steps):
        id = insert_guide_steps.get('id')
        step_content = insert_guide_steps.get('step_content')
        step_selector = insert_guide_steps.get('step_selector')
        step_next = insert_guide_steps.get('step_next')
        id_step = insert_guide_steps.get('id_step_update', 0)
        self.update_guide_step(id, step_content, step_selector, step_next, id_step)

    def get(self, request):
        id_guide = request.GET.get('id_guide')
        form = DetailsFrom()
        context = {
            'content_data': self.set_context(id_guide),
            'form': form,
            "guide_id": id_guide
        }
        return render(request, self.template_name, context)

    def post(self, request):
        id_guide = request.GET.get('id_guide')
        self.remove_guid_step(request.POST.get('id_step', 0))
        trigger_update = request.POST.get('id_step_update')
        if trigger_update:
            self.modify_guide_steps(request.POST)
            return HttpResponseRedirect('/GuidedLearningSolution/details?id_guide=' + str(id_guide))
        inset_guide_steps = DetailsFrom(request.POST)
        if not trigger_update and inset_guide_steps.is_valid():
            self.create_guide_steps(inset_guide_steps, id_guide)
            update_guide_steps = DetailsFrom()
            return HttpResponseRedirect('/GuidedLearningSolution/details?id_guide='+str(id_guide))
        context = {
            'content_data': self.set_context(id_guide),
            'form': inset_guide_steps
        }
        return render(request, self.template_name, context)