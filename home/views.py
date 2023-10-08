from home.validators import get_clean_image
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django.shortcuts import redirect
from django.http import JsonResponse 
from django.utils.translation import ugettext_lazy as _
from products.models import brand, category, sub_category, segment
from .forms import *
from .serializers import *
from .models import *
from django.contrib import messages


def home(request):
    return render(request, 'index.html')

def banners(request):
    if request.method == "POST":
        try:    
            string = request.POST.get("list")
            list = string.split(",")
            for id in list:
                banner.objects.filter(id=id).delete()
            messages.info(request, 'Successfully deleted '+str(len(list))+' banners.')
            return JsonResponse({"status": 'success'}) 
        except:
            return JsonResponse({"error": 'Something went wrong'}) 
    else:
        data = banner.objects.order_by('-id')
        content={
            "content":data,
            "home":True,
            "title":"Banners",
            "name":"BANNER",
            "edit":"/dashboard/banners/"
        }
        return render(request, 'tables.html',content)

def box_banners(request):
    if request.method == "POST":
        try:    
            string = request.POST.get("list")
            list = string.split(",")
            for id in list:
                box_banner.objects.filter(id=id).delete()
            messages.info(request, 'Successfully deleted '+str(len(list))+' box banners.')
            return JsonResponse({"status": 'success'}) 
        except:
            return JsonResponse({"error": 'Something went wrong'}) 
    else:
        data = box_banner.objects.order_by('-id')
        content={
            "content":data,
            "home":True,
            "title":"Box banners",
            "name":"BOX BANNER",
            "edit":"/dashboard/box-banners/"
        }
        return render(request, 'tables.html',content)

def mini_banners(request):
    if request.method == "POST":
        try:
            string = request.POST.get("list")
            list = string.split(",")
            for id in list:
                mini_banner.objects.filter(id=id).delete()
            messages.info(request, 'Successfully deleted '+str(len(list))+' mini banners.')
            return JsonResponse({"status": 'success'}) 
        except:
            return JsonResponse({"error": 'Something went wrong'}) 
    else:
        data = mini_banner.objects.order_by('-id')
        content={
            "content":data,
            "home":True,
            "title":"Mini banners",
            "name":"MINI BANNER",
            "edit":"/dashboard/mini-banners/"
        }
        return render(request, 'tables.html',content)

def categories(request):
    if request.method == "POST":
        try:
            string = request.POST.get("list")
            list = string.split(",")
            for id in list:
                category.objects.filter(id=id).delete()
            messages.info(request, 'Successfully deleted '+str(len(list))+' categories.')
            return JsonResponse({"status": 'success'}) 
        except:
            return JsonResponse({"error": 'Something went wrong'}) 
    else:
        data = category.objects.order_by('-id')
        content={
            "content":data,
            "slug":True,
            "page":"/dashboard/category/",
            "title":"Categories",
            "name":"CATEGORY"
        }
        return render(request, 'tables.html',content)

def sub_categories(request):
    if request.method == "POST":
        try:
            string = request.POST.get("list")
            list = string.split(",")
            for id in list:
                sub_category.objects.filter(id=id).delete()
            messages.info(request, 'Successfully deleted '+str(len(list))+' sub categories.')
            return JsonResponse({"status": 'success'}) 
        except:
            return JsonResponse({"error": 'Something went wrong'}) 
    else:
        data = sub_category.objects.order_by('-id')
        content={
            "content":data,
            "slug":True,
            "page":"/dashboard/sub-category/",
            "title":"Sub Categories",
            "name":"SUB CATEGORY"
        }
        return render(request, 'tables.html',content)

def segments(request):
    if request.method == "POST":
        try:
            string = request.POST.get("list")
            list = string.split(",")
            for id in list:
                segment.objects.filter(id=id).delete()
            messages.info(request, 'Successfully deleted '+str(len(list))+' segments.')
            return JsonResponse({"status": 'success'}) 
        except:
            return JsonResponse({"error": 'Something went wrong'}) 
    else:
        data = segment.objects.order_by('-id')
        content={
            "content":data,
            "slug":True,
            "title":"Segments",
            "name":"SEGMENT"
        }
        return render(request, 'tables.html',content)

