from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Job,Category
from .forms import ApplyForm
def job_list(request):
    job_list = Job.objects.filter().order_by('-puplished_at')
    paginator = Paginator(job_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "jobs": page_obj,
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


