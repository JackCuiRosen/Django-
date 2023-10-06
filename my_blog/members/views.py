# from django.http import HttpResponse
# from django.template import loader
# def members(request):
#     template = loader.get_template('myfirst.html')
#     return HttpResponse(template.render())

from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
  mymembers = Member.objects.all().values()
  temp = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(temp.render(context,request))
def details(request,id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
      'mymembers': mymember,
    }
    return HttpResponse(template.render(context,request))
def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())
def testing(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('template.html')
    context = {
      'fruits':['Apple', 'Bnana', 'Renegade','Cherry','Pear'],
      'firstname':'Linus',
      'mymembers':mymembers,
      'greeting':1,
    }
    return HttpResponse(template.render(context,request))
def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

