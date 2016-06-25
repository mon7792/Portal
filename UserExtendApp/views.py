from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required


from .forms import UserForm
from .models import User
# Create your views here.


@login_required
def update_profile(request):
    post = get_object_or_404(User, username= request.user)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            bio = form.cleaned_data['Bio']
            post.Bio = bio
            post.save()
            # reply back a feedback message stating changes are saved
            
            
    else:
        form = UserForm(instance=post)
    
    return render(request, 'UserExtendApp/user_update_form.html', {'form': form})