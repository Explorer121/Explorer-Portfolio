from django.shortcuts import render
from django.views.generic import ListView, CreateView, View, TemplateView
from accounts.models import ProfileModel
from app.models import HomeModel, ContactModel, AboutModel, WorkModel, EducationModel, ServiceModel
from app.forms import ContactForm
# Create your views here.
    
from django.core.mail import send_mail



class Index(View):
     send_mail(
          'Subject here',
          'Here is the message.',
          'ba028ae02e30ab',
          ['lordnarry0@gmail.com'],
          fail_silently=False,
     )
     def get(self, request, *args, **kwargs):
          service_list = ServiceModel.objects.all()
          education_list = EducationModel.objects.all()
          work_list = WorkModel.objects.all()
          about_list = AboutModel.objects.all()
          object_list = HomeModel.objects.all()
          contact_form = ContactForm()
          context = {
               'object_list': object_list,
               'contact_form': contact_form,
               'about_list': about_list,
               'work_list': work_list,
               'education_list': education_list,
               'service_list': service_list,
          }
          return render(request, 'view/home.html', context)
     
     
     def post(self, request, *args, **kwargs):
          service_list = ServiceModel.objects.all()
          education_list = EducationModel.objects.all()
          work_list = WorkModel.objects.all()
          about_list = AboutModel.objects.all()
          object_list = HomeModel.objects.all()
          contact_form = ContactForm(request.POST)
          if contact_form.is_valid():
               instance = contact_form.save(commit=False)
               instance.user = request.user
               instance.save()
          
          # self.context['contact_form'] = contact_form
          # self.context['object_list'] = HomeModel.objects.all()
          
          context = {
               'object_list': object_list,
               'contact_form': contact_form,
               'about_list': about_list,
               'work_list': work_list,
               'education_list': education_list,
               'service_list': service_list,
          }
          return render(request, 'view/home.html', context)
          
     


def about(request):
     context = {}
     return render(request, "view/about.html", context)

class ContactCreate(CreateView):
     model = ContactModel
     fields = '__all__'
     template_name = 'view/contact.html'
     success_url = '/'
     