from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=250)
    def __str__(self):
        return self.name


def image_upload(instance, filename):
    imagename, extension = filename.split(".")
    return "jobs/%s/%s.%s" % (instance.id, instance.id, extension)

class Job(models.Model):
    JOB_TYPE=(
        ('Full Time','Full Time'),
        ('Part Time','Part Time'),
    )
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    title       =models.CharField(max_length=1000)
    job_type    =models.CharField(max_length=30,choices=JOB_TYPE)
    description=models.TextField(max_length=1000)
    puplished_at=models.DateTimeField(auto_now_add=True)
    vecancy=models.IntegerField(default=1)
    salary=models.IntegerField(default=0)
    experience=models.IntegerField(default=1)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to=image_upload)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Apply(models.Model):
        job = models.ForeignKey(Job, on_delete=models.CASCADE)
        name = models.CharField(max_length=50)
        email = models.EmailField(max_length=50)
        website = models.URLField()
        upload_cv = models.FileField(upload_to="apply/")
        message = models.TextField(max_length=1000)

        def __str__(self):
            return self.name