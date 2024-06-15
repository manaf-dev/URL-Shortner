from django.shortcuts import render
import requests
from .models import UrlData

# Create your views here.
def index(request):
    if request.method == 'POST':
        original_url = request.POST.get('userUrl')
        new_url = shortenUrl(original_url)
        url = UrlData.objects.create(original_url = original_url, short_url = new_url)
        return render(request, 'shortner/new_url.html', {'new_url':new_url})
    return render(request, 'shortner/index.html')


def shortenUrl(original_url):
    bitly_api_url = "https://api-ssl.bitly.com/v4/shorten"
    headers = {'Authorization': 'Bearer b08cf81536a92c758f5386d98cb434ae1b8215a0'}
    payload = {'long_url': original_url}
    try:
        response = requests.post(bitly_api_url, headers=headers, json=payload)
        if response.status_code == 200:
            return response.json()['link'] 
            # return new_url

    except Exception as e:
        return 'Error: There is a problem with your connection'