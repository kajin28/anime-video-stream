
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import User, Anime, SubscriptionPlan, Payment




# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        address = request.POST['address']
        email = request.POST['email']
        password = request.POST['password']
        
        # Create a new user
        user = User.objects.create(name=name, age=age, address=address, email=email, password=password)
        user.save()
        
        messages.success(request, 'Signup successful! Please log in.')
        return redirect('login')
    
    return render(request, 'signup.html')

# Login View
def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            user = User.objects.get(email=email, password=password)
            messages.success(request, 'Login successful!')
            return redirect('index')
        except User.DoesNotExist:
            messages.error(request, 'Invalid credentials. Please try again.')
    
    return render(request, 'login.html')



def index(request):
    animes = Anime.objects.all()
    return render(request, 'index.html', {'animes': animes})
# Detail view
def anime_list(request):
    animes = Anime.objects.all()
    return render(request, 'anime_list.html', {'animes': animes})

def anime_detail_view(request, anime_id):
    anime = get_object_or_404(Anime, pk=anime_id)
    episodes = anime.episodes.all()
    return render(request, 'animedetails.html', {
        'anime': anime,
        'episodes': episodes,
    })


def subscribe_view(request):
    plans = SubscriptionPlan.objects.all().order_by('price')
    return render(request, 'subscribe.html', {'plans': plans})

def payment_view(request, plan_id):
    plan = get_object_or_404(SubscriptionPlan, id=plan_id)
    return render(request, 'payment.html', {'plan': plan})


def payment_confirm(request):
    if request.method == "POST":
        plan_id = request.POST.get('plan_id')
        plan = get_object_or_404(SubscriptionPlan, id=plan_id)
        name = request.POST.get('name')
        email = request.POST.get('email')
        method = request.POST.get('method')

        payment = Payment.objects.create(
            plan=plan,
            customer_name=name,
            email=email,
            payment_method=method,
            amount=plan.price
        )
        payment.save()
        return render(request, 'payment_success.html', {'payment': payment})

    return redirect('subscribe')
    