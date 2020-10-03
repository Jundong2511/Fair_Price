from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,

)
from django.conf import settings
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'home/main.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    # to show post from newer to older, if wanna show older to newer, use['date_posted']
    ordering= ['-date_posted']
    paginate_by = 5 # every page show only 2 post

class UserPostListView(ListView):
    model = Post
    template_name = 'home/user_post.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    # django premade fuction name.
    def get_queryset(self):
        #
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return  Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post

# LoginRequiredMixin is a requirement for the user who's trying to use the function,
# it verify the user if is login first, if not, send them to lgoin page.
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
        # this function is for when submit the form, set the instance's author
        # to the user who send the request (current login user).
    def form_valid(self, form):
        form.instance.author = self.request.user
        # super means run the follow function with the parent class
        # which is form_valid right here.
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # get the user's object(it means everythins in user, such as title, content, date and
    # author. then post.author means object's author.), and see the post's author is
    # the user who send the reuqest or not, return True if yes.
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False # return page 403

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False




def about(request):
    return render(request, 'home/main.html', {'title': 'About'})
