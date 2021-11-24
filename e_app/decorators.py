
from django.shortcuts import redirect

# my decorator
def login_required_d(myfuction):
    def check(request):
        if request.user.is_authenticated:
            return myfuction(request)
        else:
            return redirect('loginuser')
    return check