"""untirta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from faper.views import prodiFaper
from feb.views import prodiFEB
from fh.views import prodiFH
from fisip.views import prodiFisip
from fk.views import prodiFK
from fkip.views import prodiFKIP
from ft.views import prodiFT
from pascasarjana.views import prodiPC

urlpatterns = [
    path('admin/', admin.site.urls),
    path('faper/', prodiFaper),
    path('feb/', prodiFEB),
    path('fh/', prodiFH),
    path('fisip/', prodiFisip),
    path('fk/', prodiFK),
    path('fkip/', prodiFKIP),
    path('ft/', prodiFT),
    path('pascasarjana/', prodiPC),

]
