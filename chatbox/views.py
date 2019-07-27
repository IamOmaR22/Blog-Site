from django.shortcuts import render
from .models import chat

def chatboxview(request):
    mychat = chat.objects.filter()
    context = {'mychat':mychat}
    if request.method == 'POST':
        if request.POST.get('chat') and request.POST.get('name'):
            Chat = chat()
            Chat.text = request.POST.get('chat')
            Chat.name=request.POST.get('name')
            Chat.save()
            return render(request, 'chatbox.html',context)
    else:
        return render(request, 'chatbox.html',context)
