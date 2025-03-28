from django.urls import path, include

app_name = 'users'
urlpatterns = [
    # Include the authentication URLs provided by Django
    path('', include('django.contrib.auth.urls')),
]