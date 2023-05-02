from django.urls import path

# http request (cliente pede)
from . import views

# http response (servidor responde)
urlpatterns = [
    path('', views.home),  # o caminho vazio representa a raiz do site # / home
    path('recipes/<id>/', views.recipe)
    # <id> isto e o id passado na url que será enviado para a view
]
