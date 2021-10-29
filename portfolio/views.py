from django.shortcuts import render

# Create your views here.


def about(request):
    return render(request, "portfolio/about.html")


def skills(request):
    return render(request, "portfolio/skills.html")


def works(request):
    return render(request, "portfolio/works.html")


def contact(request):
    return render(request, "portfolio/contact.html")


def fingers(request):
    return render(request, "portfolio/fingers.html")


def downloader(request):
    return render(request, "portfolio/downloader.html")


def rewriter(request):
    return render(request, "portfolio/rewriter.html")
