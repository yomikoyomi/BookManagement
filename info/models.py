from django.db import models


class trn_infomation(models.Model):
    INFO_CHOICE = (
        ('01', '通常'),
        ('02', '重要'),
    )

    """ お知らせ """
    title = models.CharField('タイトル', max_length=100)
    value = models.TextField('本文')
    date_joined = models.DateTimeField('登録日時', auto_now_add=True, editable=False)
#    user_joined =
    date_updated = models.DateTimeField('更新日時', auto_now=True, editable=False)
#    user_updated = 
    infomation_division = models.CharField('重要度', max_length=2, choices=INFO_CHOICE)
