import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eyeofjob.settings')  
django.setup()

from django.contrib.auth.models import User

User.objects.all().delete()