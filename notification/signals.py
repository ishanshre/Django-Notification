from django.db.models.signals import post_save
from django.dispatch import receiver

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from notification.models import Notification

import json


@receiver(signal=post_save, sender=Notification)
def notification_handler(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "notification_broadcast", {
                'type':'send.notification',
                'message':json.dumps(instance.content)
            }
        )
        instance.sent = True