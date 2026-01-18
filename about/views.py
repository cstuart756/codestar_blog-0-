from django.shortcuts import render
from .models import About
from .forms import CollaborateForm


def about(request):
    about_content = About.objects.first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {
            "about": about_content,
            "collaborate_form": collaborate_form,
        },
    )
