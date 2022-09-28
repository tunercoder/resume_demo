from django.shortcuts import render
from django.contrib import messages
from .models import (
    UserProfile,
    Blog,
    Portfolio,
    Certificate,
    Testimonial
)

from django.views import generic
from .forms import ContactForm


class IndexView(generic.TemplateView):
    template_name='main/index.html'


    def get_context_data(self, **kwargs):
        print('helooo')
        context= super().get_context_data(**kwargs)
        testimonials=Testimonial.objects.filter(is_active=True)
        certificates=Certificate.objects.filter(is_active=True)
        blogs=Blog.objects.filter(is_active=True)
        portfolio=Portfolio.objects.filter(is_active=True)
        context['testimonials']=testimonials
        context['certificates']=certificates
        context['blogs']=blogs
        context['portfolio']=portfolio
        return context

class ContactView(generic.FormView):
    form_class=ContactForm
    template_name='main/contact.html'
    success_url='/'


    def form_valid(self, form):
        form.save()
        messages.success(self.request,'Thankyou we will get back to you!')
        return super().form_valid(form)


class PortfolioView(generic.ListView):
    model=Portfolio
    template_name='main/portfolio.html'
    pageinated_by=10

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)



class PortfolioDetailView(generic.DetailView):
    model=Portfolio
    template_name='main/portfolio-detail.html'

class BlogView(generic.ListView):
    model=Blog
    template_name='main/blog.html'
    pageinated_by=10

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class BlogDetailView(generic.DetailView):
    model=Blog
    template_name='main/blog-detail.html'
    
