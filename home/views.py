from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Category, Comment
from .forms import AddPostForm, EditPostForm, AddCategoryForm, CommentForm
from django.urls import reverse_lazy


# class HomeView(ListView):
#     model = Post
#     template_name = 'home.html'
#     ordering = ['-date_published']
#     # ordering = ['-id']
#     extra_context = {'categories': Category.objects.all()}


# def CategoryView(request, category):
#     category_posts = Post.objects.filter(category=category.replace('-', ' '))
#     categories = Category.objects.all()
#     return render(request, 'category.html', {'category': category.replace('-', ' ').title(), 'category_posts': category_posts, 'categories': categories })


# class PostDetailView(DetailView):
#     model = Post
#     template_name = 'post-detail.html'
#     extra_context = {'categories': Category.objects.all(), 'next_post': None, 'previous_post': None}

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         comments = Comment.objects.filter(post=self.get_object()).order_by('-date_added')
#         context['comments'] = comments
#         if self.request.user.is_authenticated:
#             context['comment_form'] = CommentForm(instance=self.request.user)

#         return context
    
#     def post(self, request, *args, **kwargs):
#         new_comment = Comment(content=request.POST.get('content'), author=self.request.user, post=self.get_object())
#         new_comment.save()
#         return self.get(self, request, *args, **kwargs)


# class AddPostView(LoginRequiredMixin, CreateView):
#     model = Post
#     form_class = AddPostForm
#     template_name = 'add-post.html'
#     extra_context = {'categories': Category.objects.all()}


# class AddCategoryView(LoginRequiredMixin, CreateView):
#     model = Category
#     form_class = AddCategoryForm
#     template_name = 'add-category.html'
#     extra_context = {'categories': Category.objects.all()}


# class UpdatePostView(LoginRequiredMixin, UpdateView):
#     model = Post
#     template_name = 'edit-post.html'
#     form_class = EditPostForm
#     extra_context = {'categories': Category.objects.all()}

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         user = self.request.user
#         context['isUserAuthorised'] = user.id == context['post'].author.id
#         return context


# class DeletePostView(LoginRequiredMixin, DeleteView):
#     model = Post
#     template_name = 'delete-post.html'
#     success_url = reverse_lazy('home')
#     extra_context = {'categories': Category.objects.all()}

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         user = self.request.user
#         context['isUserAuthorised'] = user.id == context['post'].author.id
#         return context
