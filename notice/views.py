from django.views.generic import ListView, TemplateView
from .models import NoticePost


class ToppageView(TemplateView):
    template_name = 'toppage.html'


class SisuutaisuuView(TemplateView):
    template_name = 'sisuutaisuu.html'


class NoticeView(ListView):
    template_name = 'notice.html'
    context_object_name = 'notices'
    queryset = NoticePost.objects.order_by('posted_at')
