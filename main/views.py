from http.client import ImproperConnectionState
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from main.chain import Chain
from .models import Voter
from .form import CreateNewUser, Login
from .chain import Chain

chain_1 = Chain(20)
chain_2 = Chain(20)

def home(response):
    return render(response,"main/home.html", {})

def register(response):
    def form_validate():
        user = Voter.objects
        if form.cleaned_data["password"] != form.cleaned_data["confirm_password"]:
            return False
        elif len(form.cleaned_data["PVC_no"]) < 5:
            return False
        elif len(user.filter(PVC_no=form.cleaned_data["PVC_no"])) > 0:
            return False
        else:
            return True

    if response.method == "POST":
        form = CreateNewUser(response.POST)
        if form.is_valid() and form_validate():
            name = form.cleaned_data["name"]
            PVC_no = form.cleaned_data["PVC_no"]
            password = form.cleaned_data["password"]
            user = Voter(name=name, PVC_no=PVC_no, password=password, vote_ID="Empty", vote_status=False)
            user.save()
            user.vote_ID = str(user.id) + PVC_no[-1] + PVC_no[-2] + PVC_no[-3]
            user.save()
            form = Login()
            return render(response,"main/login.html", {"form":form, "vote_id":"Vote ID: " + user.vote_ID})
    else:
        form = CreateNewUser()
    return render(response,"main/register.html", {"form":form})

def login(response):
    if response.method == "POST":
        form = Login(response.POST)
        if form.is_valid():
            vote_ID = form.cleaned_data["vote_ID"]
            password = form.cleaned_data["password"]
            user = Voter.objects
            global usr_obj
            try:
                usr_obj = user.get(vote_ID=vote_ID)
            except:
                return render(response,"main/login.html", {"form":form})
            else:
                if usr_obj.password == password and usr_obj.vote_status == False:
                    return redirect("/vote")
    else:
        form = Login()
    return render(response,"main/login.html", {"form":form})

def vote(response):
    return render(response, "main/vote.html", {})

def button1(response):
    data = usr_obj.password + usr_obj.vote_ID
    if len(chain_1.blocks) == 0:
        chain_1.genesis_block()
        chain_1.append_to_pool(data)
        chain_1.mine()
        usr_obj.vote_status = True
        usr_obj.save()
    else:
        chain_1.append_to_pool(data)
        chain_1.mine()
        usr_obj.vote_status = True
        usr_obj.save()
    return render(response, "main/result.html", {"vote1_count":len(chain_1.blocks)-1, "vote2_count":len(chain_2.blocks)-1})

def button2(response):
    data = usr_obj.password + usr_obj.vote_ID
    if len(chain_2.blocks) == 0:
        chain_2.genesis_block()
        chain_2.append_to_pool(data)
        chain_2.mine()
        usr_obj.vote_status = True
        usr_obj.save()
    else:
        chain_2.append_to_pool(data)
        chain_2.mine()
        usr_obj.vote_status = True
        usr_obj.save()
    return render(response, "main/result.html", {"vote1_count":len(chain_1.blocks)-1, "vote2_count":len(chain_2.blocks)-1})

def result(response):
    return render(response, "main/result.html", {"vote1_count":len(chain_1.blocks)-1, "vote2_count":len(chain_2.blocks)-1})

