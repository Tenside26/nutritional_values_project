from django.shortcuts import render
from django.http import HttpResponseServerError
import requests


def calculator_page(request):

    template = "calculator.html"
    api_url = "http://127.0.0.1:8000/api/products"

    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            api_data = response.json()

            return render(request, template, {'api_data': api_data})
        else:
            return HttpResponseServerError(f"Error fetching data from API. Status code: {response.status_code}")

    except requests.exceptions.RequestException as e:

        return HttpResponseServerError(f"Error fetching data from API: {e}")

    except ValueError as e:

        return HttpResponseServerError(f"Error parsing JSON data: {e}")

    except Exception as e:

        return HttpResponseServerError(f"An unexpected error occurred: {e}")
