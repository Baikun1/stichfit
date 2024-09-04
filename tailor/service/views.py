from django.shortcuts import render
import requests
# Create your views here.
def service(request):
    return render(request,'service.html')
# Pexels API Key (Ensure you keep your API keys secure)
PEXELS_API_KEY = 'z6WgIA7yCxOYa8RK1UMm2Sqvr3u0YMm4BPfiUVYQ3xd7KJQ8Zm1R6qdN'

def custom(request):
    # Pexels API endpoint for searching photos
    url = "https://api.pexels.com/v1/search"
    headers = {
        "Authorization": PEXELS_API_KEY
    }
    params = {
        "query": "fashion",  # The search term
        "per_page": 5        # Number of images to fetch per request
    }

    try:
        # Make the request to the Pexels API
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        images = data.get('photos', [])  # Extract the list of photos
    except requests.exceptions.RequestException as e:
        print(f"Error fetching images from Pexels: {e}")
        images = []  # Fallback to an empty list if the API call fails

    # Pass the images to the template
    return render(request, 'custom_template.html', {'images': images})