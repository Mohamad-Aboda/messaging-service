from rest_framework import serializers
from .models import Message, UserMessage


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ("id", "content",)


class UserMessageSerializer(serializers.ModelSerializer):
    message = MessageSerializer()
    from_user = serializers.SerializerMethodField()
    to_user = serializers.SerializerMethodField()


    class Meta:
        model = UserMessage
        fields = [
            "id",
            "message",
            "from_user",
            "to_user",
        ]

    def create(self, validated_data):
        msg_data = validated_data.pop('message')
        message = Message.objects.create(**msg_data)
        user_msg = UserMessage.objects.create(message=message, **validated_data)
        return user_msg
    
    def get_from_user(self, obj):
        return obj.from_user.username if obj.from_user else None

    def get_to_user(self, obj):
        return obj.to_user.username if obj.to_user else None

        

















