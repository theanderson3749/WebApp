from django.shortcuts import render

posts = [ #fake test data(list of dictionaries)
    {   
        'author': 'Devin Heng',
        'title': 'Fake blog post(dummy data)',
        'content': 'first fake post',
        'date_posted': 'June 16, 2020'  
    },
    {
        'author': 'Second Person',
        'title': 'Fake blog post(dummy data)',
        'content': 'second fake post',
        'date_posted': 'June 16, 2020'  
    }
]

#home page of the blog APP
def home(request):
    context = {
        'posts': posts #list of dictionaries
    }
    return render(request, 'blog/home.html', context) #this is how you pass in the template so you can use it
    #the third argument passes the data into the template and let us access it within the template

#about page of the blog APP
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'}) #passing in the template for the about page
