from django.shortcuts import render

def index_view(request):
    context = {'title':'Interested in learning','years_experience':'2','projects_complited':'5','happy_client':'+10',
               'about':'Interested and eager to learn in the field of technology, artificial intelligence, and software',
               'about_me_title':'back-end developer learner',
               'about_me':'Student of the 4th semester of Bachelor of Computer Engineering at the University of Science and Culture',
               'name':'salman sadafi','phone':'09389533216','age':'20','email':'sadafitehran.ms@gmail.com',
               'job':'back-end developer','nationality':'iran','address':'iran-tehran'}
    return render(request, 'website/index.html',context)
