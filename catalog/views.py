from django.shortcuts import render

def home(request):
    return render(request, 'catalog/home.html')


#temporary for styling html
def search(request):
    query = request.GET.get('q', '').strip()
    
    results = [
        {'name': 'pomidor', 'price': '19.99'},
        {'name': 'ziemniak', 'price': '34.50'},
    ] if query else []

    return render(request, 'catalog/search_results.html', {
        'query': query,
        'results': results,
    })