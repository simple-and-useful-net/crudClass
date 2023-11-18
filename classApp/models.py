from django.db import models


class MemoModel(models.Model):

    title       = models.CharField( verbose_name="タイトル",max_length=10)
    memo        = models.TextField()
    type_name   = models.TextField()
    # type_name   = models.TextField(verbose_name="animal", choices=ANIMAL_CHOICES, default="2")
    # type_name2  = models.TextField(verbose_name="都道府県", choices=PREFECT_CHOICES, blank=True, default=None)
    # categories  = models.ManyToManyField(BlogCategory)

    def __str__(self):
        return f"{self.id}=>{self.title} {self.memo}"
    

