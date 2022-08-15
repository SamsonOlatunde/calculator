from django.shortcuts import render

# Create your views here.
def basic_calculator(a, b, operation):
    if(a.isnumeric() & b.isnumeric()):
        a = float(a)
        b = float(b)
        if operation == 'add':
            result = a + b
        elif operation == 'subtract':
            result = a - b
        elif operation == 'divide':
            result = a / b
        elif operation == 'multiply':
            result = a * b
        else:
            result = 'Operation supported: add, subtract, divide and multiply'
    else:
        result = 'Please enter a valid number for a and b'
    
    return result


def index(request):
    if request.method == "POST":
        a = request.POST['a']
        b = request.POST['b']
        operation = request.POST['operation']
        result = basic_calculator(a, b, operation)
        return render(request, 'index.html', {'result':result})
        
    return render(request, 'index.html')
