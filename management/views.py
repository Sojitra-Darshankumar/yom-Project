from django.shortcuts import render,redirect
from management.models import admin1,admin1form,slider,sliderform,services,servicesform,blogcategory,blogcategoryform,blog,blogform
from yomapp.models import Contact,comments,Workcategory,Workcategoryform,Work,Workform,Clients,Clientsform
from django.http import HttpResponse
import random
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.



def adminregistration(request):
    msg = ""
    obj = admin1form()
    if 'save' in request.POST:
        obj = admin1form(request.POST,request.FILES)
        if obj.is_valid():
            obj.save()
            msg = "Successfull"
            return redirect('/adminlogin/')
    return render(request,'admin-register-v2.html',{'msg':msg,'frm':obj})

def login(request):
    msg = ""
    if 'login' in request.POST:
        email = request.POST['Email']
        password = request.POST['Password']
        rows = admin1.objects.filter(Email=email,Password=password)
        print(rows.count())
        if rows.count() == 0:
            msg = "Invalid E-Mail Or Password"
        else:
            user = rows.first()
            request.session['adminid'] = user.id
            print(user)
            msg = "Success"
            return redirect("/adminwelcome/")
    return render(request,'admin-login-v2.html',{'msg':msg})

def welcome(request):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    adminid = request.session['adminid']
    info = admin1.objects.filter(id=adminid).get()
    return render(request , 'admin-index.html', {'info':info})

# --------------------------------------------------------------------- Admin ------------

def adminaddregistration(request):
    msg = ""
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    obj = admin1form()
    if 'save' in request.POST:
        obj = admin1form(request.POST,request.FILES)
        obj.save()
        msg = "Successfull"
        return redirect('/admindata/')
    adminid = request.session['adminid']
    info = admin1.objects.filter(id=adminid).get()
    return render(request,'admin-general.html',{'msg':msg ,'info':obj , 'info':info})

def view_admin(request):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    admin = admin1.objects.filter().all()
    print(admin)
    adminid = request.session['adminid']
    info = admin1.objects.filter(id=adminid).get()
    return render(request, 'admin-data.html' , {'info1' : admin , 'info':info}) 

def edit_profile(request,edit_id):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    info=admin1.objects.filter(id=edit_id).get()
    obj=admin1form(instance=info)
    msg=""
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    else:
        if 'save' in request.POST:
            obj=admin1form(request.POST,request.FILES,instance=info)
            if obj.is_valid():
                obj.save()
                msg="data update"
                return redirect("/admindata/")
            print(info)
    return render(request,'admin-general.html',{'edit_profile':info,'msg':msg})

def delete_admin_view(request,del_id):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    admin1.objects.get(id=del_id).delete()
    return redirect('/admindata/')

# --------------------------------------------------------------------- Slider ------------

def adminslider(request):
    msg = ""
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    obj = sliderform()
    if 'save' in request.POST:
        obj = sliderform(request.POST,request.FILES)
        obj.save()
        msg = "Successfull"
        return redirect('/viewslider/')
    adminid = request.session['adminid']
    info = admin1.objects.filter(id=adminid).get()
    return render(request,'admin-add-slider.html',{'msg':msg , 'info':info})

def view_slider(request):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    slider1 = slider.objects.filter().all()
    print(slider1)
    adminid = request.session['adminid']
    info = admin1.objects.filter(id=adminid).get()
    return render(request, 'admin-view-slider.html' , {'slider_detail' : slider1 , 'info':info})

def edit_slider(request,edit_id):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    info=slider.objects.filter(id=edit_id).get()
    obj=sliderform(instance=info)
    msg=""
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    else:
        if 'save' in request.POST:
            obj=sliderform(request.POST,request.FILES,instance=info)
            if obj.is_valid():
                obj.save()
                msg="data update"
                return redirect("/viewslider/")
            print(info)
    return render(request,'admin-add-slider.html',{'edit_Slider':info,'msg':msg})

def delete_slider_view(request,del_id):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    slider.objects.get(id=del_id).delete()
    return redirect('/viewslider/')

# ------------------------------------------------------------------ Services ------------

