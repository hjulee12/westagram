import json

from django.views import View
from django.http  import JsonResponse

from .models     import Post
from user.models import User

class PostingView(View):
# @login_decorator
    def post(self, request):
        data = json.loads(request.body)
        
        user       = User.objects.get(email=data['email'])

        user_id    = user.id
        image_url  = data['image_url']

        try:

            Post.objects.create(
                user_id     = user_id,   
                image_url   = image_url
            )

            return JsonResponse({'MESSAGE':'SUCCESS'}, status=201)

        except KeyError as e:
            return JsonResponse({'MESSAGE':'KEY_ERROR =>' + e.args[0]}, status=400)

        except User.DoesNotExist:
            return JsonResponse({'MESSAGE':'INVALID_USER'}, status=400)


class PostingdetailView(View): 
    def get(self, request, post_id):

        try:

            posting = Post.objects.get(id=post_id)

            post = {
                'id'        : posting.id,
                'contents'  : posting.contents,
                'image_url' : posting.image_url,
                'created_at': posting.created_at,
            }

            return JsonResponse({'MESSAGE':'SUCCESS'}, status=200)

        except KeyError as e:
            return JsonResponse({'MESSAGE':'KEY_ERROR =>'+e.args[0]}, status=400)
        
        except User.DoesNotExist:
            return JsonResponse({'MESSAGE':'INVALID_USER'}, status=400)


class PostinglistView(View):
    def get(self, request):
        
        try:

            postings = Post.objects.order_by('-created_at').all()

            posting_lists = [{
                'id'        : posting.id,
                'contents'  : posting.contents,
                'image_url' : posting.image_url,
                'created_at': posting.created_at,
            } for posting in postings]

            return JsonResponse({'MESSAGE':'SUCCESS'}, status=200)

        except Exception as e:
            return JsonResponse({'MESSAGE':'KEY_ERROR =>'+ e.args[0]}, status=400)

        except User.DoesNotExist:
            return JsonResponse({'MESSAGE':'INVALID_USER'}, status=400)
