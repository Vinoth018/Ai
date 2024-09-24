from django.urls import path
from myapp import views
urlpatterns = [
    path('language/', views.language_translation ),
    path('products/', views.products ),
    path('subtitles/', views.subtitles )
]
