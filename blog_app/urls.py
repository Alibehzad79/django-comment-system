from django.urls import path
from blog_app.views import article_list_view, article_detail_view

urlpatterns = [
    path('', article_list_view, name="article_list"),
    path("<int:pk>/", article_detail_view, name="article_detail"),

]