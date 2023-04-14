from django.shortcuts import render

# Create your views here.
def TeeTimeBetView(request, teetime_pk):

    if request.method == "POST":
        teetime_data = get_object_or_404(Trip_TeeTime, pk=teetime_pk)