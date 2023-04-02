from django.shortcuts import render
from django.http import HttpResponse
#FPYaR6NqNCPNHD0BZEw/HA==ZyIuuL9csHHCnkyk

# Create your views here.
def home(request):
    import requests

query = '1lb brisket and fries'
api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
response = requests.get(api_url, headers={'X-Api-Key': 'YOUR_API_KEY'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)


    return render(request, 'home.html')
    