def adminservices(request):
    msg = ""
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    obj = servicesform()
    if 'save' in request.POST:
        obj = servicesform(request.POST,request.FILES)
        obj.save()
        msg = "Successfull"
        return redirect('/viewservices/')
    adminid = request.session['adminid']
    info = admin1.objects.filter(id=adminid).get()
    return render(request,'admin-add-services.html',{'msg':msg , 'info':info})

def view_services(request):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    services1 = services.objects.filter().all()
    print(services1)
    adminid = request.session['adminid']
    info = admin1.objects.filter(id=adminid).get()
    return render(request, 'admin-view-services.html' , {'services_detail' : services1 , 'info':info})

def edit_services(request,edit_id):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    info=services.objects.filter(id=edit_id).get()
    obj=servicesform(instance=info)
    msg=""
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    else:
        if 'save' in request.POST:
            obj=servicesform(request.POST,request.FILES,instance=info)
            if obj.is_valid():
                obj.save()
                msg="data update"
                return redirect("/viewservices/")
            print(info)
    return render(request,'admin-add-services.html',{'edit_Services':info,'msg':msg})

def delete_services_view(request,del_id):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    services.objects.get(id=del_id).delete()
    return redirect('/viewservices/')

# ------------------------------------------------------------ Blog Category ------------

def adminblogcategory(request):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    msg = ""
    obj = blogcategoryform()
    if 'save' in request.POST:
        obj = blogcategoryform(request.POST,request.FILES)
        obj.save()
        msg = "Successfull"
        return redirect('/viewblogcategory/')
    adminid = request.session['adminid']
    info = admin1.objects.filter(id=adminid).get()
    return render(request,'admin-add-blogcategory.html',{'msg':msg  , 'info':info})

def view_blogcategory(request):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    blogcategory1 = blogcategory.objects.filter().all()
    print(blogcategory1)
    adminid = request.session['adminid']
    info = admin1.objects.filter(id=adminid).get()
    return render(request, 'admin-view-blogcategory.html' , {'blogcategory_deatil' : blogcategory1 , 'info':info})

def edit_blogcategory(request,edit_id):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    info=blogcategory.objects.filter(id=edit_id).get()
    obj=blogcategoryform(instance=info)
    msg=""
    if 'save' in request.POST:
        obj=blogcategoryform(request.POST,request.FILES,instance=info)
        if obj.is_valid():
            obj.save()
            msg="data update"
            return redirect("/viewblogcategory/")
        print(info)
    return render(request,'admin-add-blogcategory.html',{'Blog_Category':info,'msg':msg})

def delete_blogcategory_view(request,del_id):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    blogcategory.objects.get(id=del_id).delete()
    return redirect('/viewblogcategory/')

# ---------------------------------------------------------------------- Blog ------------

def adminblog(request):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    msg = ""
    all_cat = blogcategory.objects.all()
    obj = blogform()
    if 'save' in request.POST:
        obj = blogform(request.POST,request.FILES)
        obj.save()
        msg = "Successfull"
        return redirect('/viewblog/')
    adminid = request.session['adminid']
    info = admin1.objects.filter(id=adminid).get()
    return render(request,'admin-add-blog.html',{'msg':msg , 'info':info , 'all_cats':all_cat})

def view_blog(request):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    blog1 = blog.objects.filter().all()
    blog_category = blogcategory.objects.filter().all()
    print(blog1)
    adminid = request.session['adminid']
    info = admin1.objects.filter(id=adminid).get()
    return render(request, 'admin-view-blog.html' , {'blog_deatil' : blog1 , 'info':info,'blog_category':blog_category})

def edit_blog(request,edit_id):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    adminid = request.session['adminid']
    info2 = admin1.objects.filter(id=adminid).get()
    all_cat = blogcategory.objects.all()
    info=blog.objects.filter(id=edit_id).get()
    cat_id = str(info.Cat_id).strip(" ")
    obj=blogform(instance=info)
    msg=""
    if 'save' in request.POST:
        obj=blogform(request.POST,request.FILES,instance=info)
        if obj.is_valid():
            obj.save()
            msg="data update"
            return redirect("/viewblog/")
        print(info)
    return render(request,'admin-add-blog.html',{'Blog':info,'msg':msg,'all_cats':all_cat,'info2':info2,'cat_id':cat_id})

