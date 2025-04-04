from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('new/', ArticleCreateView.as_view(), name='article_create'),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
