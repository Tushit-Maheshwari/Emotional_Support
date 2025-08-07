from django import forms
from .models import SelfAssessment
class SelfAssessmentForm(forms.ModelForm):
    class Meta:
        model = SelfAssessment
        fields = ['mood_score', 'anxiety_level', 'notes']
        widgets = {
            'mood_score': forms.Select(attrs={'class': 'form-select'}),
            'anxiety_level': forms.Select(attrs={'class': 'form-select'}),
            'notes': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 4,
                'placeholder': 'Share anything that might help us understand how you feel'
            }),
        }