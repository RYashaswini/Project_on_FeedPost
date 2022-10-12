

from django.shortcuts import render,redirect
from django.conf import settings
import requests
from django.contrib import messages 
import json
from django.contrib.auth import logout
from django.core.paginator import Paginator 



url = settings.URL 

# Create your views here.

def register(request):

    if request.method == 'POST':
        user_name =  request.POST['txtUserName']
        email =  request.POST['txtEmail']
        password1 = request.POST.get('txtPwd1')
        password2 = request.POST.get('txtpwd2')

        if password1 == password2:
            data = {'username' : user_name, 'email' : email, 'password' : password1}
            response = requests.post('{url}/api/create_user/'.format(url=url) ,data=data) 
            print(response.text)
            get_response = response.json()
            print('--------------------------response----------------------------')
            if response.status_code > 300:
                print('--------------------------response>300----------------------------')
                messages.error(request,'Invalid')
                return render(request,'register.html')
            else:
                messages.success(request,("User created successfully"))
                return redirect('signin')
        else:
            return render (request,'register.html')
    else:
        return render (request,'register.html')


def signin(request):
    if request.method == 'POST':
        user_name =  request.POST['txtUserName']
        password =  request.POST['txtPwd']
        data={
            'username':user_name,
            'password':password,
            
        }
        response = requests.post('{url}/api/login/'.format(url=url) ,data=data) 
        print(response.text)
        if response.status_code >= 200 <300:
            messages.success(request,('Logged in successful'))
            print(response.text)
            dict=json.loads(response.text) 
            Token=(dict["token"])
            user_id=(dict["user_id"])
            superuser=(dict["superuser"])
            print(Token)
            # for getting session variable:
            request.session['get_token'] = Token 
            request.session['get_username'] = user_name 
            request.session['get_user_id'] = user_id
            print(user_name)
            print(user_id)

            # for setting session variable:
            # get_token = request.session.get('get_token')
            
            true = True
            if superuser == true:
                return redirect('retrieve')
            print('its user')
            return redirect('addpost')
        else:
            messages.error(request,("Wrong credentials. Try Again"))
            return render(request,'login.html')
    return render (request,'login.html')



def addpost(request):

    if request.method == 'POST':
        get_userid = request.session.get('get_user_id')
        get_username = request.session.get('get_username')
        get_token = request.session.get('get_token')
        data={
            'token':get_token,
            'username':get_username,
            'user_id':get_userid,
        }
      
        print(get_token)
        post_name =  request.POST['txtPostName']
        upload_image =  request.FILES.get('imgUpload')
        description = request.POST['txtDesc']
        get_userid = request.session.get('get_user_id')

        data = {'post_name' : post_name,  'description' : description,'user_id':get_userid}
        files = {'upload_image' : upload_image}

        print(get_userid)
        try:
            header={'Authorization':'Token {toki}'.format(toki=get_token)}
            print(header)
            print('try-----------------------------------')
            response = requests.post('{url}/api/create_postnn/'.format(url=url) ,headers=header, data=data , files=files)
            print(response.text)
            messages.error(request,("Posted Successfully!!!!")) 
            return redirect('addpost') 
        except:
            return redirect('addpost') 
    else:
        get_userid = request.session.get('get_user_id')
        get_username = request.session.get('get_username')
        get_token = request.session.get('get_token')
        data={
            'token':get_token,
            'username':get_username,
            'user_id':get_userid,
        }
        try:
            header={"Content-Type":"application/json; charset=UTF-8", 'Authorization':'Token {toki}'.format(toki=get_token)}
            print(header)
            response = requests.get('{url}/api/wholedata/{pk}/'.format(url=url,pk=get_userid),headers=header).json()
            # print(response)
            # return render (request,'post.html',{'data':data,'response':response})
           

            response_tup = tuple(response)
            if request.GET.get('showEntries', ''):
                val = request.GET.get('showEntries')
                print(val)
                response_data = Paginator(response_tup, val)
                page_number = request.GET.get('page')
                page_obj = response_data.get_page(page_number)
                return render (request,'post.html',{'data':data,'response' : response,'response_data':page_obj})
            else:
                response_data = Paginator(response_tup, 2)
                page_number = request.GET.get('page')
                page_obj = response_data.get_page(page_number)
                return render (request,'post.html',{'data':data,'response' : response,'response_data':page_obj})
        except:
            return redirect('signin')

