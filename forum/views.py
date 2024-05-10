from django.shortcuts import render, get_object_or_404
from .models import *

def forum(request):
    queryset = Chat.objects.filter()
    data = {
        "title": 'Форум',
        'showprofile': True,
        'chats': queryset,
        'now': 'forum',
    }
    return render(request, 'forum/forum.html', data)

from django.contrib.auth import update_session_auth_hash
def forum_by_id(request, page_id):
    auth = False
    if request.user.is_authenticated:
        auth = True
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            message = Message(content=content, user=Profile.objects.get(user=request.user), chat=get_object_or_404(Chat, pk=page_id))
            user = Profile.objects.get(user=request.user)
            user.message_count += 1
            user.save()
            message.save()
            update_session_auth_hash(request, user)
    chat = get_object_or_404(Chat, pk=page_id)
    queryset = Chat.objects.filter()
    data = {
        "title": 'Форум',
        'showprofile': True,
        'page_name': chat.name,
        'messages': [[obj.id, obj.chat, str(obj.user), obj.content, obj.timestamp.strftime('%d.%m.%Y'), obj.timestamp.strftime('%H:%M')] for obj in chat.messages.all()],
        'chats': [[obj.id, obj.name] for obj in queryset],
        'now': 'forum',
        'auth': auth,
        'user_now': str(request.user.username),
    }
    return render(request, 'forum/forumbyid.html', data)