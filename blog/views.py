from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import EmailPostForm
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.views.generic import ListView
# Create your views here.
class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'

# def post_list(request):
#     obj_list = Post.published.all()
#     paginator = Paginator(obj_list,3)
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)

#     return render(
#         request,
#         'blog/post/list.html',
#         {
#             'posts': posts,
#         }
#     )

def post_detail(request,year,month,day,post):
    post = get_object_or_404(Post, slug=post,status='published',
                            publish__year=year,
                            publish__month=month,
                            publish__day = day)
    
    return render(
        request,
        'blog/post/detail.html',
        {'post': post}
    )


def post_share(request):
    post = get_object_or_404(Post,id=post_id,status='published')
    if request.method == 'POST':
        # 初始化表单
        form = EmailPostForm(request.POST)
        # 表单验证
        if form.is_valid():
            sendEmail()
        else:
            form = EmailPostForm()
        
        return render(request,'blog/post/share.html',{
            'post':post,
            'form':form
        })

    
