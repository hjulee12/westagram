import json, bcrypt, jwt
import re

from django.views   import View
from django.http    import JsonResponse

from .models      import User
from my_settings  import SECRET, ALGORITHM

class SignupView(View):
    def post(self, request):
        data = json.loads(request.body)

        REGEX_email     = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        REGEX_password  = '^[A-Za-z0-9@#$%^&+=]{8,}$'

        try:

            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({"message":"USER_EXIST"}, status=400)
                
            if not re.match(REGEX_email, (data['email'])):
                return JsonResponse({"message":"INVALID_EMAIL"}, status=400)
                
            if not re.match(REGEX_password, (data['password'])):
                return JsonResponse({"message":"INVALID_PASSWORD"}, status=400)
            
            else:
                # bcrypt.hashpw() 메소드 이용해 암호화
                user_signup = User(
                    email = data['email'],
                    password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
                ).save()

                return JsonResponse({"message":"SUCCESS"}, status=200)

        except KeyError as e:
            return JsonResponse({"message":"KEY_ERROR =>" + e.args[0]}, status=400)


class SigninView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
             
            if User.objects.filter(email=data['email']).exists():
                user = Users.objects.get(email=data['email'])

                # bcrypt.checkpw() 메소드 이용해 비밀번호 확인(입력받은 pw, 저장된 암호화된 pw): 데이터타입은 Bytes
                if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                    access_token = jwt.encode({'id':user.email}, SECRET, ALGORITHM)
                    
                    return JsonResponse({"message":"SUCCESS", "ACCESS_TOKEN":access_token}, status=201)

                return JsonResponse({"message":"INVALID_USER"}, status=401)

            return JsonResponse({"message":"INVALID_USER"}, status=401)

        except KeyError as e:
            return JsonResponse({"message":"KEY_ERROR =>" + e.args[0]}, status=400)
