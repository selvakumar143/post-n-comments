from django.shortcuts import render, redirect
from .forms import PostForm
from django.views.generic import ListView, DetailView
from .models import BlogPost
from comments.models import Comment

def post_form_view(request):
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # Process the form data
            title = form.cleaned_data['title']
            short_description = form.cleaned_data['short_description']
            content = form.cleaned_data['content']
            media = form.cleaned_data['media']
            form = PostForm(request.POST, request.FILES)
            # print(form.cleaned_data) 
            
            if request.method == 'POST':
                form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                instance= form.save(commit=False)
                instance.author_id = 2
                instance.status = "draft"
                # print(form)
                instance.save()
                # return redirect('form_success')
        else:
            form = PostForm()
            
            # Do something with the data, e.g., save it to the database
            
            # return redirect('form_success')
    else:
        form = PostForm()
    form = PostForm()
    return render(request, 'form_template.html', {'form': form})


class post_list_view(ListView):
    model = BlogPost  # Specify the model to display
    template_name = 'list.html'  # Define the template for rendering
    paginate_by = 5  # Set the number of items per page (optional)

    def get_queryset(self):
        # Optionally filter or modify the queryset here
        queryset = super().get_queryset().order_by('id')
        return queryset.filter() 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_pages'] = context # Add context variables
        # context['current_page'] = context # Add context variables
        # print(request.GET.get('variable_name'))
        return context
    
class detail_view(DetailView):
    model = BlogPost  # Specify the model to use
    template_name = 'detail.html'  # Define the template for rendering

    # Optional: Customize the context data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()  # Access the retrieved post object
        # print(post.comment)
        context['comments'] = Comment.objects.filter(post_id = post.id )  # Load all comments
        # Add additional context data here (e.g., related objects)
        return context