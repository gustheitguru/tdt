from django.shortcuts import render

def home(request):
	return render(request, "home.html", {})

def about(request):
	return render(request, "about.html", {})

def bc(request):
	return render(request, "bc.html", {})

def bjj(request):
	return render(request, "bjj.html", {})

def mt(request):
	return render(request, "mt.html", {})

def pt(request):
	return render(request, "pt.html", {})

def nutrition(request):
	return render(request, "nutrition.html", {})

def training(request):
	return render(request, "training.html", {})