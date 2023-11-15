from django.shortcuts import render
from .models import Webpage, AccessRecord

# Create your views here.

def index(request):
    webpages = Webpage.objects.all()
    access_records = AccessRecord.objects.all()

    # Combine data for display
    data = [{'webpage': webpage, 'access_date': access_record.date}
            for webpage, access_record in zip(webpages, access_records)]
    return render(request, 'index.html', {'data': data})

def help(request):    
    return render(request, 'help.html', {'key': 'Always here for you'})