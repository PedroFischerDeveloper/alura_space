from django.urls import path # type: ignore
from galery.views import index, image


urlpatterns = [
       path('', index),
       path('imagem/', image, name='imagem'),
]
