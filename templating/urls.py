from django.urls import path
from templating.views import contacts_page, increase_views, BlogListView, BlogCreateView, HomeListView, BlogUpdateView, BlogDeleteView, BlogDetailView
from templating.apps import TemplatingConfig

app_name = TemplatingConfig.name

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('contacts/', contacts_page, name='contacts'),

    path('blog/', BlogListView.as_view(), name='blog'),
    path('blog_create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog_update/<int:pk>/<slug>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog_delete/<int:pk>/<slug>/', BlogDeleteView.as_view(), name='blog_delete'),
    path('blog_detail/<int:pk>/<slug>/', BlogDetailView.as_view(), name='blog_detail'),
    path('inc_views/<int:pk>/<slug>/', increase_views, name='inc_views')
]