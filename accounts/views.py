from django.shortcuts import render,redirect

def activate_account(request,uid,token):
    return redirect(f'http://localhost:3000/activate/{uid}/{token}')
