from django.shortcuts import render,redirect
from management.views import slider,services,blogcategory,blog
from yomapp.models import comments,commentsform,Contact,Contactform,Workcategory,Work,Clients
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
import random

# Create your views here.

# ---------------------------------------------------------------------- Index ------------

def index(request):
    slider1 = slider.objects.filter().all()
    services1 = services.objects.order_by('-id')[:3].all()
    blogcategory1 = blogcategory.objects.filter().all()
    workcategory1 = Workcategory.objects.filter().all()
    blog1 = blog.objects.order_by('-id')[:3].all()
    comment1 = comments.objects.order_by('-id')[:9].all()
    blog5 = blog.objects.order_by('-id')[:5].all()
    Work8 = Work.objects.order_by('-id')[:8].all()
    blogcategory1 = blogcategory.objects.filter().all()
    return render(request, 'index.html' , {'slider_detail' : slider1 , 'services_detail' : services1 , 'blogcategory_detail' : blogcategory1 , 'blog_detail' : blog1 ,'blog5_detail':blog5,'comment_detail':comment1,'workcategory_detail':workcategory1,'work8':Work8})

# ---------------------------------------------------------------------- About ------------

def about(request):
    blog5 = blog.objects.order_by('-id')[:5].all()
    blogcategory1 = blogcategory.objects.filter().all()
    workcategory1 = Workcategory.objects.filter().all()
    clients1 = Clients.objects.filter().all()
    comment1 = comments.objects.order_by('-id')[:9].all()
    return render(request,'about.html',{'blogcategory_detail' : blogcategory1  ,'blog5_detail':blog5,'workcategory_detail':workcategory1,'clients_detail':clients1,'comment_detail':comment1})

# ----------------------------------------------------------------------- Blog ------------

def blog1(request,Cat_id):
    blog2 = blog.objects.filter(Cat_id_id=Cat_id).all()
    blog5 = blog.objects.order_by('-id')[:5].all()
    blogcategory1 = blogcategory.objects.filter().all()
    workcategory1 = Workcategory.objects.filter().all()
    return render(request,'blog.html',{'blogcategory_detail' : blogcategory1 , 'blog2':blog2 ,'blog5_detail':blog5,'workcategory_detail':workcategory1})

# ------------------------------------------------------------------ Blog Grid ------------

def bloggrid(request):
    blog5 = blog.objects.order_by('-id')[:5].all()
    blog_all = blog.objects.filter().all()
    blogcategory1 = blogcategory.objects.filter().all()
    workcategory1 = Workcategory.objects.filter().all()
    return render(request,'blog-grid.html',{'blogcategory_detail' : blogcategory1  ,'blog5_detail':blog5,'workcategory_detail':workcategory1,'blog_all':blog_all})

# ---------------------------------------------------------------- Blog Single ------------

def blogsingle(request,Blog_id):
    blog_show = blog.objects.filter(id=Blog_id).get()
    blog_comment = comments.objects.filter(Blogid_id = Blog_id).all()
    workcategory1 = Workcategory.objects.filter().all()
    blog5 = blog.objects.order_by('-id')[:5].all()
    blog1 = blog.objects.order_by('-id')[:3].all()
    blogsearch = blog.objects.filter(Tital__contains = "F").all()
    blogcategory1 = blogcategory.objects.filter().all()
    obj = commentsform()
    if 'save' in request.POST:
        obj = commentsform(request.POST,request.FILES)
        if obj.is_valid():
            obj.save()
            msg = "Successfull"
    return render(request,'blog-single.html',{'blogcategory_detail' : blogcategory1 ,'blog_show':blog_show ,'blog_detail':blog1,'Comments_detail':blog_comment ,'blog5_detail':blog5,'workcategory_detail':workcategory1})

# -------------------------------------------------------------------- Clients ------------

def clients(request):
    blog5 = blog.objects.order_by('-id')[:5].all()
    blogcategory1 = blogcategory.objects.filter().all()
    clients1 = Clients.objects.filter().all()
    workcategory1 = Workcategory.objects.filter().all()
    return render(request,'clients.html',{'blogcategory_detail' : blogcategory1  ,'blog5_detail':blog5,'workcategory_detail':workcategory1,'clients_detail':clients1})

# -------------------------------------------------------------------- Contact ------------

def contact1(request):
    blog5 = blog.objects.order_by('-id')[:5].all()
    blogcategory1 = blogcategory.objects.filter().all()
    workcategory1 = Workcategory.objects.filter().all()
    contact1 = Contact.objects.filter().all()
    obj = Contactform()
    if 'save' in request.POST:
        obj = Contactform(request.POST)
        if obj.is_valid():
            obj.save()
            msg = "Successfull"
            return redirect('/contact/')
    return render(request,'contact.html',{'blogcategory_detail' : blogcategory1 ,'contact_detail' :contact1 ,'blog5_detail':blog5,'workcategory_detail':workcategory1 })

