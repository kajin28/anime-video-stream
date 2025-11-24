from django.contrib import admin
from myapp.models import User
from .models import Anime, Episode # Removed AnimeDetail import
from .models import SubscriptionPlan, Payment

admin.site.register(User)



# Removed AnimeDetailInline and references to it
class AnimeAdmin(admin.ModelAdmin):
    pass  # No inline now

admin.site.register(Anime, AnimeAdmin)
admin.site.register(Episode)

# Removed this line:
# admin.site.register(AnimeDetail)
class EpisodeInline(admin.TabularInline):
    model = Episode
    extra = 1  # Number of blank episodes to show

@admin.register(SubscriptionPlan)
class SubscriptionPlanAdmin(admin.ModelAdmin):
    list_display = ('plan_name', 'duration_months', 'price', 'price_per_month', 'has_ads')
    list_filter = ('plan_name', 'has_ads')
    search_fields = ('plan_name',)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'plan', 'payment_method', 'amount', 'payment_date')
    list_filter = ('payment_method', 'payment_date')