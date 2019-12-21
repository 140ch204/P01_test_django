from django.urls import path, re_path
from . import views

urlpatterns = [
    # path('accueil', views.home),
    # path('article/<id_article>', views.view_article, name='afficher_article'),
    # path('articles/<str:tag>', views.list_articles_by_tag),
    # path('articles/<int:year>/<int:month>', views.list_articles),
    # path('date', views.date_actuelle),
    # path('addition/<int:nombre1>/<int:nombre2>/', views.addition),
    path('', views.home),
    path('dashboard/', views.dashboard)
    # path('mapage/', views.mapage)
]