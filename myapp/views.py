from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
'''
class GetSlangzz(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, *args, **kwargs):
        pass


'''

from django.shortcuts import render
from django.http import HttpResponse
import json
import requests

def index(request):
    '''
    with open('./data.json',"a") as file:
     #   configs = json.load(file)
        if request.method == 'POST':
            new_slangs=request.POST.get('searchBox1')
            new_meaning=request.POST.get('searchBox2')
            new_data = {'meaning':new_meaning,'slang':new_meaning}
            print(new_data)
            json.dump(new_data, file)

    '''
       
    with open('./data.json') as f :
        config = json.load(f)
       # config2=json.load(f2)
        context = {'': config}
       # context2 = {'': config2}
        if request.method == 'POST':
            slangs=request.POST.get('searchBox')
           
            

            for d in config:
                if d['slang'] == slangs :
                    pass_slang={'slang_view':d}
                    return render(request,'index.html',pass_slang)
                '''
                else:
                    error_message = "Oops ! Looks like 'Slang Not Found' 😔 "
                    pass_slang={'error_message': error_message}
                    return render(request,'index.html',pass_slang)
               '''
           
                    
                   

        else:
        
            return render(request,'index.html',{})


'''
    else:
        return render(request,'index.html',"Oops ! Looks like 'Slang not find' 😔 ")

'''


def add(request):
    return render(request,'add.html',{})