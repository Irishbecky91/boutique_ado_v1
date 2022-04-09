"""
veiws.py defines all views
"""

from django.shortcuts import render


# Create your views here.
def index(request):
    """
    Renders the index template
    """
    return render(request, 'home/index.html')
