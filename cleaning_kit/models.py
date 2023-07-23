from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File


#this function compress image to reduce its size
def compress(image):
    im = Image.open(image)
    im_io = BytesIO() 
    im.save(im_io, 'JPEG', quality=60) 
    new_image = File(im_io, name=image.name)
    return new_image



class KitCategory(models.Model):
    name=models.CharField(max_length=255)
    desc=models.TextField(blank=True)

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        super(KitCategory,self).save(*args,**kwargs)



class CleaningKit(models.Model):
    name=models.CharField(max_length=255)
    desc=models.TextField(blank=True)
    price=models.FloatField(blank=False)
    image=models.ImageField(upload_to='')
    category=models.ForeignKey(KitCategory,on_delete=models.CASCADE)

    def save(self,*args,**kwargs):
        new_image = compress(self.image)
        self.image = new_image
        super(CleaningKit,self).save(*args,**kwargs)

    
    def __str__(self):
        return self.name



class Order(models.Model):

    PAYMENT_CHOICES=(
        ('B','Bkash'),
        ('R','Rocket'),
        ('N','Nogod'),
        ('U','Upay'),
    )

    ordered_by=models.IntegerField(default=0)
    product_id=models.IntegerField(default=0)
    location=models.CharField(max_length=200,null=False)
    contact=models.CharField(max_length=20,null=False,default='+8801')
    payment_method=models.CharField(max_length=1, choices=PAYMENT_CHOICES)
    transection_no=models.CharField(max_length=200)
    price=models.IntegerField(default=0)
    
    def __str__(self):
        return "paid_by "+self.payment_method

    def save(self,*args,**kwargs):
        super(Order,self).save(*args,**kwargs)


class Notification(models.Model):
    to=models.IntegerField(default=0)
    desc=models.TextField(null=False)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return 'notofication to {}'.format(self.to)

    def save(self,*args,**kwargs):
        super(Notification,self).save(*args,**kwargs)
