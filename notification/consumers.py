import json

from channels.generic.websocket import AsyncWebsocketConsumer

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("+++++++++Web socket connection initialized+++++++")
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"notification_{self.room_name}"
        print(self.room_group_name)
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()
    
    async def send_notification(self, event):
        print(event)
        message = json.loads(event['message'])
        print(type(message))
        await self.send(text_data=json.dumps(message))
    
    
    async def disconnect(self, code):
        print("websocket disconnected.......")
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
    
    
