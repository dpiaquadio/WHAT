from django.forms.formsets import formset_factory

from utility.forms import AutoCompleteField, JqueryDatePicker
from models import Task, TaskProgeny, RandomRecurringTaskGenerator, TaskPrototype
from people.models import GenericParty

from django import forms

from django.db.models import Q

class RandomRecurringTaskGeneratorForm(forms.ModelForm):
    class Meta:
        model = RandomRecurringTaskGenerator

class TaskPrototypeForm(forms.ModelForm):
    name = AutoCompleteField(models = (TaskPrototype,))
    no_generate = forms.BooleanField()
    class Meta:
        model = TaskPrototype

class TaskPrototypeNameForm(forms.ModelForm):
    name = AutoCompleteField(models = (TaskPrototype,), name_visible_field=True)
    class Meta:
        model = TaskPrototype
        fields = ['name']

class RestOfTheTaskPrototypeForm(forms.ModelForm):
    class Meta:
        model = TaskPrototype
        exclude = ['name', 'weight', 'creator']

class TaskForm(forms.ModelForm):
    projected = JqueryDatePicker()
    class Meta:
        model = Task
        exclude = ['owners']


class TaskHierarchyForm(forms.ModelForm):
    class Meta:
        model = TaskProgeny
        
class GenerateTaskForm(forms.ModelForm):
    completed = forms.BooleanField()
    class Meta:
        model = Task
        exclude = ['prototype', 'weight']