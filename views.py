from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home(request):
    return render(request, 'home.html',{
        "blogs":[
            {"title": "How buhari ruined Nigeria",
            "body": "This is is just for testing but buhari really ruined Nigeria",
            "No_of_comment": 10,
            "date": "22-02-2022"
            },
            {"title": "How buhari ruined Nigeria",
            "body": "This is is just for testing but buhari really ruined Nigeria",
            "No_of_comment": 10,
            "date": "22-02-2022"
            },
            {"title": "How Tinubu ruined Nigeria",
            "body": "This is is just for testing but buhari really ruined Nigeria",
            "No_of_comment": 10,
            "date": "22-02-2020"
            },
            {"title": "How Omoshomole became a godfather",
            "body": "This is is just for testing but buhari really ruined Nigeria",
            "No_of_comment": 10,
            "date": "22-02-2021"
            },
        ]
    })

def aboutUs(request):
    return HttpResponse("<p>This is we the dev at sight-innovation</p>")

def contactUs(request): 
    return HttpResponse("<p>Contact Us</p")