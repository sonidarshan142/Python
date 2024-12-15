from django.shortcuts import render
from .models import *
from .utils import *
import random

# Create your views here.
# Which is contain all business logics

def home(request):
    return render(request, "myapp/index.html")


def login(request):

    if "email" in request.session:
        uid = User.objects.get(email = request.session["email"])
        cid = Chairman.objects.get(user_id = uid)
        contex = {
                    'uid' : uid,
                    'cid' : cid,
        }
        return render(request,"myapp/index.html",contex)
    else:

        if request.method == "POST":
            p_email = request.POST["email"]  
            p_password = request.POST["password"] 
            print("-------------------password varified--------------------------------")
            try:
                uid = User.objects.get(email = p_email)
                if uid:
                    print("-->>uid",uid.role)
                    if uid.role == "Chairman":
                        if uid.password == p_password:
                            cid = Chairman.objects.get(user_id = uid)
                            contex = {
                                'uid' : uid,
                                'cid' : cid,
                            }

                            request.session["email"] = p_email # store session here

                            return render(request,"myapp/index.html",contex )
                    else:
                        pass
                        print("--->outside ... else password")
                else:
                    print("Wrong credentials")
                    return render(request,"myapp/login.html")


            # print("Email ---->>",p_email)
            # print("-------------->>> Login Button Pressed !!!")

            except:
                e_msg = "Invalid Email or Password"
                return render(request,"myapp/login.html",{'e_msg' : e_msg})

        else:
            print("-------------->>> Login page Render !!!")
            print("-->>> outside")
            return render(request, "myapp/login.html")


def logoutuser(request):
    print("------------>>>>Called")
    if "email" in request.session:
        del request.session["email"]
        return render(request,"myapp/login.html")
    else:
        return render(request,"myapp/login.html") 
    
def profile(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session["email"])
        cid = Chairman.objects.get(user_id = uid)
        contex = {
                    'uid' : uid,
                    'cid' : cid,
        }
        return render(request,"myapp/profile.html",contex)
    else:
        return render(request,"myapp/login.html") 
    
def dashboard(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session["email"])
        cid = Chairman.objects.get(user_id = uid)
        contex = {
                    'uid' : uid,
                    'cid' : cid,
        }
        return render(request,"myapp/index.html",contex)
    else:
        return render(request,"myapp/login.html") 

def change_profile_password(request):
    if "email" in request.session:
        currentpassword = request.POST["currentpassword"]
        newpassword = request.POST["newpassword"]

        uid = User.objects.get(email = request.session["email"])
        cid = Chairman.objects.get(user_id = uid)

        if uid.password == currentpassword:
            uid.password = newpassword      # Update new password
            uid.save()      # save new password
            if currentpassword == newpassword:
                n_msg = "Cuurent password and newpassword both are same"

                contex = {
                    'uid' : uid,
                    'cid' : cid,
                    'n_msg' : n_msg,
                }
                return render(request,"myapp/profile.html",contex)

            s_msg = "Password Change Successfully !!!"
            contex = {
                    'uid' : uid,
                    'cid' : cid,
                    's_msg' : s_msg,
                
            }
            return render(request,"myapp/profile.html",contex)
        

        else:
            e_msg = "Invalid Current Password ---"

            contex = {
                    'uid' : uid,
                    'cid' : cid,
                    'e_msg' : e_msg,
                
            }
            return render(request,"myapp/profile.html",contex)
        

def update_profile(request):
    if request.POST:
        uid = User.objects.get(email = request.session["email"])
        cid = Chairman.objects.get(user_id = uid)

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        address = request.POST['address']
        contact_no = request.POST['contact_no']

        if "pic" in request.FILES:
            cid.pic = request.FILES['pic']
            cid.save()

        cid.save()

        contex = {
                    'uid' : uid,
                    'cid' : cid,
        }
        return render(request,"myapp/profile.html",contex)



def forgot_password(request):
    try:
        if request.POST:
            email = request.POST['email']
            uid = User.objects.get(email = email)
            otp = random.randint(1000,9999)

            if uid:
                uid.otp = otp
                uid.save()
                myCustomSendmail("Forgot password","mailtemplate",email,otp)
                return render(request,"myapp/change_password.html",{'email' : email})
            
        return render(request,"myapp/forgot_password.html")
    except Exception as e:
        return render(request,"myapp/change_password.html",{'e_msg': "Invalid Email"})

 
def update_password(request):
    if request.POST:
        email = request.POST['email']

        otp = request.POST['otp']
        newpassword = request.POST['newpassword']
        renewpassword = request.POST['renewpassword']

        uid = User.objects.get(email = email)

        if str(uid.otp) == otp:
            if newpassword == renewpassword:
                uid.password = newpassword
                uid.otp = 456
                uid.save()
                s_msg = "Successfully Password Reset !!"
                return render(request,"myapp/login.html", {'s_msg': s_msg})
            
            else:
                e_msg = "Incorrect new-Password and re-password"
                return render(request,"myapp/change_password.html", {'email':email,'e_msg': e_msg}) 
            
        else:
            e_msg = "Invalid otp"
            return render(request,"myapp/change_password.html", {'email':email,'e_msg': e_msg})
        
    else:
        return render(request,"myapp/login.html")


def add_notice(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(user_id = uid)
        context = {
                    'uid' : uid,
                    'cid' : cid,
        }
        if request.POST:
            title = request.POST['title']
            description = request.POST['description']
            pic = request.POST['pic']

            if "pic" in request.FILES:
                nid = Notice.objects.create(user_id = uid, title = title, description = description , pic = pic)

            else:
                nid = Notice.objects.create(user_id = uid, title = title, description = description)
                
            if nid:
                context = {
                    'uid' : uid,
                    'cid' : cid,
                    's_msg' : "Successfully Notice Added"
                }
                return render(request,"myapp/add_notice.html",context)
            
        else:
            return render(request,"myapp/add_notice.html",context)


def view_notice(request):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(user_id = uid)

        nall = Notice.objects.all()

        context = {
                    'uid' : uid,
                    'cid' : cid,
                    'nall' : nall,
        }
        return render(request,"myapp/noticelist.html",context)

def delete_notice(request,pk):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(user_id = uid)

        nid = Notice.objects.get(id = pk)
        nid.delete()
        nall= Notice.objects.all()

        context = {
                    'uid' : uid,
                    'cid' : cid,
                    'nall' : nall,
        }
        return render(request,"myapp/noticelist.html",context)
    



def edit_notice(request, pk):
    if "email" in request.session:
        uid = User.objects.get(email = request.session['email'])
        cid = Chairman.objects.get(user_id = uid)
        nid = Notice.objects.get(id = pk)
        context = {
                    'uid' : uid,
                    'cid' : cid,
                    'nid' : nid
        }
        return render(request,"myapp/edit_notice.html",context)

    else:
        return render(request,"myapp/edit_notice.html",context)


def update_notice(request):
    if request.POST:
            uid = User.objects.get(email = request.session['email'])
            cid = Chairman.objects.get(user_id = uid)

            title = request.POST['title']
            description = request.POST['description']
            id = request.POST["id"]

            nid = Notice.objects.get(id = id)
            if "pic" in request.FILES:
                nid.title = title
                nid.description = description
                nid.pic = request.POST["pic"]
                nid.save()
            else:
                nid.title = title
                nid.description = description
                nid.save()
                
            context = {
                'uid' : uid,
                'cid' : cid,
                's_msg' : "Successfully Notice updated"
            }
            return render(request,"myapp/edit_notice.html",context)



# for  members 



        

    



