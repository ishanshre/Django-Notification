from django.shortcuts import render, HttpResponse
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json
# Create your views here.
def home(request):
    return render(request, "index.html", {
        'room_name':"broadcast"
    })



def testing_channel(request):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "notification_broadcast", {
            "type":"send.notification",
            "message": json.dumps("Notification")
        }
    )
    return HttpResponse("done")