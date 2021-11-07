from django.shortcuts import redirect, render
from .models import Blog
from django.contrib.auth.models import User, auth
from django.contrib import messages



# Create your views here.
def index(request):
    blog = Blog.objects.all()
    return render(request, "index.html", {'blog' : blog})

def post(request , pk):    
    blog=Blog.objects.get(id=pk)
    return render(request, "post.html",{'blog' : blog})

def ragister(request):
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "email alerdy used!")
                return redirect('ragister')   
            elif User.objects.filter(username=username):
                messages.info(request, "username alerdy used!")
                return redirect('ragister')           
            else:
                user= User.objects.create_user(username=username ,email =email, password =password)
                user.save()
                return redirect('/')
        else:
            messages.info(request, 'password Not Same !')
            return redirect('/ragister/')

    else:
        return render(request, 'ragister.html')



def login(request):
    if request.method == 'POST':
        username= request.POST['username']
        password = request.POST['password']
        
        user =auth.authenticate(username=username , password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request ," Somethings Went Worng !")
            return redirect('login')
    else:
        return render(request , 'login.html')




    