from django.shortcuts import render
from app38.forms import inputform

def fact(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def home(request):
    result = None
    n1 = None
    
    if request.method == "POST":
        form = inputform(request.POST)
        if form.is_valid():
            n1 = form.cleaned_data.get("input1")
            result = fact(n1)  # Calculate factorial using the fact function
    else:
        form = inputform()
    
    return render(request, "app38/index.html", {'param1': result, 'param2': n1, 'form': form})
# Create your views here.
