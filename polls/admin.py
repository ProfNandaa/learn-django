from django.contrib import admin

# Register your models here.

from .models import Question, Choice

#StackedInline or TabularIniline
class ChoiceInline(admin.TabularInline):
	model = Choice

class QuestionAdmin(admin.ModelAdmin):
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question_text']
	fields = ['pub_date', 'question_text']
	inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)