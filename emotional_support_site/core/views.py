from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CrisisHotline, SelfAssessment
from .forms import SelfAssessmentForm
def home(request):
    crisis_hotlines = CrisisHotline.objects.filter(is_active=True)[:6]
    context = {
        'crisis_hotlines': crisis_hotlines,
    }
    return render(request, '../emotional_support_site/templates/base.html', context)
def crisis_help(request):
    hotlines = CrisisHotline.objects.filter(is_active=True)
    context = {
        'hotlines': hotlines,
    }
    return render(request, 'core/crisis_help.html', context)
def self_assessment(request):
    if request.method == 'POST':
        form = SelfAssessmentForm(request.POST)
        if form.is_valid():
            assessment = form.save(commit=False)
            if request.user.is_authenticated:
                assessment.user = request.user
            assessment.save()
            messages.success(request, 'Assessment completed. Thank you for sharing.')
            return redirect('core:home')
    else:
        form = SelfAssessmentForm()
    return render(request, 'core/self_assessment.html', {'form': form})