def brands(request):
    if request.method == "POST":
        try:
            string = request.POST.get("list")
            list = string.split(",")
            for id in list:
                brand.objects.filter(id=id).delete()
            messages.info(request, 'Successfully deleted '+str(len(list))+' brands.')
            return JsonResponse({"status": 'success'}) 
        except:
            return JsonResponse({"error": 'Something went wrong'}) 
    else:
        data = brand.objects.order_by('-id')
        content={
            "content":data,
            "brand":True,
            "slug":True,
            "page":"/dashboard/brand/",
            "title":"Brands",
            "name":"BRAND"
        }
    return render(request, 'tables.html', content)

def category_detail(request,pk):
    try:
        data = category.objects.get(pk=pk)
        subcat = data.sub_categories.order_by('-id')
    except:
        data = ""
        subcat = ""
    content={
        "content":data,
        "values":subcat,
        "slug":True,
        "title":"Category",
        "name":"Sub Categories",
        "page":"/dashboard/sub-category/"
    }
    return render(request, 'detail_table.html', content)

def subcategory_detail(request,pk):
    try:
        data = sub_category.objects.get(pk=pk)
        segments = data.segments.order_by('-id')
    except:
        data = ""
        segments = ""
    content={
        "content":data,
        "values":segments,
        "slug":True,
        "title":"Sub Category",
        "name":"Segments",
    }
    return render(request, 'detail_table.html', content)

def new_banners(request,value):
    error=""
    if request.method == "POST":
        try:
            form = bannerForm(request.POST,request.FILES)
            if form.is_valid():
                obj = ""
                if value == "banners":
                    obj = banner()
                elif value == "mini-banners":
                    obj = mini_banner()
                elif value == "box-banners":
                    obj = box_banner()
                if obj:
                    if form.cleaned_data["title"]:
                        obj.title = form.cleaned_data["title"]
                    else:
                        error = "Please enter your title"
                    if request.FILES and request.FILES["image"]:
                        error = get_clean_image(request.FILES["image"])
                        obj.image = request.FILES["image"]
                    elif obj.title:
                        error = "Please upload an image."
                    obj.url = form.cleaned_data["url"]
                    if not error:
                        obj.save()
                        if value == "banners":
                            messages.info(request, 'Banner "' + obj.title + '" added successfully.')
                        elif value == "mini-banners":
                            messages.info(request, 'Mini banner "' + obj.title + '" added successfully.')
                        elif value == "box-banners":
                            messages.info(request, 'box banner "' + obj.title + '" added successfully.')
                        return redirect("/dashboard/"+value+"/")
                    else:
                        return render(request, 'form.html',{"form":form,"error":error})
            else:
                return render(request, 'form.html',{"form":form,"error":"Invalid form details."})
        except:
            pass #error page here
    else:
        form = bannerForm()
        if value == "banners" or value == "mini-banners" or value == "box-banners":
            return render(request, 'form.html',{"form":form,"error":error})
        else:
            pass #error page here

