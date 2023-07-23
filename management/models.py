from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File
from django.db.models.signals import pre_save, post_save

from .utils import unique_slug_generator

#this function compress image to reduce its size
def compress(image):
    im = Image.open(image)
    im_io = BytesIO() 
    im.save(im_io, 'JPEG', quality=60) 
    new_image = File(im_io, name=image.name)
    return new_image


class Cleaner(models.Model):
    name=models.CharField(max_length=255,blank=False)
    desc=models.TextField(blank=True)
    cleaning_task=models.CharField(max_length=255)
    contact=models.CharField(max_length=255,blank=False)
    price=models.FloatField(blank=False,default=0.00)
    address=models.TextField(blank=False)
    image=models.ImageField(upload_to='')
    class Meta:
        verbose_name_plural = "Cleaners"
    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        new_image = compress(self.image)
        self.image = new_image
        super(Cleaner,self).save(*args,**kwargs)



class GarbageCategory(models.Model):
    name=models.CharField(max_length=255,blank=False)
    desc=models.TextField(blank=True)
    status=models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Categories"


    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name



class Garbage(models.Model):

    name=models.CharField(max_length=255,blank=False)
    desc=models.TextField(blank=False)
    status=models.BooleanField(default=False)
    weight=models.PositiveIntegerField(blank=True) 
    image=models.ImageField(upload_to='')
    categoy=models.ForeignKey(GarbageCategory,on_delete=models.CASCADE)
    slug=models.SlugField(blank=True,unique=True)
    uploaded_by=models.IntegerField(default=0)

    #calling image compression function before saving the data
    def save(self, *args, **kwargs):
        new_image = compress(self.image)
        self.image = new_image
        super(Garbage,self).save(*args, **kwargs)

    
    def __str__(self):
        return "{}".format(self.name)
    

class GarbageOrder(models.Model):
    ordered_by=models.IntegerField(blank=False)
    ordered_garbage=models.ForeignKey(Garbage,on_delete=models.CASCADE)

    def __str__(self):

        return "order by {}".format(self.ordered_by)


    
def garbage_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(garbage_pre_save_receiver, sender=Garbage)