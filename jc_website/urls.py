"""jc_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
# from post.views import PostListView, PostDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("home.urls")),
    path("MapPage/",include("map.urls")),
    path("AboutUs/",include("about.urls")),
    path("Contact/",include("contact.urls")),
    path("post/",include("post.urls")),
    path("Service/",include("service.urls"))
    # path('post/', PostListView.as_view()),
    # path('post_<pk>', PostDetailView.as_view())
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