def edit_banners(request,value,id):
    error =""
    if request.method == "POST":
        try:
            form = bannerForm(request.POST,request.FILES)
            if form.is_valid():
                if value == "banners":
                    obj = banner.objects.get(id=id)
                elif value == "mini-banners":
                    obj = mini_banner.objects.get(id=id)
                elif value == "box-banners":
                    obj = box_banner.objects.get(id=id)
                if obj:
                    if form.cleaned_data["title"]:
                        obj.title = form.cleaned_data["title"]
                    else:
                        error = "Please enter your title"
                    if request.FILES and request.FILES["image"]:
                        error = get_clean_image(request.FILES["image"])
                        obj.image = request.FILES["image"]
                    elif obj.title and not obj.image:
                        error = "Please upload an image."
                    obj.url = form.cleaned_data["url"]
                    if not error:
                        obj.save()
                        if value == "banners":
                            messages.info(request, 'Banner "' + obj.title + '" was changed successfully.')
                        elif value == "mini-banners":
                            messages.info(request, 'Mini banner "' + obj.title + '" was changed successfully.')
                        elif value == "box-banners":
                            messages.info(request, 'box banner "' + obj.title + '" was changed successfully.')
                        return redirect("/dashboard/"+value+"/")
                    else:
                        return render(request, 'form.html',{"form":form,"error":error})
            else:
                return render(request, 'form.html',{"form":form,"error":"Invalid form details."})
        except:
            pass #error page
    else:
        try:
            if value == "banners":
                data = banner.objects.get(id=id)
            elif value == "box-banners":
                data = box_banner.objects.get(id=id)
            elif value == "mini-banners":
                data = mini_banner.objects.get(id=id)
            image = data.image if data.image else ""
            title = data.title if data.title else ""
            url = data.url if data.url else  ""
            if value == "banners" or value == "mini-banners" or value == "box-banners":
                form = bannerForm(initial={"title":title,"image":image,"url":url})
                return render(request, 'form.html',{"form":form,"error":error})
        except:
                pass #error page here

def new_brand(request):
    error=""
    if request.method == "POST":
        try:
            form = brandForm(request.POST, request.FILES)
            if form.is_valid():
                obj = brand()
                if form.cleaned_data["title"]:
                    obj.title = form.cleaned_data["title"]
                else:
                    error = "Please enter your title"
                if request.FILES and request.FILES["image"]:
                    error = get_clean_image(request.FILES["image"])
                    obj.image = request.FILES["image"]
                elif not error and not obj.image:
                    error = "Please upload an image."
                if form.cleaned_data["status"]:
                    obj.status = form.cleaned_data["status"]
                elif not error:
                    error = "Please select status."
                obj.admin_remarks = form.cleaned_data["admin_remarks"]
                if not error:
                    obj.save()
                    messages.info(request, 'Brand "' + obj.title + '" added successfully.')
                    return redirect('/dashboard/brands/')
                else:
                    return render(request, 'form.html',{"form":form,"error":error})
            else:
                error="Invalid form details."
                return render(request, 'form.html',{"form":form,"error":error})       
        except:
            pass #error page     
    else:
        form = brandForm()
        return render(request, 'form.html',{"form":form,"error":error})

def edit_brand(request,id):
    error=""
    if request.method == "POST":
        try:
            form = brandForm(request.POST, request.FILES)
            if form.is_valid():
                obj = brand.objects.get(id=id)
                if form.cleaned_data["title"]:
                    obj.title = form.cleaned_data["title"]
                else:
                    error = "Please enter your title"
                if request.FILES and request.FILES["image"]:
                    error = get_clean_image(request.FILES["image"])
                    obj.image = request.FILES["image"]
                elif not error and not obj.image:
                    error = "Please upload an image."
                if form.cleaned_data["status"]:
                    obj.status = form.cleaned_data["status"]
                elif not error:
                    error = "Please select status."
                obj.admin_remarks = form.cleaned_data["admin_remarks"]
                if not error:
                    obj.save()
                    messages.info(request, 'Brand "' + obj.title + '" was changed successfully.')
                    return redirect('/dashboard/brands/')
                else:
                    return render(request, 'form.html',{"form":form,"error":error})
            else:
                error="Invalid form details."
                return render(request, 'form.html',{"form":form,"error":error})       
        except:
            pass #error page     
    else:
        try:
            data = brand.objects.get(id=id)
            image = data.image if data.image else ""
            title = data.title if data.title else ""
            status = data.status if data.status else ""
            remarks = data.admin_remarks if data.admin_remarks else ""
            form = brandForm(initial={"title":title,"image":image,"status":status,"admin_remarks":remarks})
            return render(request, 'form.html',{"form":form,"error":error})
        except:
            pass #error

