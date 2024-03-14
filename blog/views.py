
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

def load_data():
    with open('blog\datajson.json') as f:
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
