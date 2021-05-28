from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils.text import slugify

CATEGORY_CHOICES = (
    ('Searching', 'Searching'),
    ('Sorting', 'Sorting'),
    ('Recursion', 'Recursion'),
    ('Backtracking', 'Backtracking'),
    ('Maths', 'Maths'),
    ('Bit Manipulation', 'Bit Manipulation'),
    ('Greedy', 'Greedy'),
    ('Dynamic Programming', 'Dynamic Programming'),
    ('Graphs', 'Graphs'),
    ('Others', 'Others')
)


class Post(models.Model):
    title = models.CharField(max_length=50, unique=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=25, default='Others')
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    explain = RichTextField(blank=True, null=True)
    adv = RichTextField(blank=True, null=True)
    disadv = RichTextField(blank=True, null=True)
    similar = RichTextField(blank=True, null=True)
    admin_approval = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images', blank=True)

    # status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
