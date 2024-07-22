from django.db import models
from django.contrib.auth.models import User
from slugify import slugify

# Creating Post model here.
class BlogPost(models.Model):
    # Title of the blog post, limited to 255 characters
    title = models.CharField(max_length=255)
    
    # Short description of the blog post
    short_description = models.TextField()
    
    # Unique slug for the blog post, automatically generated
    slug = models.SlugField(unique=True,blank=True)  
    
    # Content of the blog post
    content = models.TextField()
    
    # Author of the blog post, linked to the User model
    author = models.ForeignKey(User, on_delete=models.CASCADE)  
    
    # Status of the blog post, either 'draft' or 'published'
    status = models.CharField(max_length=20, choices=(('draft', 'Draft'), ('published', 'Published')))  
    
    # Optional media field for the blog post
    media = models.ImageField(upload_to='media/', blank=True, null=True)  

    # String representation of the blog post, returns the title
    def __str__(self):
        return self.title

    # Override the save method to generate a unique slug if it doesn't exist
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.unique_slug_generator()  # Function to generate unique slugs
        super().save(*args, **kwargs)

    # Function to generate a unique slug for the blog post
    def unique_slug_generator(self):
        # Generate slug from lowercase title
        slug = slugify(self.title.lower())  
        
        # Check if a blog post with the same slug already exists
        qs_exists = BlogPost.objects.filter(slug=slug)
        
        # If a blog post with the same slug exists, add a count to the end of the slug
        if qs_exists:
            count = 1
            while qs_exists.filter(slug=slug + '-' + str(count)).exists():
                count += 1
            slug = slug + '-' + str(count)
        
        # Truncate the slug if it's longer than 30 characters
        return slug[:30]  