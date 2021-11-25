from django.views.generic import ListView, DetailView, UpdateView, DeleteView  
from .models import Category, Author, Post, PostCategory, Comment
from .filters import PostFilter
from .forms import PostForm

 
class PostList(ListView):
    model = Post
    template_name = 'news.html' 
    context_object_name = 'news' 
    queryset = Post.objects.order_by('-created')
    paginate_by = 1    


class SearchList(ListView):
    model = Post
    template_name = 'search.html' 
    context_object_name = 'search' 
    queryset = Post.objects.order_by('-created')

    def get_context_data(self, **kwargs):  
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


class PostUpdateView(UpdateView):
    template_name = 'edit.html'
    form_class = PostForm
 
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(DeleteView):
    template_name = 'delete.html'
    queryset = Post.objects.all()
    context_object_name = 'news'
    success_url = '/search/' 
 

class AddList(ListView):
    model = Post
    template_name = 'add.html' 
    context_object_name = 'add' 
    queryset = Post.objects.order_by('-created')
    form_class = PostForm

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        context['form'] = PostForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST) 
        if form.is_valid(): 
            form.save() 
        return super().get(request, *args, **kwargs)


class PostDetail(DetailView):
    model = Post
    template_name = 'new.html' 
    context_object_name = 'news'