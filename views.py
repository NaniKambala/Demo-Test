from django.shortcuts import render,redirect
from rest_framework.response import Response
from.forms import FileForm
from.models import Users
from.serializer import signupSerializer
from.serializer import fileSerializer
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required,user_passes_test
from.models import File
from django.http import FileResponse
from django.shortcuts import get_object_or_404



def otp_generation():
    return random.randint(100000,999999)

def send_email(email):
    Generate=otp_generation()
    subject='verification of otp'
    to_list=[email]
    message=f'Hello....! {email}\nHere is your OTP: {Generate}'
    send_mail(subject,message,settings.EMAIL_HOST_USER,to_list)


# Create your views here.
@api_view(['GET','POST'])
def signupUser(request,snp_id=None):
    if request.method == 'GET':
        signupdata=Users.objects.all()
        signupserializeddata=signupSerializer(signupdata,many=True)
        return render(request,'signup.html')
    if request.method == 'POST':
        signupdata=request.data
        print(signupdata)
        Sdata=signupSerializer(data=signupdata,many=True)
        email=Sdata[email]
        if Sdata.is_valid() == True:
            send_email(email)
            Sdata.save()
            messages.success(request,'succefully stored your details')
            return render(request,'login.html')
        else:
            messages.error(request,'please re enter your details')
            return redirect('signupurl') 
        return render(request,'signup.html')

def login(request):
    if request.method == 'POST':
        uname=request.POST['uname']
        pwd=request.POST['pwd']
        validuser=authenticate(request,Username=uname,password=pwd)
        if validuser != None:
            return render(request,'insert.html')
        else:
            messages.error(request,'Invalid credentials')
            return render(request,'login.html')
    return render(request,'login.html')

def insertfile(request):
    fileform=FileForm()
    if request.method == 'POST':
        filedata=FileForm(request.POST,request.FILES)
        if filedata.is_valid() == True:
            filedata.save()
            messages.success(request,'File inserted succefully')
            return redirect('filelisturl')
        else:
            messages.error(request,'file insertion failed')
    return render(request,'insert.html',{'form':fileform})
def displayfileslist(request):
    file=File.objects.all()
    return render(request,'list.html',{'files':file})

def download_file(request, fileid):
    file_instance = get_object_or_404(File, id=fileid)
    file_path = file_instance.file.path
    with open(file_path, 'rb') as file:
        response = FileResponse(file)
        response['Content-Disposition'] = f'attachment; filename="{file_instance.file.name}"'
        return response







    



