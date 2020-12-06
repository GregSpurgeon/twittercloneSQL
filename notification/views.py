from django.shortcuts import render
from notification.models import Notification
from twitteruser.models import TwitterUser

# Create your views here.


def notification_view(request):
    notifications = Notification.objects.filter(user_mentioned=request.user)
    unseen_notification = notifications.filter(seen_message=False)
    for notification in unseen_notification:
        notification.seen_message = True
        notification.save()
    return render(request, 'notification.html', {'notifications': unseen_notification})

