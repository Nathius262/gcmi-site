from django.shortcuts import render

# Create your views here.
def index_view(requet):
    return render(requet, "index.html")