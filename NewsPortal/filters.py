from django_filters import FilterSet, DateRangeFilter
from .models import Category, Author, Post, PostCategory, Comment


class PostFilter(FilterSet):
    created = DateRangeFilter()
    class Meta:
        model = Post
        fields = ('author', 'created', 'cats', 'post_type')