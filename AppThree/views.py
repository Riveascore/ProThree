from django.shortcuts import render
from AppThree.models import User

# Create your views here.
def index(request):
  users = User.objects.order_by("firstname")
  users_dict = {
    'users': users
  }
  return render(request, 'AppThree/index.html', context=users_dict)
