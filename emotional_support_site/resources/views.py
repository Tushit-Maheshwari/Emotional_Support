from django.shortcuts import render, get_object_or_404
from .models import CopingStrategy, BreathingExercise
def coping_strategies(request):
    category = request.GET.get('category', 'all')
    if category == 'all':
        strategies = CopingStrategy.objects.all()
    else:
        strategies = CopingStrategy.objects.filter(category=category)
    categories = CopingStrategy.CATEGORY_CHOICES
    context = {
        'strategies': strategies,
        'categories': categories,
        'current_category': category,
    }
    return render(request, 'resources/coping_strategies.html', context)
def strategy_detail(request, strategy_id):
    strategy = get_object_or_404(CopingStrategy, id=strategy_id)
    return render(request, 'resources/strategy_detail.html', {'strategy': strategy})
def breathing_exercises(request):
    exercises = BreathingExercise.objects.all()
    return render(request, 'resources/breathing_exercises.html', {'exercises': exercises})