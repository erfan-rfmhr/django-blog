from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .forms import PostForm
from .models import Post


class PostListView(generic.ListView):
    template_name = 'blog\home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(status='pub').order_by('-date_modified')


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog\post_detail.html'
    # context_object_name = 'post'


# def post_create_view(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(to='posts_list')
#
#     new_form = PostForm()
#     return render(request, 'blog\create_post.html', context={'form': new_form})


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = PostForm
    template_name = 'blog\create_post.html'


# def post_update_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     form = PostForm(request.POST or None, instance=post)
#     if form.is_valid():
#         form.save()
#         return redirect(to='post_detail', pk=pk)
#     return render(request, 'blog\create_post.html', context={'form': form})

class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog\create_post.html'

#
#
# def post_delete_view(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == 'POST':
#         post.delete()
#         return redirect('posts_list')
#     return render(request, 'blog\delete_post.html', context={'post': post})


class PostDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Post
    template_name = 'blog\delete_post.html'
    success_url = reverse_lazy('posts_list')
