from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.URLField()
    release_date = models.DateField()
    lte_exists = models.BooleanField(default=True)
    slug = models.SlugField(max_length=255, db_index=True)

