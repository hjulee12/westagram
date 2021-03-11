import json
import re
import bcrypt

from django.views   import View
from django.http    import JsonResponse

from .models    import Users

class SignupView(View):
    def post(self, request):
        data = json.loads(request.body)

        REGEX_email     = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        REGEX_password  = '^[A-Za-z0-9@#$%^&+=]{8,}$'

        try:

            if Users.objects.filter(email=data['email']).exists():
                return JsonResponse({"message":"USER_EXIST"}, status=400)
                
            if not re.match(REGEX_email, (data['email'])):
                return JsonResponse({"message":"INVALID_EMAIL"}, status=400)
                
            if not re.match(REGEX_password, (data['password'])):
                return JsonResponse({"message":"INVALID_PASSWORD"}, status=400)
            
            else:
                Users.objects.create(
                    email = data['email'],
                    password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
                )

                return JsonResponse({"message":"SUCCESS"}, status=200)

        except KeyError as e:
            return JsonResponse({"message":"KEY_ERROR =>" + e.args[0]}, status=400)
    
