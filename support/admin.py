from tabnanny import verbose
from django.contrib import admin
from support.models import Faq, Inquiry, Answer
# Register your models here.

# admin.site.register(Answer)
# admin.site.register(Inquiry)


class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 0
    verbose = '답변'
    verbose_name_plural = '답변'


@admin.register(Faq)
class FaqModelAdmin(admin.ModelAdmin):
    list_display = ('question', 'cartegori', 'last_updated_at')
    search_fields = ['question']
    list_filter = ['cartegori']


@admin.register(Inquiry)
class InquiryModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'title_category', 'created_at',
                    'writer', 'condition_category')
    search_fields = ['title', 'email', 'message', 'writer__username']
    list_filter = ['title_category', 'condition_category']
    inlines = [AnswerInline]
    actions = ['send_mail', ]

    def send_mail(modeladmin, request, queryset):
        for query in queryset:
            if query.email_btn:
                print(query.email)
            if query.message_btn:
                print(query.message)
