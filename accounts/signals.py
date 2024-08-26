from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Profile

@receiver(post_save, sender=Profile)
def add_user_to_students_group(sender, instance, created, **kwargs):
    if created:
        try:
            g1 = Group.objects.get(name='estudiantes')
        except Group.DoesNotExist:
            g1 = Group.objects.create(name='estudiantes')
            g2 = Group.objects.create(name='profesores')
            g3 = Group.objects.create(name='preceptores')
            g4 = Group.objects.create(name='administrativos')
        instance.user.groups.add(g1)