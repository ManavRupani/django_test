
# from django.shortcuts import render
# import json 

# with open(r'C:\Users\manav\Desktop\python\blog\data_json.json') as f:
#     data = json.load(f)

# def home(request):
#     context = data
#     return render(request,'home.html',context)

# def blog(request):
#     context = data
#     return render(request,'blog.html',context)

# def me(request):
#     context = data
#     return render(request,'me.html',context)



from django.shortcuts import render
import json 
import os

def load_data():
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, 'datajson.json')
    with open(file_path) as f:
        return json.load(f)

def home(request):
    context = {'data': load_data()}
    return render(request,'home.html',context)

def blog(request):
    context = {'data': load_data()}
    return render(request,'blog.html',context)

def me(request):
    context = {'data': load_data()}
    return render(request,'me.html',context)

def blog_ind(request,id_json):
    data = load_data()
    item = data[int(id_json)]
    context = {'item':item}
    return render(request,'blog_detail.html',context)
