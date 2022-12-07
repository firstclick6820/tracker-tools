from django.urls import path





from .views import phonenumber_details, countryInformation, seracher_details



urlpatterns = [
    path('phonenumber/<int:phonenumber>/', phonenumber_details, name="phonenumber_details"),
    path('country/<str:country>/',countryInformation, name='country_information' ),
    path('searcher/', seracher_details, name="searcher_details")
]
