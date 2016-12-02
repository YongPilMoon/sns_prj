from django.conf.urls import url
from .views import PostListView,PostDetailView,PostCreateView

urlpatterns = [
    url(r'list/$', PostListView.as_view(), name='post_list'),
    url(r'add/$',PostCreateView.as_view(),name='post_create'),
    url(r'(?P<pk>\d+)/$',PostDetailView.as_view(),name='post_detail'),
]