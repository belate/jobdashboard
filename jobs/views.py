from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .models import Job
from .forms import JobForm, NoteForm


def index(request):
    jobs = Job.objects.all().order_by('-id')
    if request.is_ajax():
        return render(request, 'jobs/jobs.html', {'jobs': jobs})
    return render(request, 'jobs/index.html', {'jobs': jobs})


@login_required
def add_job(request):
    form = JobForm(request.POST or None)

    if form.is_valid():
        form.save(request.user)
        return redirect(reverse('index'))

    return render(request, 'jobs/add_job.html', {'form': form})


@login_required
def edit_job(request, job_id):
    job = Job.objects.get(id=job_id)

    if job.owner != request.user and not request.user.is_staff:
        return redirect(reverse('index'))

    form = JobForm(request.POST or None, instance=job)
    if form.is_valid():
        form.save()
        return redirect(reverse('index'))

    return render(request, 'jobs/add_job.html', {'form': form})


@login_required
def add_note(request, job_id):
    job = Job.objects.get(id=job_id)
    form = NoteForm(request.POST or None)

    if form.is_valid():
        form.save(request.user, job)
        return redirect(reverse('index'))

    return render(request, 'jobs/add_note.html', {'form': form})
