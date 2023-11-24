from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Delete old superuser created with the previous user model"

    def handle(self, *args, **options):
        try:
            old_superuser = User.objects.get(username="admin")
            old_superuser.delete()
            self.stdout.write(self.style.SUCCESS("Old superuser deleted successfully"))
        except User.DoesNotExist:
            self.stdout.write(self.style.SUCCESS("Old superuser not found"))
