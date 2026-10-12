from django.shortcuts import redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .models import CUser
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def signup_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    elif request.method == 'POST':
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if CUser.objects.filter(username=username).exists():
            messages.error(request, 'این نام کاربری قبلاً استفاده شده است.')
            return redirect('/')
        elif CUser.objects.filter(phone=phone).exists():
            messages.error(request, 'این شماره تماس قبلاً استفاده شده است.')
            return redirect('/')
        elif CUser.objects.filter(email=email).exists():
            messages.error(request, 'این ایمیل قبلاً استفاده شده است.')
            return redirect('/')
        else:  
            UserCreate = CUser.objects.create_user(username=username, phone=phone, email=email, password=password)
            UserCreate.save()

            login(request, UserCreate)

            messages.success(request, '{0} عزیز سلام، به پلتفرم جامع آیه خوش آمدید.'.format(username))
            return redirect('/')
    else:
        return redirect('/')

@csrf_exempt
def signin_view(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        try:
            UserModel = CUser.objects.get(phone=phone)
            if UserModel.is_active:
                if UserModel.check_password(password):
                    if UserModel.is_superuser:
                        login(request, UserModel)

                        messages.success(request, 'مدیر عزیز سلام، به پنل مدیریت آیه خوش آمدید.')
                        return redirect('/panel/')
                    else:
                        login(request, UserModel)

                        messages.success(request, '{0} عزیز سلام، به پلتفرم جامع آیه خوش آمدید.'.format(request.user.username))
                        return redirect('/')
                else:
                    messages.error(request, 'شماره تماس یا رمز عبور شما اشتباه می باشد.')
                    return redirect('/')
            else:
                messages.warning(request, 'اکانت شما غیرفعال است. لطفاً با پشتیبانی تماس بگیرید.')
                return redirect('/')
        except CUser.DoesNotExist:
            messages.error(request, "کاربری با این شماره وجود ندارد.")
            return redirect('/')
    else:
        return redirect('/')

def signout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')

@csrf_exempt
def profile_edit_view(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get('usernameForEdit')
            
            user = request.user

            if CUser.objects.filter(id=request.user.id).exists():
                if CUser.objects.filter(username=username):
                    messages.error(request, 'این نام کاربری قبلاً استفاده شده است.')
                    return redirect('/')
                else:
                    user.username = username
                    user.save()

                    messages.success(request, 'ویرایش اطلاعات با موفقیت انجام شد.')
                    return redirect('/')
            else:
                messages.error(request, 'ویرایش اطلاعات با مشکل مواجه شد.')
                return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('/')
