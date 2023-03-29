from django.urls import path

# http request (cliente pede)
from recipes.views import home

# http response (servidor responde)
urlpatterns = [
    path('', home),  # o caminho vazio representa a raiz do site # / home

]
