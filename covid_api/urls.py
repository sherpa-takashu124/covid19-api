from django.contrib import admin
from django.urls import path
from .views import WorldCovidCase, CountryList, GlobalCase, CovidCaseByCountryCode


urlpatterns = [
    path('', WorldCovidCase.as_view(), name='WORLDCOVIDCASE'),
    path('countries',CountryList.as_view(), name='countries'),
    path('global_data', GlobalCase.as_view(), name='globalData'),
    path('case_by_countryid', CovidCaseByCountryCode.as_view(), name='bycountryCode')



]