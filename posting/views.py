import json

from django.views import View
from django.http  import JsonResponse

from .models     import Post
from user.models import User

class PostingView(View):
# @login_decorator
    def post(self, request):
        data = json.loads(request.body)
        
        user        = User.objects.get(email=data['email'])

        user_id     = user.id
        image_urls  = data['image_urls']

        try:

            Post.objects.create(
                user_id     = user_id,   
                image_urls  = image_urls
            )

            return JsonResponse({'MESSAGE':'SUCCESS'}, status=200)

        except KeyError as e:
            return JsonResponse({'MESSAGE':'KEY_ERROR =>' + e.args[0]}, status=400)

#class PostingListView(View):
#    def get(self, request):
#        
#        try:


