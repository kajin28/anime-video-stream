from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Anime(models.Model):
    name = models.CharField(max_length=200)
    season_list = models.TextField()  # List of seasons in JSON or text
    episode_price = models.DecimalField(max_digits=5, decimal_places=2)  # Price of each episode
    image = models.ImageField(upload_to='anime_images/')

"""class Anime(models.Model):
    name = models.CharField(max_length=200)
    season_list = models.TextField()
    episode_price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='anime_images/')
    
    # 👇 New fields
    subscription_month = models.CharField(max_length=20, default='January')
    subscription_year = models.IntegerField(default=2025)

    def __str__(self):
        return self.name"""

class AnimeDetail(models.Model):
    anime = models.OneToOneField(Anime, on_delete=models.CASCADE, related_name='details')
    year = models.IntegerField(null=True, blank=True)
    hours = models.DecimalField(max_digits=4, decimal_places=1, default=1.0)
    language = models.CharField(max_length=50, default='Japanese')

    def __str__(self):
        return f"Details for {self.anime.name}"

class Episode(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name='episodes')
    title = models.CharField(max_length=200)
    duration = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.title} ({self.anime.name})"



class SubscriptionPlan(models.Model):
    PLAN_CHOICES = [
        ('Mobile', 'Mobile'),
        ('Super', 'Super'),
        ('Premium', 'Premium'),
    ]
    
    plan_name = models.CharField(max_length=50, choices=PLAN_CHOICES)
    devices = models.IntegerField(default=1)
    description = models.TextField(blank=True, null=True)
    has_ads = models.BooleanField(default=True)
    resolution = models.CharField(max_length=50, default='HD 720p')
    sound_quality = models.CharField(max_length=50, default='Stereo')
    duration_months = models.IntegerField(default=3)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    price_per_month = models.DecimalField(max_digits=6, decimal_places=2)
    features = models.TextField(blank=True, null=True)  # e.g. "Dolby Atmos, No Ads, etc."
    
    def __str__(self):
        return f"{self.plan_name} ({self.duration_months} months)"

class Payment(models.Model):

    PAYMENT_METHODS = [
        ('gpay', 'Google Pay'),
        ('phonepe', 'PhonePe'),
        ('paytm', 'Paytm'),
        ('card', 'Credit/Debit Card'),
    ]

    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.plan.plan_name} ({self.payment_method})"