from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.CharField(max_length=100, default='AI Automation Team')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='posts')
    excerpt = models.CharField(max_length=300, blank=True)
    content = models.TextField()
    featured_image = models.URLField(blank=True)
    is_published = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    meta_description = models.CharField(max_length=160, blank=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title


class CaseStudy(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    client_name = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    challenge = models.TextField()
    solution = models.TextField()
    results = models.TextField()
    testimonial = models.TextField(blank=True)
    featured_image = models.URLField(blank=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