def delete_blog_view(request,del_id):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    blog.objects.get(id=del_id).delete()
    return redirect('/viewblog/')

#  ------------------------------------------------------------------- Contact ----------

def view_contact(request):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    contact1 = Contact.objects.filter().all()
    print(contact1)
    adminid = request.session['adminid']
    info = admin1.objects.filter(id=adminid).get()
    return render(request, 'admin-view-contact.html' , {'contact_detail' : contact1 , 'info':info})


def view_comment(request):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    comment1 = comments.objects.filter().all()
    print(comment1)
    adminid = request.session['adminid']
    info = admin1.objects.filter(id=adminid).get()
    return render(request, 'admin-view-comment.html' , {'comment_deatil' : comment1 , 'info':info})


# ---------------------------------------------------------- Work Category ------------

def adminworkcategory(request):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    msg = ""
    obj = Workcategoryform()
    if 'save' in request.POST:
        obj = Workcategoryform(request.POST)
        obj.save()
        msg = "Successfull"
        return redirect('/viewworkcategory/')
    adminid = request.session['adminid']
    info = admin1.objects.filter(id=adminid).get()
    return render(request,'admin-add-workcategory.html',{'msg':msg  , 'info':info})

def view_workcategory(request):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    workcategory1 = Workcategory.objects.filter().all()
    print(workcategory1)
    adminid = request.session['adminid']
    info = admin1.objects.filter(id=adminid).get()
    return render(request, 'admin-view-workcategory.html' , {'workcategory_deatil' : workcategory1 , 'info':info})

def edit_workcategory(request,edit_id):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    info=Workcategory.objects.filter(id=edit_id).get()
    obj=Workcategoryform(instance=info)
    msg=""
    if 'save' in request.POST:
        obj=Workcategoryform(request.POST,instance=info)
        if obj.is_valid():
            obj.save()
            msg="data update"
            return redirect("/viewworkcategory/")
        print(info)
    return render(request,'admin-add-workcategory.html',{'Work_Category':info,'msg':msg})

def delete_workcategory_view(request,del_id):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    Workcategory.objects.get(id=del_id).delete()
    return redirect('/viewworkcategory/')


# ------------------------------------------------------------------- Work ------------

def adminwork(request):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    msg=""
    all_work_cat = Workcategory.objects.all()
    obj = Workform()
    if 'save' in request.POST:
        obj = Workform(request.POST,request.FILES)
        if obj.is_valid():
            obj.save()
            msg = "Success"
            return redirect('/viewwork/')
    adminid = request.session['adminid']
    info = admin1.objects.filter(id = adminid).get()
    return render(request,'admin-add-work.html',{'msg':msg,'info':info,'all_work_cat':all_work_cat})


def view_work(request):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    work_category = Workcategory.objects.filter().all()
    Work1 = Work.objects.filter().all()
    print(Work1)
    adminid = request.session['adminid']
    info = admin1.objects.filter(id=adminid).get()
    return render(request, 'admin-view-work.html' , {'work_deatil' : Work1 , 'info':info,'work_category':work_category})

def edit_work(request,edit_id):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    adminid = request.session['adminid']
    info2 = admin1.objects.filter(id=adminid).get()
    all_work_cat = Workcategory.objects.all()
    info=Work.objects.filter(id=edit_id).get()
    cat_id = str(info.Work_Category.Name).strip(" ")
    obj=Workform(instance=info)
    msg=""
    if 'save' in request.POST:
        obj=Workform(request.POST,request.FILES,instance=info)
        if obj.is_valid():
            obj.save()
            msg="data update"
            return redirect("/viewwork/")
        print(info)
    return render(request,'admin-add-work.html',{'Work':info,'msg':msg,'all_work_cat':all_work_cat,'info2':info2,'cat_id':cat_id})

def delete_work_view(request,del_id):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    Work.objects.get(id=del_id).delete()
    return redirect('/viewwork/')

