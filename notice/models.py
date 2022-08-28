from django.db import models


class NoticePost(models.Model):
    CATEGORY = (('宿題について', '宿題について'), ('授業について', '授業について'),
                ('定期テストについて', '定期テストについて'), ('その他', 'その他'))

    title = models.CharField(verbose_name='タイトル', max_length=200)
    target = models.CharField(verbose_name='対象', max_length=200, null=True)
    content = models.TextField(verbose_name='本文')
    url = models.URLField(verbose_name='URL', max_length=200, null=True, blank=True)
    url_name = models.CharField(verbose_name='URL先の名前', max_length=200, null=True)
    posted_at = models.DateTimeField(verbose_name='投稿日時', auto_now_add=True)
    category = models.CharField(verbose_name='カテゴリー', max_length=50, choices=CATEGORY)

    def __str__(self):
        return self.title

    # Create your models here.
