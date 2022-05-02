from django.contrib import admin
from .models import Faq, Inquiry, Answer
# Register your models here.
admin.site.register(Faq)
admin.site.register(Answer)
admin.site.register(Inquiry)
