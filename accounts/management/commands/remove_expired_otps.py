from typing import Any
from django.core.management.base import BaseCommand
from datetime import datetime,timedelta
from accounts.models import OtpCode
import pytz

class Command(BaseCommand):
    help = 'remove all expired otp codes'
    def handle(self, *args: Any, **options: Any):
        expire_time = datetime.now(tz=pytz.timezone('Asia/Tehran')) - timedelta(minutes=2)
        OtpCode.objects.filter(created__lt=expire_time).delete()
        self.stdout.write('all expired otp codes removed')