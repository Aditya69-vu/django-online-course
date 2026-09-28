from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

# Define Choice inline for Question
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2

# Define Question inline for Lesson
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2

# Custom QuestionAdmin to include ChoiceInline
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['question_text', 'grade']

# Custom LessonAdmin to include QuestionInline
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [QuestionInline]

# Register models with admin site
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)