from django.contrib import admin
from .models import CrisisHotline, SelfAssessment

@admin.register(CrisisHotline)
class CrisisHotlineAdmin(admin.ModelAdmin):
    list_display = ['country', 'number', 'description', 'is_active']
    list_filter = ['is_active', 'country']
    search_fields = ['country', 'number', 'description']

@admin.register(SelfAssessment)
class SelfAssessmentAdmin(admin.ModelAdmin):
    list_display = ['user', 'assessment_date', 'mood_score', 'anxiety_level']
    list_filter = ['assessment_date', 'mood_score', 'anxiety_level']
    readonly_fields = ['assessment_date']