# ------------------------------------------------------------------- Services ------------

def services1(request):
    blog5 = blog.objects.order_by('-id')[:5].all()
    services2 = services.objects.filter().all()
    workcategory1 = Workcategory.objects.filter().all()
    blogcategory1 = blogcategory.objects.filter().all()
    return render(request,'services.html',{'blogcategory_detail' : blogcategory1 ,'services_detail':services2 ,'blog5_detail':blog5,'workcategory_detail':workcategory1})

# ------------------------------------------------------------- Single Project ------------

def singleproject(request):
    blog5 = blog.objects.order_by('-id')[:5].all()
    workcategory1 = Workcategory.objects.filter().all()
    blogcategory1 = blogcategory.objects.filter().all()
    return render(request,'single-project.html',{'blogcategory_detail' : blogcategory1 ,'blog5_detail':blog5,'workcategory_detail':workcategory1})

# ------------------------------------------------------------- Work 3 Columns ------------

def work3columns(request):
    blog5 = blog.objects.order_by('-id')[:5].all()
    workcategory1 = Workcategory.objects.filter().all()
    Work1 = Work.objects.filter().all()
    blogcategory1 = blogcategory.objects.filter().all()
    return render(request,'work-3columns.html',{'blogcategory_detail' : blogcategory1 ,'blog5_detail':blog5,'workcategory_detail':workcategory1,'Work_detail':Work1 })

# ------------------------------------------------------------- Work 4 Columns ------------

def work4columns(request):
    blog5 = blog.objects.order_by('-id')[:5].all()
    workcategory1 = Workcategory.objects.filter().all()
    blogcategory1 = blogcategory.objects.filter().all()
    Work1 = Work.objects.filter().all()
    return render(request,'work-4columns.html',{'blogcategory_detail' : blogcategory1 ,'blog5_detail':blog5,'workcategory_detail':workcategory1,'Work_detail':Work1})

# --------------------------------------------------------------------- Search ------------

def search(request):
    search_word = request.GET['keyword']
    blogsearch = blog.objects.filter(Tital__contains = search_word).all()
    blog5 = blog.objects.order_by('-id')[:5].all()
    workcategory1 = Workcategory.objects.filter().all()
    blogcategory1 = blogcategory.objects.filter().all()
    Work1 = Work.objects.filter().all()
    return render(request,'search.html',{'blogcategory_detail' : blogcategory1 ,'blog5_detail':blog5,'workcategory_detail':workcategory1,'Work_detail':Work1,'Blog_Search':blogsearch})

# ------------------------------------------------------------------- Comments ------------

def view_comment(request):
    slider1 = comments.objects.filter().all()
    print(slider1)
    return render(request, 'comment_view.html' , {'Comments_view' : slider1 })

def delete_comment_view(request,del_id):
    comments.objects.get(id=del_id).delete()
    return redirect('/commentview/')

# -------------------------------------------------------------------- Contact ------------

def view_contact(request):
    slider1 = Contact.objects.filter().all()
    print(slider1)
    return render(request, 'comment_view.html' , {'Comments_view' : slider1 })

def delete_contact_view(request,del_id):
    Contact.objects.get(id=del_id).delete()
    return redirect('/contact/')

# ---------------------------------------------------- Ajax Search Blog Single ------------

def ajax_search_blogsingle(request):
    searchkeyword = request.GET['search_blogcategory']
    data = blog.objects.filter(Tital__contains=searchkeyword).all()
    htmlData = ''
    for row in data:
        htmlData+= '<div class="col-md-4"><div class="blog-item"><a href="/blogsingle/'+str(row.id)+'"><img src="'+row.Picture.url+'" alt=""/></a><h3><a href="/blogsingle/'+str(row.id)+'">'+row.Tital+'</a></h3><span><a href="/blogsingle/'+str(row.id)+'">'+str(row.Cat_id)+'</a></span><p>'+row.Description+'...</p><div class="read-more"><a href="/blogsingle/'+str(row.id)+'">Read more</a></div></div></div>'
    return HttpResponse(htmlData)

# ----------------------------------------------------------------- Send Email ------------

def send_email(request):
    otp = random.randint(000000,99999)
    send_mail(
            subject="Darshna Sojitra",
            message="Hello User"+str(otp),
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=["sojitradarshan94@gmail.com"]
        )
    return HttpResponse("Email Sent"+str(otp))

