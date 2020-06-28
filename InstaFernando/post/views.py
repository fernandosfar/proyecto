from django.shortcuts import render
#from django.http import HttpResponse
from datetime import datetime 


now = datetime.now().strftime("%b %dth, %Y - %H:%M hrs ")  
posts = [
    {
        'title': 'Mont Blanc',
        'user': {
            'name': 'Yésica Cortés',
            'picture': 'http://www.picsum.photos/60/60/?image=1027',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'http://www.picsum.photos/800/600?image=1036',
    },
    {
        'title': 'Via Láctea',
        'user': {
            'name': 'Christian Van der Henst',
            'picture': 'http://www.picsum.photos/60/60/?image=1005',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'http://www.picsum.photos/800/800/?image=903',
    },
    {
        'title': 'Nuevo auditorio',
        'user': {
            'name': 'Uriel (thespianartist)',
            'picture': 'http://www.picsum.photos/60/60/?image=883',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'http://www.picsum.photos/800/700/?image=1076',
    },
    {
        'title': 'Aurora',
        'user': {
            'name': 'William Stuard',
            'picture': 'http://www.picsum.photos/60/60/?image=805',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'http://www.picsum.photos/800/600/?image=873',
    },
    {
        'title': 'Rayo Solar ',
        'user': {
            'name': 'Fernando Limantour',
            'picture': 'http://www.picsum.photos/60/60/?image=365',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'http://www.picsum.photos/800/500/?image=102',
    } 
]
def list_posts(request):  
    return  render (request,'feed.html',{'posts':posts})







#    content = []
#    for post in posts:
#            content.append("""
#                    <p><strong>{name}</strong></p>
#                   <figure><img src="{picture}"/></figure>
#            """.format(**post))
    