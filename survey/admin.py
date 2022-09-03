from django.contrib import admin
import nested_admin
from .models import Survey, Question, Choice, YesNoChoices


class ChoiceInLine(nested_admin.NestedTabularInline):
    """Class to create inline choice nestings for Question objects
    Nested Choices are collapsed by default
    """
    model = Choice
    classes = ['collapse']


class ChoicesInLine2(nested_admin.NestedTabularInline): 
    model = YesNoChoices
    extra = 2
    classes = ['collapse']




class QuestionInLine(nested_admin.NestedTabularInline):
    """Class to create inline choice nestings for Survey objects
        Nested Questions are collapsed by default
        """
    model = Question
    extra = 1
    classes = ['collapse']
    inlines = [ChoiceInLine, ChoicesInLine2]


class SurveyAdmin(nested_admin.NestedModelAdmin):
    """Class to create model admin mapping for Survey objects
        Here the form fields can be specified using fieldsets attribute.
        published_on attribute form for Survey objects are collapsed by default.
        """
    fieldsets = [
        ('Survey Name', {'fields': ['name']}),
        ('When would you like to publish it?', {'fields': ['published_on'], 'classes': ['collapse']})
    ]
    inlines = [QuestionInLine]

    search_fields = ['name']


admin.site.register(Survey, SurveyAdmin)
