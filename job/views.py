from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from .models import Job,Category
from .forms import ApplyForm,JobForm
from django.urls  import reverse
from django.contrib.auth.decorators import login_required
from .filter import JobFilter

def job_list(request):
    job_list = Job.objects.filter().order_by('-puplished_at')
    filter = JobFilter(request.GET, queryset=job_list)
    job_list=filter.qs
    paginator = Paginator(job_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "jobs": page_obj,
        "filter":filter,
    }
    return render(request,"job_list.html",context)


def job_detail(request,slug):
    job_detail = Job.objects.get(slug=slug)
    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detail
            myform.save()
            

    else:
        form = ApplyForm()

    context = {
        'job_detail': job_detail,
        "form": form,
    }
    return render(request, "job_detail.html", context)

@login_required
def add_job(request):
    if request.method=="POST":
        form=JobForm(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.owner=request.user
            myform.save()
            return redirect(reverse('job_list'))

    else:
        form=JobForm()
    context={
        'form':form,
    }
    return render(request,'add_job.html',context)
