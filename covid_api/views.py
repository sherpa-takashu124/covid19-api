from django.shortcuts import render
from django.views import View
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse, Http404
from covid import Covid


class WorldCovidCase(APIView):
    def get(self, request, *args, **kwargs):
        covid = Covid(source="worldometers")
        covid_world_case = covid.get_data()
        if covid_world_case:
            return Response(covid_world_case, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'server fail'}, status=status.HTTP_204_NO_CONTENT)


class CovidCaseByCountryCode(APIView):
    def post(self, request, *args, **kwargs):
        covid = Covid(source="worldometers")
        query_word = request.data.get('id', None)
        print(query_word)
        country_case = covid.get_status_by_country_name(query_word)
        if country_case:
            return Response(country_case, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'server fail'}, status=status.HTTP_204_NO_CONTENT)


class GlobalCase(APIView):
    def get(self, request):
        covid = Covid(source="worldometers")
        globalresponse = {}
        globalresponse['confirmedCase'] = covid.get_total_confirmed_cases()
        globalresponse['activeCase'] = covid.get_total_active_cases()
        globalresponse['recoveredCase'] = covid.get_total_recovered()
        globalresponse['deathCase'] = covid.get_total_deaths()
        return Response(globalresponse, status=status.HTTP_200_OK)


class CountryList(APIView):
    def get(self, request):
        covid = Covid(source="worldometers")
        country_list = covid.list_countries()
        if country_list:
            return Response(country_list, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'server fail'}, status=status.HTTP_204_NO_CONTENT)
