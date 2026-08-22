from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    data = {
        'author': 'Apurba',
        'age': 20,
        'lst': ['python', 'is', 'easy'],
        'birthday': datetime.datetime.now(),
        'courses' : [
            {
                'id' : 1,
                'name' : 'python',
                'fee' : 2000,
            },
            {
                'id' : 2,
                'name' : 'Django',
                'fee' : 3000,
            },
            {
                'id' : 3,
                'name' : 'C++',
                'fee' : 1000,
            },
        ]
    }
    return render(request, 'home.html', data)