from django.shortcuts import render

# render the base page which displays the simulated data
def base_Page(request):
    return render(request, 'index.html', {})
