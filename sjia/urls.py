from django.urls import path, include
import sjia.views

urlpatterns = [
    path('', sjia.views.index),
    path('index', sjia.views.index),
    path('results', sjia.views.results_log),
    path('chart', sjia.views.chart)
]
