from django.urls import path





from .views import phonenumber_details, countryInformation, seracher_details, home



urlpatterns = [
    path('', home, name="Home Page"),
    path('api/phonenumber/<int:phonenumber>/', phonenumber_details, name="phonenumber_details"),
    path('api/country/<str:country>/',countryInformation, name='country_information' ),
    path('api/searcher/', seracher_details, name="searcher_details")
]
