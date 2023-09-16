from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.core.mail import send_mail
from blog.forms import EmailSendForm 
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger 


from blog.models import Comment 
from blog.forms import CommentForm 


def post_list_view(request): 
    post_list=Post.objects.all() 
    paginator=Paginator(post_list,2)
    page_number=request.GET.get('page')
    try:
        post_list=paginator.page(page_number)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage: 
        post_list=paginator.page(paginator.num_pages)

    return render(request,'blog/post_list.html',{'post_list':post_list})
     
     
    

     


def post_detail_view(request,name):
    post=Post.objects.filter(status='Published',slug=name)
    comments=Comment.objects.filter(active=True)
    csubmit=False 
    if request.method=='POST': 
        form=CommentForm(data=request.POST) 
        if form.is_valid():
            new_comment=form.save() 
            new_comment.post=post 
            new_comment.save() 
            csubmit=True
    else:
        form=CommentForm() 
    return render(request,'blog/post_detail.html',{'post':post,'form':form,'comments':comments,'csubmit':csubmit})  


def mail_send_view(request,idf): 
    print(idf)
    
    return render(request,'blog/sharebymail.html',) 



# Create your views here.
