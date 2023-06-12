from django.shortcuts import render
from .models import ProfileUser
import json
 

def home(request):  # sourcery skip: for-append-to-extend, list-comprehension
    stories=[]
    
    for user in ProfileUser.objects.all():
        item=[]
        for status in user.status.all():
            item.append({
                "type":"",
                "lenght":3,
                "src":(f'/{status.file}')  
                })
        stories.append({
            "id":str(user.uid),
            "photo":  f'/{user.photo}',
            "items":item,
            "name":user.name,
        })
    return render(request,'home.html',context={'stories':json.dumps(stories)})