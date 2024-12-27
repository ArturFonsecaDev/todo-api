from django.dispatch import receiver
from django.db.models.signals import pre_save
from .models import Column

@receiver(pre_save, sender=Column)
def auto_increment(sender, instance, **kwargs):
    if instance.pk is None:
        todo_instance = instance.todo
        last_column = todo_instance.columns.order_by('-position').first()
        if last_column:
            instance.position = last_column.position + 1
            return
        instance.position = 1
