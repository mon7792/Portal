from django.shortcuts import render

# Create your views here.

'''
View to handle homepage
'''
def home_page(request):
    template_name = "home/home.html"
    context= {}
    return render(request, template_name, context)