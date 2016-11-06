from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.template import RequestContext
from tasks.forms import RegistrationForm, TaskForm
from django.contrib.auth.decorators import login_required
from tasks.models import Task, User


@login_required(login_url='/login/')
def main_page(request):
    tasks = Task.objects.filter(user_id=request.user)
    return render_to_response(
        'main_page.html', RequestContext(request, {'tasklist':  tasks})
    )


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
        'form': form
    })
    return render_to_response(
        'registration/register.html', variables
    )


@login_required(login_url='/login/')
def task_list(request, template_name='tasks/task_list.html'):
    tasks = Task.objects.filter(user_id=request.user)
    return render(request, template_name, {'user': request.user, 'tasks': tasks})


@login_required(login_url='/login/')
def task_update(request, pk, template_name='tasks/task_form.html'):
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    return render(request, template_name, {'form': form})


@login_required(login_url='/login/')
def task_create(request, template_name='tasks/task_form.html'):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        task, dummy = Task.objects.get_or_create(
            title=form.cleaned_data['title'],
            priority=form.cleaned_data['priority'],
            user=request.user
        )
        task.save()
        return HttpResponseRedirect('/')
    return render(request, template_name, {'form': form})


@login_required
def task_delete(request, pk, template_name='tasks/task_confirm_delete.html'):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return HttpResponseRedirect('/')
    return render(request, template_name, {'task':task})