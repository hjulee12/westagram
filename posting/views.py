import json

from django.views import View
from django.http  import JsonResponse

from .models import Posts

#@login_decorator
class PostingView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            Posts.objects.create(
                user_id     = request.user.id,  # request.user will give you a User object representing the currently logged-in user.
                image_urls  = data['image_urls'],
            )

            return JsonResponse({'MESSAGE':'SUCCESS'}, status=200)

        except KeyError as e:
            return JsonResponse({'MESSAGE':'KEY_ERROR =>' + e.args[0]}, status=400)

class PostingListView(View):
    def get(self, request):
        
        try:


