from django.contrib import admin
from app.models import HomeModel, ContactModel, AboutModel, WorkModel, EducationModel, ServiceModel
# Register your models here.




admin.site.register(HomeModel)
admin.site.register(ContactModel)
admin.site.register(AboutModel)
admin.site.register(WorkModel)
admin.site.register(EducationModel)
admin.site.register(ServiceModel)