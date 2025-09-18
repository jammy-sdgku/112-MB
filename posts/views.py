from django.urls import reverse_lazy
from django.views.generic import (ListView , DetailView, CreateView, DeleteView, UpdateView)
from .models import Post
from django.contrib.auth.models import User

#CRUD - Create, Read, Update, Delete
#the generic classes are ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
#ListView - to show a list of items
class PostListView(ListView): #inheritance
    #template_name attribute is goigng to tell django which template to use.
    model = Post
    template_name = 'posts/list.html'
    #model attribute is going to tell django which model/database to use
    model = Post
    #or we can use queryset attribute to tell django which data to use from the model/database.
    #context_object_name attribute is going to tell django what variable name to use in the template. Only applies to ListView and DetailView. 
    #Context is a python dictionary that is passed to the template. This is how we pass data from the view to the template.
    #by default the context variable name is object or object_list for ListView and object for DetailView.
    context_object_name = 'post_list'
    paginate_by = 10
    #queryset attribute is going to tell django which data to use from the model/database.
    #by default it is going to use all the data from the model/database.
    #we can use queryset to filter the data.
    #queryset = Post.objects.filter(author='admin') #filtering the data to show only posts by author 'admin'
   
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/detail.html'
    context_object_name = 'single_post' 
    
class PostCreateView(CreateView):
    template_name = 'posts/new.html'  
    model = Post
    fields = ['title', 'subtitle', 'body']
    
    def form_valid(self, form):
        print(form)
        print(User.objects.all())
        form.instance.author = User.objects.filter(is_superuser=True).first()
        return super().form_valid(form)
    
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/delete.html'
    success_url = reverse_lazy('posts')
    
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'posts/edit.html'
    fields = ['title', 'subtitle', 'body']
    