from django.db import models
from django_prose_editor.fields import ProseEditorField
from prose.fields import RichTextField

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    
    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return '/%s/' % self.slug
    

class Post(models.Model):
    ACTIVE = 'active'
    DRAFT = 'draft'
    
    CHOICE_STATUS = (
        (ACTIVE, 'Active'),
        (DRAFT, 'Draft')
    )
    
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=CHOICE_STATUS, default=ACTIVE)
    
    class Meta:
        ordering = ('-created_at',)
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return '/%s/%s' %(self.category.slug, self.slug)
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments',on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name