import uuid
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect


def generate_token(user = None):
    token_generate = str(uuid.uuid4())
    token = Token.objects.get_or_create(user=user, defaults={'user': user, 'key': token_generate})
    return token

def destroy_token(user):
    user_id = user.id
    token = get_object_or_404(Token, user_id=int(user_id))
    token.delete()
    return redirect('/')

