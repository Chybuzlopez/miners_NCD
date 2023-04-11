from django.core.management.base import BaseCommand
from miners92.models import Alert WorkerCluster

class Command(BaseCommand):
    help = 'Check the status of the mining workers and triggers alerts if necessary'

    def handle(self, *arg, **options):
        workers = WorkerCluster.objects.all()
        for worker in workers:
            if not worker.is_online:
                alert = Alert.objects.create(
                        alert_type='offline',
                        message=f'Mining worker {worker.name} is offline'
                        )
            elif worker.cpu_usage > 90:
                alert = Alert.objects.create(
                        alert_type='high_cpu',
                        message=f'Mining worker {worker.name} has high CPU usage ({worker.cpu_usage}%)'
                        )
