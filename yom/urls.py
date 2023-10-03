"""
URL configuration for yom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from yomapp.views import *
from management.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('bloggrid/', bloggrid),
    path('blogsingle/<int:Blog_id>', blogsingle),
    path('about/', about),
    path('blog/<int:Cat_id>', blog1),
    path('clients/', clients),
    path('contact/', contact1),
    path('services/', services1),
    path('singleproject/', singleproject),
    path('work3columns/', work3columns),
    path('work4columns/', work4columns),
    path('search/', search),
    path('delete_comment/<int:del_id>',delete_comment_view),
    path('contactview/', view_contact),
    path('delete_contact/<int:del_id>',delete_contact_view),
    path('ajax_search_blog/',ajax_search_blog),
    path('ajax_search_work/',ajax_search_work),
    path('ajax_search_admin/',ajax_search_admin),
    path('ajax_search_slider/',ajax_search_slider),
    path('ajax_search_services/',ajax_search_service),
    path('ajax_search_blogcategory/',ajax_search_blogcategory),
    path('ajax_search_workcategory/',ajax_search_workcategory),
    path('ajax_search_clients/',ajax_search_clients),
    path('ajax_search_comments/',ajax_search_comments),
    path('ajax_search_contact/',ajax_search_contact),
    path('ajax_search_blogsingle/',ajax_search_blogsingle),
    path('ajax_search_blog_category/',ajax_search_blog_category),
    path('ajax_search_work_category/',ajax_search_work_category),
    path('email_sent/',send_email),
    path('recover_password/',recover_password),
    path('forgot_password_email/',forgot_password_email),
    path('verify_otp/',verify_otp),


# ----------------------- admin ---------------------------

    path('adminregisteration/', adminregistration),
    path('adminlogin/', login),
    path('adminwelcome/', welcome),

    path('admindata/', view_admin),
    path('admingenerl/', adminaddregistration),
    path('editprofile/<int:edit_id>', edit_profile),
    path('deleteadmin/<int:del_id>', delete_admin_view),

    path('viewslider/', view_slider),
    path('adminaddslider/', adminslider),
    path('editslider/<int:edit_id>', edit_slider),
    path('deleteslider/<int:del_id>', delete_slider_view),

    path('viewservices/', view_services),
    path('adminaddservices/', adminservices),
    path('editservices/<int:edit_id>', edit_services),
    path('deleteservices/<int:del_id>', delete_services_view),

    path('viewblogcategory/', view_blogcategory),
    path('adminaddblogcategory/', adminblogcategory),
    path('editblogcategory/<int:edit_id>', edit_blogcategory),
    path('deleteblogcategory/<int:del_id>', delete_blogcategory_view),

    path('viewblog/', view_blog),
    path('adminaddblog/', adminblog),
    path('editblog/<int:edit_id>', edit_blog),
    path('deleteblog/<int:del_id>', delete_blog_view),

    path('viewcontact/', view_contact),
    path('viewcomment/', view_comment),

    path('viewworkcategory/', view_workcategory),
    path('adminaddworkcategory/', adminworkcategory),
    path('editworkcategory/<int:edit_id>', edit_workcategory),
    path('deleteworkcategory/<int:del_id>', delete_workcategory_view),

    
    path('viewwork/', view_work),
    path('adminaddwork/', adminwork),
    path('editwork/<int:edit_id>', edit_work),
    path('deletework/<int:del_id>', delete_work_view),

    path('viewclients/', view_clients),
    path('adminaddclients/', adminclients),
    path('editclients/<int:edit_id>', edit_clients),
    path('deleteclients/<int:del_id>', delete_clients_view),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
