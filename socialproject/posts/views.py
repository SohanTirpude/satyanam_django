from django.shortcuts import render
from .forms import PostCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostCreationForm(data = request.POST)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
    else:
        form = PostCreationForm(data = request.GET)
    return render(request, 'posts/create.html',{'form':form})
             
        