def addstatus(request,post_id):

    if request.POST.get('hiddenapprove','') == 'appstatus':
        get_token = request.session.get('get_token')
        header={"Content-Type":"application/json; charset=UTF-8", 'Authorization':'Token {toki}'.format(toki=get_token)}
        print(header)
        collect_data = requests.get('{url}/api/update_post/{pk}/'.format(url=url,pk=post_id), headers=header)
        print(collect_data.text)
        print(type(collect_data))
        dict=json.loads(collect_data.text)     

        user_details = (dict["user_id"])
        user_id = user_details.get('id')
        print(user_id)
        
        status = "Approved"
      
        header_approve={'Authorization':'Token {toki}'.format(toki=get_token)} 


        # data = { 'post_name':post_name,  'description' : description, 'status' : status,'user_id':post_id}
        data = {'post_id':(dict["post_id"]),'post_name':(dict["post_name"]),  'description' : (dict["description"]),'status' : status, 'user_id':user_id}
        
                      
        response = requests.put('{url}/api/update_postnn/{pk}/'.format(url=url,pk=post_id) ,data=data,headers=header_approve)
        print(response.text)

        return redirect('retrieve')

    elif request.POST.get('hiddenreject','') == 'rejstatus':
        get_token = request.session.get('get_token')
        header={"Content-Type":"application/json; charset=UTF-8", 'Authorization':'Token {toki}'.format(toki=get_token)}
        print(header)
        collect_data = requests.get('{url}/api/update_post/{pk}/'.format(url=url,pk=post_id), headers=header)
       
        print(collect_data.text)
        print(type(collect_data))
        dict=json.loads(collect_data.text) 
        
        user_details = (dict["user_id"])
        user_id = user_details.get('id')
        print(user_id)

        status = "Rejected"
        reason = request.POST['txtReason']
      
        data = {'post_id':(dict["post_id"]),'post_name':(dict["post_name"]),  'description' : (dict["description"]),'status' : status,  'reason' : reason,'user_id':user_id}
      

        print(user_id)
        header_reject={'Authorization':'Token {toki}'.format(toki=get_token)} 

        response = requests.put('{url}/api/update_postnn/{pk}/'.format(url=url,pk=post_id) ,data=data, headers=header_reject)
        print(response.text)

        return redirect('retrieve')

    return render (request,'post.html') 


def retrieve(request):
    try:
        get_token = request.session.get('get_token')
        get_username = request.session.get('get_username')
        data={
            'token':get_token,
            'username':get_username,
        }
       
        print('0000000000000000000000000000')
        print(data)
        header={"Content-Type":"application/json; charset=UTF-8", 'Authorization':'Token {toki}'.format(toki=get_token)}
        print(header)
        print(get_token)

        response = requests.get('{url}/api/adminpost/'.format(url=url), headers=header).json()
        statusresponse = requests.get('{url}/api/actionstatus/'.format(url=url), headers=header).json()
      

        # statusresponse = Paginator(requests.get('{url}/api/actionstatus/'.format(url=url), headers=header).json(),4) 
        # page_number = request.GET.get('page')
        # print('00000000000000000')
        # print(page_number)
        # page_obj = statusresponse.get_page(page_number)

        return render (request,'retrieve.html',{'response' : response,'statusresponse' : statusresponse,'data':data}) 
        
    except:
        return redirect('signin')
    

def feedpost(request):
    response = Paginator(requests.get('{url}/api/approvestatus/'.format(url=url)).json(), 8)
    page_number = request.GET.get('page')
    
    page_obj = response.get_page(page_number)
    return render (request,'feed.html',{'response' : page_obj})

def user_logout(request):
    # logout(request)
    get_token = request.session.get('get_token')
    header={"Content-Type":"application/json; charset=UTF-8", 'Authorization':'Token {toki}'.format(toki=get_token)}
    logout_reponse = requests.post('{url}/logout/'.format(url=url), headers=header)
    print(logout_reponse)
    logout(request)
    messages.error(request,("Logged out successfully!!!!")) 
    return redirect('signin')
   

