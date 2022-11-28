from . import views
from . import amber_views
from . import green_views
from django.urls import path

urlpatterns = [
    path('login',views.login,name='Login'),
    path('signup/',views.signup, name='signup'),
    path('Economic_Red',views.Economic_Red, name='economic_view'),
    path('Education',views.Education, name= 'education_view'),
    path('Health',views.Health, name= 'health_view'),
    path('Protection',views.Protection, name= 'protection_view'),
    path('Nutrition',views.Nutrition, name= 'Nutrition_view'),
    path('view_all',views.view_all, name= 'all_view'),
    path('',views.Homeview.as_view(),name='home_view' ),
    path('search',views.search,name='search-results' ),
    path('Nutrition_Amber',amber_views.Nutrition_Amber, name= 'nutrition_amber'),
    path('Health_Amber',amber_views.Health_Amber, name= 'health_amber'),
    path('Economic_Amber',amber_views.Economic_Amber, name= 'economic_amber'),
    path('Protection_Amber',amber_views.Protection_Amber, name= 'protection_amber'),
    path('Nutrition_Green',green_views.Nutrition_Green, name= 'nutrition_green'),
    path('Health_Green',green_views.Health_Green, name= 'health_green'),
    path('Economic_Green',green_views.Economic_Green, name= 'economic_green'),
    path('Protection_Green',green_views.Protection_Green, name= 'protection_green'),
    path('Education_Green',green_views.Education_Green, name= 'education_green'),

]