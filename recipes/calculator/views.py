from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def get_dish(request, recipe):
    servings = int(request.GET.get('servings', 1))
    ingredients = {}
    name = ''
    if recipe in DATA:
        ingredients = {k: (v * servings) for k, v in DATA[recipe].items()}
        name = recipe
    context = {'recipe': ingredients,
               'name': name}
    return render(request, 'calculator/index.html', context)
