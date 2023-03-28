from django.urls import path

# http request (cliente pede)
from recipes.views import contato, home, sobre

# http response (servidor responde)
urlpatterns = [
    path('', home),  # o caminho vazio representa a raiz do site # / home
    path('sobre', sobre),  # / sobre
    path('contato', contato)  # /contato
]