# --------------------------------------------------------------- Clients ------------

def adminclients(request):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    msg=""
    obj = Clientsform()
    if 'save' in request.POST:
        obj = Clientsform(request.POST,request.FILES)
        if obj.is_valid():
            obj.save()
            msg = "Success"
            return redirect('/viewclients/')
    adminid = request.session['adminid']
    info = admin1.objects.filter(id = adminid).get()
    return render(request,'admin-add-clients.html',{'msg':msg,'info':info})


def view_clients(request):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    clients1 = Clients.objects.filter().all()
    print(clients1)
    adminid = request.session['adminid']
    info = admin1.objects.filter(id=adminid).get()
    return render(request, 'admin-view-clients.html' , {'clients_deatil' : clients1 , 'info':info})

def edit_clients(request,edit_id):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    adminid = request.session['adminid']
    info2 = admin1.objects.filter(id=adminid).get()
    info=Clients.objects.filter(id=edit_id).get()
    obj=Clientsform(instance=info)
    msg=""
    if 'save' in request.POST:
        obj=Clientsform(request.POST,request.FILES,instance=info)
        if obj.is_valid():
            obj.save()
            msg="data update"
            return redirect("/viewclients/")
        print(info)
    return render(request,'admin-add-clients.html',{'clients':info,'msg':msg,'info2':info2})

def delete_clients_view(request,del_id):
    if 'adminid' not in request.session:
        return redirect('/adminlogin/')
    Clients.objects.get(id=del_id).delete()
    return redirect('/viewclients/')

# ----------------------------------------------------------- Ajax Search Blog ------------

def ajax_search_blog(request):
    searchkeyword = request.GET['search_blog']
    searchby = request.GET['search_by']
    serchbycategory = request.GET["serch_by_category"]
    if searchby=="Title":
        if serchbycategory!="":
            data = blog.objects.filter(Tital__contains=searchkeyword,Cat_id=serchbycategory).all()
        else:
            data = blog.objects.filter(Tital__contains=searchkeyword).all()
    elif searchby=="id":
        data = blog.objects.filter(id=searchkeyword).all()
    elif searchby=="Cat_id":
        data = blog.objects.filter(Cat_id=searchkeyword).all()
    elif searchby=="Admin_id":
        data = blog.objects.filter(Admin_id=searchkeyword).all()

    htmlData = ''
    for row in data:
        htmlData+= '<tr><td>'+str(row.id)+'</td><td>'+row.Tital+'</td><td>'+row.Description+'</td><td>'+str(row.Cat_id.id)+'</td><td>'+str(row.Admin_id)+'</td><td><img src="'+row.Picture.url+'" alt="" width="70px" height="70px" style="object-fit: cover; border-radius: 20px;"></td><td><a href="/editblog/'+str(row.id)+'"><button type="button" class="btn btn-outline-primary">Edit Profile</button></a><a href="/deleteblog/'+str(row.id)+'""><button type="button" class="btn btn-outline-danger" onclick="return confirm("ARE YOU SURE?")>Delete</button></a></td></tr>'
    return HttpResponse(htmlData)

# -------------------------------------------------- Ajax Search Blog Category ------------

def ajax_search_blog_category(request):
   
    searchbycategory = request.GET['search_by_category']
   
    data = blog.objects.filter(Cat_id_id=searchbycategory).all()

    htmlData = ''
    for row in data:
        htmlData+= '<tr><td>'+str(row.id)+'</td><td>'+row.Tital+'</td><td>'+row.Description+'</td><td>'+str(row.Cat_id)+'</td><td>'+str(row.Admin_id)+'</td><td><img src="'+row.Picture.url+'" alt="" width="70px" height="70px" style="object-fit: cover; border-radius: 20px;"></td><td><a href="/editblog/'+str(row.id)+'"><button type="button" class="btn btn-outline-primary">Edit Profile</button></a><a href="/deleteblog/'+str(row.id)+'""><button type="button" class="btn btn-outline-danger" onclick="return confirm("ARE YOU SURE?")>Delete</button></a></td></tr>'
    return HttpResponse(htmlData)

