from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import UpdateView

from app.forms import UserSignupForm, UserSignupEditForm
from app.models import User

# Create your views here.


class Home(View):
    def get(self, request):
        return render(request, 'login.html', {'title' : "User Login"})

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            get_user = User.objects.get(email=email)
            user = authenticate(request, username=get_user.username, password=password)
        except:
            # msg
            return redirect('home')

        if user is not None:
            login(request, user)
            if user.is_authenticated:
                # msg
                return redirect('user_details')
            else:
                logout(request)
                # msg
                return redirect('home')
        else:
            # msg
            return redirect('home')

        return redirect('home')


class SignUp(View):
    def get(self, request):
        form = UserSignupForm
        return render(request, 'signup.html',{'forms':form, 'title':"User Signup"})

    def post(self, request):
        form = UserSignupForm(request.POST or None)
        if form.is_valid():
            form.save()
            print('user created')
            return redirect('home')
        else:
            # msg
            return redirect('signup')


class LogOut(View, LoginRequiredMixin):
    def get(self, request):
        logout(request)
        # msg
        return redirect('home')

class User_Details(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'allUsers': User.objects.all(),
            'title': "User Details"
        }
        return render(request, 'user_details.html', context)


class User_Detail_Edit(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserSignupEditForm
    template_name = 'user_details_update.html'

    def form_valid(self, form):
        form.save()
        return redirect('user_details')


class DeleteUser(LoginRequiredMixin, View):
    def get(self, request, id):
        p = User.objects.get(id=id)
        p.delete()
        return redirect('user_details')