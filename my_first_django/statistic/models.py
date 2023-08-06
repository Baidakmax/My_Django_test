from django.db import models


class UserStat(models.Model):
    create_at = models.DateTimeField("Create", auto_now_add=True, null=True, editable=False)
    headers = models.TextField('Headers')

    class Meta:
        verbose_name = 'Статистика'
        verbose_name_plural = 'Статистика-плюрас-мета'

    def __str__(self):
        return str(self.pk)