# ----------------------------------------------------------- Ajax Search Work ------------

def ajax_search_work(request):
    searchkeyword = request.GET['search_work']
    searchby = request.GET['search_by']
    serchbycategory = request.GET["serch_by_category"]
    if searchby=="Name":
        if serchbycategory!="":
            data = Work.objects.filter(Name__contains=searchkeyword,Work_Category=serchbycategory).all()
        else:
            data = Work.objects.filter(Name__contains=searchkeyword).all()
    elif searchby=="id":
        data = Work.objects.filter(id=searchkeyword).all()
    elif searchby=="workcategory":
        data = Work.objects.filter(Work_Category=searchkeyword).all()

    htmlData = ''
    for row in data:
        htmlData+= '<tr><td>'+str(row.id)+'</td><td>'+row.Name+'</td><td>'+row.Description+'</td><td>'+str(row.Work_Category_id)+'</td><td><img src="'+row.Picture.url+'" alt="" width="70px" height="70px" style="object-fit: cover; border-radius: 20px;"></td><td><a href="/editwork/'+str(row.id)+'"><button type="button" class="btn btn-outline-primary">Edit Profile</button></a><a href="/deletework/'+str(row.id)+'""><button type="button" class="btn btn-outline-danger" onclick="return confirm("ARE YOU SURE?")>Delete</button></a></td></tr>'
    return HttpResponse(htmlData)

# -------------------------------------------------- Ajax Search Work Category ------------

def ajax_search_work_category(request):
    searchbycategory= request.GET['search_by_category']
    data = Work.objects.filter(Work_Category_id = searchbycategory).all()
    htmlData = ''
    for row in data:
        htmlData+= '<tr><td>'+str(row.id)+'</td><td>'+row.Name+'</td><td>'+row.Description+'</td><td>'+str(row.Work_Category_id)+'</td><td><img src="'+row.Picture.url+'" alt="" width="70px" height="70px" style="object-fit: cover; border-radius: 20px;"></td><td><a href="/editwork/'+str(row.id)+'"><button type="button" class="btn btn-outline-primary">Edit Profile</button></a><a href="/deletework/'+str(row.id)+'""><button type="button" class="btn btn-outline-danger onclick="return confirm("ARE YOU SURE?") ">Delete</button></a></td></tr>'
    return HttpResponse(htmlData)

def ajax_search_admin(request):
    searchkeyword = request.GET['search_admin']
    searchby = request.GET['search_by']
    if searchby=="Name":
        data = admin1.objects.filter(Name__contains=searchkeyword).all()
    elif searchby=="Email":
        data = admin1.objects.filter(Email__contains=searchkeyword).all()
    elif searchby=="id":
        data = admin1.objects.filter(id=searchkeyword).all()
    elif searchby=="Contact":
        data = admin1.objects.filter(Contact__contains=searchkeyword).all()

    htmlData = ''
    for row in data:
        htmlData+= '<tr><td>'+str(row.id)+'</td><td>'+row.Name+'</td><td>'+row.Email+'</td><td>'+str(row.Password)+'</td><td>'+str(row.Contact)+'</td><td><img src="'+row.Picture.url+'" alt="" width="70px" height="70px" style="object-fit: cover; border-radius: 20px;"></td><td><a href="/editprofile/'+str(row.id)+'"><button type="button" class="btn btn-outline-primary">Edit Profile</button></a><a href="/deleteadmin/'+str(row.id)+'""><button type="button" class="btn btn-outline-danger" onclick="return confirm("ARE YOU SURE?")>Delete</button></a></td></tr>'
    return HttpResponse(htmlData)

# --------------------------------------------------------- Ajax Search Slider ------------

