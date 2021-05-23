from django.shortcuts import render

def home_view(request):
    return render(request, "home.html", {})

def results_view(request):
    return render(request, "results.html")

# def request_page(request):
#   if(request.GET.get('mybtn')):
#     response = yelp_api.search_query(categories='restaurants', longitude=14.439893669268018, latitude=50.07851691127118, limit=10) 
#     return render(request, "results.html", context=response)
