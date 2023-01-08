from notification.models import Notification

def notifications(request):
    notifications = Notification.objects.all()
    return {
        "notifications":notifications
    }