def ajax_search_slider(request):
    searchkeyword = request.GET['search_slider']
    searchby = request.GET['search_by']
    if searchby=="Title":
        data = slider.objects.filter(Tital__contains=searchkeyword).all()
    elif searchby=="id":
        data = slider.objects.filter(id=searchkeyword).all()

    htmlData = ''
    for row in data:
        htmlData+= '<tr><td>'+str(row.id)+'</td><td>'+row.Tital+'</td><td>'+row.Description+'</td><td><img src="'+row.Picture.url+'" alt="" width="70px" height="70px" style="object-fit: cover; border-radius: 20px;"></td><td><a href="/editslider/'+str(row.id)+'"><button type="button" class="btn btn-outline-primary">Edit Profile</button></a><a href="/deleteslider/'+str(row.id)+'""><button type="button" class="btn btn-outline-danger" onclick="return confirm("ARE YOU SURE?")>Delete</button></a></td></tr>'
    return HttpResponse(htmlData)

# ------------------------------------------------------- Ajax Search Services ------------

def ajax_search_service(request):
    searchkeyword = request.GET['search_services']
    searchby = request.GET['search_by']
    if searchby=="Title":
        data = services.objects.filter(Tital__contains=searchkeyword).all()
    elif searchby=="id":
        data = services.objects.filter(id=searchkeyword).all()
    htmlData = ''
    for row in data:
        htmlData+= '<tr><td>'+str(row.id)+'</td><td>'+row.Icon+'</td><td>'+row.Tital+'</td><td>'+row.Description+'</td><td><a href="/editservices/'+str(row.id)+'"><button type="button" class="btn btn-outline-primary">Edit Profile</button></a><a href="/deleteservices/'+str(row.id)+'""><button type="button" class="btn btn-outline-danger" onclick="return confirm("ARE YOU SURE?")>Delete</button></a></td></tr>'
    return HttpResponse(htmlData)

# -------------------------------------------------- Ajax Search BlogCategory ------------

def ajax_search_blogcategory(request):
    searchkeyword = request.GET['search_blogcategory']
    searchby = request.GET['search_by']
    if searchby=="Name":
        data = blogcategory.objects.filter(Name__contains=searchkeyword).all()
    elif searchby=="id":
        data = blogcategory.objects.filter(id=searchkeyword).all()
    htmlData = ''
    for row in data:
        htmlData+= '<tr><td>'+str(row.id)+'</td><td>'+row.Name+'</td><td><a href="/editblogcatrgory/'+str(row.id)+'"><button type="button" class="btn btn-outline-primary">Edit Profile</button></a><a href="/deleteblogcategory/'+str(row.id)+'""><button type="button" class="btn btn-outline-danger" onclick="return confirm("ARE YOU SURE?")>Delete</button></a></td></tr>'
    return HttpResponse(htmlData)

# -------------------------------------------------- Ajax Search WorkCategory ------------

def ajax_search_workcategory(request):
    searchkeyword = request.GET['search_workcategory']
    searchby = request.GET['search_by']
    if searchby=="Name":
        data = Workcategory.objects.filter(Name__contains=searchkeyword).all()
    elif searchby=="id":
        data = Workcategory.objects.filter(id=searchkeyword).all()
    htmlData = ''
    for row in data:
        htmlData+= '<tr><td>'+str(row.id)+'</td><td>'+row.Name+'</td><td><a href="/editworkcatrgory/'+str(row.id)+'"><button type="button" class="btn btn-outline-primary">Edit Profile</button></a><a href="/deleteworkcategory/'+str(row.id)+'""><button type="button" class="btn btn-outline-danger" onclick="return confirm("ARE YOU SURE?")>Delete</button></a></td></tr>'
    return HttpResponse(htmlData)

# -------------------------------------------------------- Ajax Search Clients ------------

def ajax_search_clients(request):
    searchkeyword = request.GET['search_clients']
    searchby = request.GET['search_by']
    if searchby=="Name":
        data = Clients.objects.filter(Name__contains=searchkeyword).all()
    elif searchby=="id":
        data = Clients.objects.filter(id=searchkeyword).all()
    htmlData = ''
    for row in data:
        htmlData+= '<tr><td>'+str(row.id)+'</td><td><img src="'+row.Picture.url+'" alt="" width="70px" height="70px" style="object-fit: cover; border-radius: 20px;"></td><td>'+row.Name+'</td><td>'+row.Link+'</td><td><a href="/editclients/'+str(row.id)+'"><button type="button" class="btn btn-outline-primary">Edit Profile</button></a><a href="/deleteclients/'+str(row.id)+'""><button type="button" class="btn btn-outline-danger" onclick="return confirm("ARE YOU SURE?")>Delete</button></a></td></tr>'
    return HttpResponse(htmlData)

