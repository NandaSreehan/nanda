from django.shortcuts import render
from django.http import HttpResponse
d={"student":[{"n":'nanda',"r":"224g5a0415","ts":7,"ps":3,'fs':4,'credits':54},
              {"n":'dinesh',"r":"224g5a0416","ts":7,"ps":40,'fs':0,'credits':54},
              {"n":'nanda',"r":"224g5a0417","ts":7,"ps":3,'fs':4,'credits':54},
              {"n":'nanda',"r":"224g5a0418","ts":7,"ps":3,'fs':4,'credits':54},
              {"n":'nanda',"r":"224g5a0419","ts":7,"ps":3,'fs':4,'credits':54},
              {"n":'nanda',"r":"224g5a0420","ts":7,"ps":3,'fs':4,'credits':54}]}
def details(request):
    return render(request,"std.html",d)
def single(request,s):
    res=None
    for l in d["student"]:
        if s == l["r"]  :
            res=l
            break
    return render(request,"new.html",res)
    
def prime(request,s):
    a=True
    for i in range(2,int((s/2)+1)):
        if s%i==0:
            a=False
            break
    return render(request,"prime.html",{"ans":a})

def perfect(request,s):
    a=0
    for i in range(1,s):
        if s%i==0:
            a+=i
    j= (a==s)
        
    return render(request,"perfect.html",{"ans":j})
