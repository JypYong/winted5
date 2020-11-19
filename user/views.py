import bcrypt
import jwt
import re
import json

from django.views import View
from django.http  import JsonResponse

from .models import User


class DuplicationView(View):
    def post(self , request):
        try:
            data    = json.loads(request.body)
            email   = data ["email"]
            pattern = r'[A-Z0-9._%+-]+@[A-Z0-9,-]+\.[A-Z]{2,4}'    
            regex   = re.compile(pattern,flags=re.IGNORECASE)
            users   = User.objects.filter(email=email)

            if len(regex.findall(email)) == 0:
                return JsonResponse({"message":"EMAIL_INVALID"},status=400)
            
            if users:
                return JsonResponse({"message":"SIGN_IN"},status=200)
            
            return JsonResponse({"message":"SIGN_UP"},status=200)

        except KeyError:
            return JsonResponse({"message":"Key_Error"},status=400)
        except json.decoder.JSONDecodeError :
            return JsonResponse({"message":"Json_Decode_Error"},status=400)

class SignUpView(View):
    def post(self , request):
        try :
            data          = json.loads(request.body)
            email         = data ["email"]
            password      = data ["password"]
            name          = data ["name"]
            phone         = data ["phone"] 
            hash_password = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt()).decode('utf-8')
            
            User.objects.create(
                email    = email,
                password = hash_password,
                name     = name ,
                phone    = phone 
            )
            return JsonResponse({"message":"SUCCESS"},status=201)

        except KeyError :
            return JsonResponse({"message":"Key_Error"},status=400)
        except json.decoder.JSONDecodeError :
            return JsonResponse({"message":"Json_Decode_Error"},status=400)

class SignInView(View):
    def post(self , request):
        try : 
            data              = json.loads(request.body)
            email             = data["email"]
            password          = data["password"]
            password_encode   = User.objects.get(email=email).password.encode('utf-8')
            users             = User.objects.get(email=email)

            user_data = {
                'id'               : users.id,
                'email'            : users.email,
                'phone'            : users.phone,
                'name'             : users.name,
                'profile_image_url': users.profile_image_url
            }

            if bcrypt.checkpw(password.encode('utf-8'), password_encode) :
                access_token  = jwt.encode({'user_id' : users.id}, SECRET, algorithm = ALGORITHM).decode('utf-8')
                return JsonResponse ({"message":"SUCCESS",'authorization':access_token, 'user_data' : user_data },status=200)

            return JsonResponse({"message":"INVALID EMAIL OR PASSWORD"},status=400)

        except KeyError :
            return JsonResponse({"message":"Key_Error"},status=400)
        except json.decoder.JSONDecodeError :
            return JsonResponse({"message":"Json_Decode_Error"},status=400)
        except User.DoesNotExist :
            return JsonResponse({"message":"Id not invalid"},status=400)