from django.contrib import admin
from .model import WorkerCluster, PerformancrMetrics
# Register your models here.

admin.site.register(WorkerCluster)
admin.site.register(PerformanceMetrics)