# ------------------------------------------------------- Ajax Search Comments ------------

def ajax_search_comments(request):
    searchkeyword = request.GET['search_comments']
    searchby = request.GET['search_by']
    if searchby=="Name":
        data = comments.objects.filter(Name__contains=searchkeyword).all()
    elif searchby=="Email":
        data = comments.objects.filter(Email__contains=searchkeyword).all()
    elif searchby=="id":
        data = comments.objects.filter(id=searchkeyword).all()
    elif searchby=="Subject":
        data = comments.objects.filter(Subject__contains=searchkeyword).all()
    elif searchby=="Blogid":
        data = comments.objects.filter(Blogid__contains=searchkeyword).all()
    htmlData = ''
    for row in data:
        htmlData+= '<tr><td><img src="'+row.Picture.url+'" alt="" width="70px" height="70px" style="object-fit: cover; border-radius: 20px;"></td><td>'+row.Name+'</td><td>'+row.Email+'</td><td>'+row.Subject+'</td><td>'+row.Comment+'</td><td>'+str(row.Blogid_id)+'</td></tr>'
    return HttpResponse(htmlData)

# -------------------------------------------------------- Ajax Search Contact ------------

def ajax_search_contact(request):
    searchkeyword = request.GET['search_contact']
    searchby = request.GET['search_by']
    if searchby=="Name":
        data = Contact.objects.filter(Name__contains=searchkeyword).all()
    elif searchby=="Email":
        data = Contact.objects.filter(Email__contains=searchkeyword).all()
    elif searchby=="id":
        data = Contact.objects.filter(id=searchkeyword).all()
    elif searchby=="Subject":
        data = Contact.objects.filter(Subject__contains=searchkeyword).all()
    elif searchby=="Message":
        data = Contact.objects.filter(Message__contains=searchkeyword).all()
    htmlData = ''
    for row in data:
        htmlData+= '<tr><td>'+row.Name+'</td><td>'+row.Email+'</td><td>'+row.Subject+'</td><td>'+row.Message+'</td></tr>'
    return HttpResponse(htmlData)

# --------------------------------------------------- Forgot Password By Email ------------

def forgot_password_email(request):
    msg = ""
    if 'Forgot' in request.POST:
        email = request.POST['Email']
        rows = admin1.objects.filter(Email=email)
        print(rows.count())
        if rows.count() == 0:
            msg = "Invalid E-Mail"
        else:
            user = rows.first()
            # request.session[''] = user.id
            otp = random.randint(000000,999999)
            request.session['otp'] = otp
            send_mail(
                    subject="Yom - Request For OTP",
                    message="Hello Dear User You Can Send The Request For Reset Your Password <br>,Your OTP Is : "+str(otp),
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[email]
                )
            request.session['forgotid'] = user.id
            print(user)
            return redirect("/verify_otp/")
    return render(request,'admin-forgot-password.html',{'msg':msg})

# ------------------------------------------------------------------------ Verify OTP ------------

def verify_otp(request):  
    msg=""
    if 'submit' in request.POST:
        user_otp = request.POST['user_otp']
        otp_session = str(request.session['otp'])
        if user_otp == otp_session:
            return redirect('/recover_password/')
        else:
            msg = "invelid OTP" 
    return render(request,'admin-otp-verify.html',{'msg':msg})

# ------------------------------------------------------------------- Recover Password ------------

def recover_password(request):
    msg=""
    if 'save' in request.POST:
        password1 = request.POST['Password']
        con_password = request.POST['Retypepassword']
        user_id = request.session['forgotid']
        if password1 == con_password:  
            info=admin1.objects.filter(id = user_id).get()
            info.Password = password1
            info.Retypepassword = con_password
            info.save()
            msg="data update"
            return redirect("/adminlogin/")
        else:
            msg="Both Password Is Not Match"
    return render(request,'admin-recover-password.html',{'msg':msg})
