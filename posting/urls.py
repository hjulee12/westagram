from django.urls import path
from .views      import PostingView, PostingdetailView, PostinglistView

urlpatterns = [
    path('/post', PostingView.as_view()),
    path('/post/<int:post_id>', PostingdetailView.as_view()),
    path('/postings', PostinglistView.as_view()),
]
