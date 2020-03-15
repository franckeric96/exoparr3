from django.shortcuts import render

# Create your views here.

def index(request):
    datas = {
        
    }
    return render(request, 'index.html', datas)

def courses(request):
    datas = {
        
    }
    return render(request, 'Courses.html', datas)

def blog(request):
    datas = {
        
    }
    return render(request, 'blog.html', datas)

def contact(request):
    datas = {
        
    }
    return render(request, 'contact.html', datas)

def singleblog(request):
    datas = {
        
    }
    return render(request, 'single-blog.html', datas)

def elements(request):
    datas = {
        
    }
    return render(request, 'elements.html', datas)


def admission(request):
    datas = {
        
    }
    return render(request, 'Admissions.html', datas)


def eventdetails(request):
    datas = {
        
    }
    return render(request, 'event_details.html', datas)


def event(request):
    datas = {
        
    }
    return render(request, 'Event.html', datas)