from django.db import models


class TodoTable(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    completed = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        task_completed = 'Completed' if self.completed else 'Not Completed'
        return f"{self.title} task is {task_completed}"
    
    

