from django.shortcuts import render, redirect
from main.forms import HomeForm
from django.views.generic import TemplateView
from main.models import PostModel, Friend
from django.contrib.auth.models import User
import itertools
# Create your views here.
class Post(TemplateView):
    template_name='main/home.html'
    def get(self,request):
        form=HomeForm()
        try:
            friend=Friend.objects.get(current_user=request.user)
            friends=friend.users.all()
        except:
            friend=[]
            friends=[]
        #posts=Post.objects.all()
        users=User.objects.exclude(id=request.user.id)
        #print(type(users))
        #for i in users:
        #    print(i)
        users=itertools.filterfalse(lambda x: x in friends,users)
        args={'form':form,'posts':PostModel.objects.all().order_by('post'),'users':users,'friends':friends}
        return render(request,self.template_name,args)
    def post(self,request):
        form=HomeForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=request.user
            post.save()
            text=form.cleaned_data['post']
            form=HomeForm()
            return redirect('/home/')
        args={'form':form,'text':text}
        return render(request,self.template_name,args)
class Users(TemplateView):
    template_name='main/profile.html'
    def get(self,request,pk):
        user=User.objects.get(pk=pk)
        args={'user':user}
        return render(request,self.template_name,args)
def change_friend(request,operation,pk):
    new_friend=User.objects.get(pk=pk)
    if operation=='add':
        Friend.make_friend(request.user,new_friend)
    else:
        Friend.lose_friend(request.user,new_friend)
    #return redirect('/profile/{}'.format(pk))
    return redirect('/home/')