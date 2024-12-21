from django.contrib.auth.decorators import login_required

from .models import Notifications
from django.shortcuts import render, get_object_or_404, redirect
@login_required(login_url='login')
def notificationview(request):
    if not request.user.activated:
        return redirect('activate_account')
    notifications = Notifications.objects.filter(user=request.user, is_read=False)
    if request.method == 'POST':
        notification_id=request.POST.get('notification_id')
        try:
            notification = Notifications.objects.get(id=notification_id)
        except Notifications.DoesNotExist:
            return redirect('notifications_view')
        if 'mark_as_read' in request.POST:
            notification.is_read=True
            notification.save()
            return redirect('notifications_view')
        if 'go_to' in request.POST:
            notification.is_read = True
            notification.save()
            return redirect('post_detail', post_id=notification.post.id)
    return render(request, 'notifications.html', {'notifications': notifications})