def new_category(request):
    error = ""
    if request.method == "POST":
        try:
            form = categoryForm(request.POST, request.FILES)
            if form.is_valid():
                obj = category()
                if form.cleaned_data["title"]:
                    obj.title = form.cleaned_data["title"]
                else:
                    error = "Please enter your title"
                if request.FILES and request.FILES["image"]:
                    error = get_clean_image(request.FILES["image"])
                    obj.image = request.FILES["image"]
                elif not error and not obj.image:
                    error = "Please upload an image."
                if not error and form.cleaned_data["sub_categories"]:
                    obj.save()
                    for val in form.cleaned_data["sub_categories"]:
                        obj.sub_categories.add(val.id)
                if not error:
                    obj.save()
                    messages.info(request, 'Category "' + obj.title + '" added successfully.')
                    return redirect('/dashboard/categories/')
                else:
                    return render(request, "form.html",{"form":form,"error":error})
            else:
                error = "Invaid form details."
                return render(request, "form.html",{"form":form,"error":error})
        except:
            pass #error
    else:    
        form = categoryForm
        return render(request, 'form.html',{"form":form,"error":error})

def edit_category(request,id):
    error = ""
    if request.method == "POST":
        try:
            form = categoryForm(request.POST, request.FILES)
            if form.is_valid():
                obj = category.objects.get(id=id)
                if form.cleaned_data["title"]:
                    obj.title = form.cleaned_data["title"]
                else:
                    error = "Please enter your title"
                if request.FILES and request.FILES["image"]:
                    error = get_clean_image(request.FILES["image"])
                    obj.image = request.FILES["image"]
                elif not error and not obj.image:
                    error = "Please upload an image."
                if not error and form.cleaned_data["sub_categories"]:
                    obj.save()
                    for val in form.cleaned_data["sub_categories"]:
                        obj.sub_categories.add(val.id)
                if not error:
                    obj.save()
                    messages.info(request, 'Category "' + obj.title + '" was changed successfully.')
                    return redirect('/dashboard/categories/')
                else:
                    return render(request, "form.html",{"form":form,"error":error})
            else:
                error = "Invaid form details."
                return render(request, "form.html",{"form":form,"error":error})
        except:
            pass #error
    else:    
        try:
            data = category.objects.get(id=id)
            image = data.image if data.image else ""
            title = data.title if data.title else ""
            sub_categories = data.sub_categories.all() if data.sub_categories else ""
            form = categoryForm(initial={"title":title,"image":image,"sub_categories":sub_categories})
            return render(request, 'form.html',{"form":form,"error":error})
        except:
            pass #error

def new_subcategory(request):
    error = ""
    if request.method == "POST":
        try:
            form = sub_categoryForm(request.POST, request.FILES)
            if form.is_valid():
                obj = sub_category()
                if form.cleaned_data["title"]:
                    obj.title = form.cleaned_data["title"]
                else:
                    error = "Please enter your title"
                if request.FILES and request.FILES["image"]:
                    error = get_clean_image(request.FILES["image"])
                    obj.image = request.FILES["image"]
                elif not error and not obj.image:
                    error = "Please upload an image."
                if not error and form.cleaned_data["segments"]:
                    obj.save()
                    for val in form.cleaned_data["segments"]:
                        obj.segments.add(val.id)
                if not error:
                    obj.save()
                    messages.info(request, 'Sub Category "' + obj.title + '" added successfully.')
                    return redirect('/dashboard/sub-categories/')
                else:
                    return render(request, "form.html",{"form":form,"error":error})
            else:
                error = "Invaid form details."
                return render(request, "form.html",{"form":form,"error":error})
        except:
            pass #error
    else:    
        form = sub_categoryForm
        return render(request, 'form.html',{"form":form,"error":error})

