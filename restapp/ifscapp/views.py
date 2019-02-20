from django.shortcuts import render
from django.http import HttpResponse
from . import serializer
from . models import Bankdata
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.core.files.storage import FileSystemStorage
from . import bank_data

# Create your views here.

#loads the data from csv file to database altering the csv file is easier and hence updation of bank details is simple process
def dataload(request):
    fs =FileSystemStorage() #To get current directory
    y = fs.location
    #print(y)
    bank_data.bank_update(y+"/ifscapp/csv/"+"bank_branches.csv")
    return HttpResponse("Datasets Loaded")


def dataquery(request):
    j = set()
    data = Bankdata.objects.all()
    for i in data:
        j.add(i.BankName)
    return render(request,'dquery.html',{'data':data,'j':j})

def dataquery1(request,data1):
    j = set()
    k = set()
    data = Bankdata.objects.all()
    for i in data:
        j.add(i.BankName)
    data = Bankdata.objects.filter(BankName=data1)
    for i in data:
        k.add()
    return render(request,'dquery.html',{'data':data,'j':j,'l':k})


def d_json(request):
    #renderer_classes = (JSONRenderer,)
    db = Bankdata.objects.all()
    ser = serializer.Bank_ser(db, many=True)
    content = JSONRenderer().render(ser.data)
    return HttpResponse(content,content_type="Application/json")

def d_jsonb(request,data):
    #renderer_classes = (JSONRenderer,)
    d = data.replace('7',' ')
    print(d)
    db = Bankdata.objects.filter(BankName=d)
    ser = serializer.Bank_ser(db, many=True)
    content = JSONRenderer().render(ser.data)
    j = "<option>Please select State</option>"
    unique = set()
    for data in db:
        unique.add(data.State)
    print(unique)
    for data in unique:
        j += "<option value="+data+">"+data+"</option>"
        #print(j)
    return HttpResponse(j)
    #return HttpResponse(content,content_type="Application/json")


def d_jsons(request,data,data1):
    #renderer_classes = (JSONRenderer,)
    d = data.replace('7',' ')
    d1 = data1.replace('7',' ')
    print(d,d1)
    db = Bankdata.objects.filter(BankName=d,State=d1)
    ser = serializer.Bank_ser(db, many=True)
    content = JSONRenderer().render(ser.data)
    j = "<option>Please select District</option>"
    unique = set()
    for data in db:
        unique.add(data.District)
    print (unique)
    for data in unique:
        j += "<option value="+data+">"+data+"</option>"


    return HttpResponse(j)
    #return HttpResponse(content,content_type="Application/json")

def d_jsonbr(request,data,data1,data2):
    #renderer_classes = (JSONRenderer,)
    d = data.replace('7',' ')
    d1 = data1.replace('7',' ')
    d2 = data2.replace('7',' ')
    print(d,d1,d2)
    db = Bankdata.objects.filter(BankName=d,State=d1,District=d2)
    ser = serializer.Bank_ser(db, many=True)
    content = JSONRenderer().render(ser.data)
    j = "<option>Please select Branch Name</option>"
    unique = set()
    for data in db:
        unique.add(data.Branch)
    for data in unique:
        j += "<option value="+data+">"+data+"</option>"
        #print(j)

    return HttpResponse(j)
    #return HttpResponse(content,content_type="Application/json")

def d_jsoni(request,data,data1,data2,data3):
    #renderer_classes = (JSONRenderer,)
    d = data.replace('7',' ')
    d1 = data1.replace('7',' ')
    d2 = data2.replace('7',' ')
    d3 = data3.replace('7',' ')
    print(d,d1,d2,d3)
    db = Bankdata.objects.filter(BankName=d,State=d1,District=d2,Branch=d3)
    ser = serializer.Bank_ser(db, many=True)
    content = JSONRenderer().render(ser.data)
    ifsc=''
    address=''
    for i in db:
        print(i.IFSC)
        ifsc+=i.IFSC
        address += i.Address
    #ifsc = db.IFSC

    return HttpResponse("<b class = 'ifsc'>IFSC CODE IS "+ifsc+address+"</b>")
    #return HttpResponse(content,content_type="Application/json")



