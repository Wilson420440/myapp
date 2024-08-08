from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.views.generic import ListView, DetailView,TemplateView
from .models import Post
# Create your views here.

class HomeView(ListView):
      model=Post
      queryset=Post.objects.all()
      template_name='index.html'
      context_object_name='blog_posts'
      ordering=['-created_date']
      paginate_by= 3

class  PostView(DetailView):
    model = Post
    template_name='post_detail.html'
   
class AboutView(ListView):
      model=Post
      template_name='about_page.html'

class ContactView(TemplateView):
    
    template_name = "contact.html"

    def post(self, request, *args, **kwargs):    
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if subject == '':
            subject = "WilsonBlog Contact"

        if name and message and email and phone:
            send_mail(
                subject+"-"+phone,
                message,
                email,
                ['wilsonmaseko94@gmail.com'], #to email
                fail_silently=False,
            )
            return render(request, 'contact.html',  {'name': name})
        else:
             
            return render(request, 'contact.html', {})
