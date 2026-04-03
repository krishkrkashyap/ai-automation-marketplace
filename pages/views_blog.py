
def blog_list(request):
    from pages.models import Post, Category
    posts = Post.objects.filter(is_published=True)[:10]
    categories = Category.objects.all()
    return render(request, 'pages/blog_list.html', {'posts': posts, 'categories': categories})


def blog_detail(request, slug):
    from pages.models import Post
    try:
        post = Post.objects.get(slug=slug, is_published=True)
    except Post.DoesNotExist:
        raise Http404("Post not found")
    return render(request, 'pages/blog_detail.html', {'post': post})


def blog_category(request, category_slug):
    from pages.models import Post, Category
    try:
        category = Category.objects.get(slug=category_slug)
        posts = Post.objects.filter(category=category, is_published=True)
    except Category.DoesNotExist:
        posts = []
    return render(request, 'pages/blog_category.html', {'posts': posts, 'category': category_slug})


def case_study_detail(request, slug):
    from pages.models import CaseStudy
    try:
        case = CaseStudy.objects.get(slug=slug, is_published=True)
    except CaseStudy.DoesNotExist:
        raise Http404("Case study not found")
    return render(request, 'pages/case_study_detail.html', {'case': case})