def edit_subcategory(request,id):
    error = ""
    if request.method == "POST":
        try:
            form = sub_categoryForm(request.POST, request.FILES)
            if form.is_valid():
                obj = sub_category.objects.get(id=id)
                if form.cleaned_data["title"]:
                    obj.title = form.cleaned_data["title"]
                else:
                    error = "Please enter your title"
                if request.FILES and request.FILES["image"]:
                    error = get_clean_image(request.FILES["image"])
                    obj.image = request.FILES["image"]
                elif not error and not obj.image:
                    error = "Please upload an image."
                if not error and form.cleaned_data["segments"]:
                    obj.save()
                    for val in form.cleaned_data["segments"]:
                        obj.segments.add(val.id)
                if not error:
                    obj.save()
                    messages.info(request, 'Sub category "' + obj.title + '" was changed successfully.')
                    return redirect('/dashboard/sub-categories/')
                else:
                    return render(request, "form.html",{"form":form,"error":error})
            else:
                error = "Invaid form details."
                return render(request, "form.html",{"form":form,"error":error})
        except:
            pass #error
    else:    
        try:
            data = sub_category.objects.get(id=id)
            image = data.image if data.image else ""
            title = data.title if data.title else ""
            segments = data.segments.all() if data.segments else ""
            form = sub_categoryForm(initial={"title":title,"image":image,"segments":segments})
            return render(request, 'form.html',{"form":form,"error":error})
        except:
            pass #error

def new_segment(request):
    error=""
    if request.method == "POST":
        try:
            form = segmentForm(request.POST, request.FILES)
            if form.is_valid():
                obj = segment()
                if form.cleaned_data["title"]:
                    obj.title = form.cleaned_data["title"]
                else:
                    error = "Please enter your title"
                if request.FILES and request.FILES["image"]:
                    error = get_clean_image(request.FILES["image"])
                    obj.image = request.FILES["image"]
                elif not error and not obj.image:
                    error = "Please upload an image."
                if not error:
                    obj.save()
                    messages.info(request, 'Segment "' + obj.title + '" added successfully.')
                    return redirect('/dashboard/segments/')
                else:
                    return render(request, 'form.html',{"form":form,"error":error})
            else:
                error="Invalid form details."
                return render(request, 'form.html',{"form":form,"error":error})       
        except:
            pass #error page     
    else:
        form = segmentForm()
        return render(request, 'form.html',{"form":form,"error":error})

def edit_segment(request,id):
    error=""
    if request.method == "POST":
        try:
            form = segmentForm(request.POST, request.FILES)
            if form.is_valid():
                obj = segment.objects.get(id=id)
                if form.cleaned_data["title"]:
                    obj.title = form.cleaned_data["title"]
                else:
                    error = "Please enter your title"
                if request.FILES and request.FILES["image"]:
                    error = get_clean_image(request.FILES["image"])
                    obj.image = request.FILES["image"]
                elif not error and not obj.image:
                    error = "Please upload an image."
                if not error:
                    obj.save()
                    messages.info(request, 'Segment "' + obj.title + '" was changed successfully.')
                    return redirect('/dashboard/segments/')
                else:
                    return render(request, 'form.html',{"form":form,"error":error})
            else:
                error="Invalid form details."
                return render(request, 'form.html',{"form":form,"error":error})       
        except:
            pass #error page     
    else:
        try:
            data = segment.objects.get(id=id)
            image = data.image if data.image else ""
            title = data.title if data.title else ""
            form = segmentForm(initial={"title":title,"image":image})
            return render(request, 'form.html',{"form":form,"error":error})
        except:
            pass #error

class bannerListview(ListAPIView):
    serializer_class = bannerSerializer
    queryset = banner.objects.all()

class box_bannerListview(ListAPIView):
    serializer_class = box_bannerSerializer
    queryset = box_banner.objects.all()

class mini_bannerListview(ListAPIView):
    serializer_class = mini_bannerSerializer
    queryset = mini_banner.objects.all()