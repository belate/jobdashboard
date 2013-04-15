from django.forms import ModelForm, Textarea
from .models import Job, Note


class JobForm(ModelForm):

    class Meta:
        model = Job
        exclude = ('owner',)

    def save(self, owner=None, *args, **kwargs):
        job = super(JobForm, self).save(commit=False, *args, **kwargs)

        # Only set the owner if this is an edit
        if not job.id:
            job.owner = owner
        job.save()

        return job


class NoteForm(ModelForm):

    class Meta:
        model = Note
        exclude = ('owner', 'job')
        widgets = {
            'text': Textarea(attrs={'cols': 100, 'rows': 3}),
        }

    def save(self, owner=None, job=None, *args, **kwargs):
        note = super(NoteForm, self).save(commit=False, *args, **kwargs)

        # Only set the owner if this is an edit
        if not note.id:
            note.owner = owner
            note.job = job
        note.save()

        return note
