from django.db import models

# Create your models here.

class homeimgcls(models.Model):
    img1=models.ImageField(upload_to="imghome1",default=1,verbose_name="عکس1 صفحه خانه")
    img2=models.ImageField(upload_to="imghome2",default=2,verbose_name="عکس2 صفحه خانه")

class shopcls(models.Model):
    name=models.CharField(max_length=50,verbose_name="نام مغازه")
    address=models.CharField(max_length=300,verbose_name="آدرس")
    type_shop=models.CharField(max_length=50,verbose_name="نوع مغازه")
    picture=models.ImageField(upload_to="imgs1",verbose_name=" عکس صفحه اطلاعات")
    icone=models.ImageField(upload_to="imgs2",verbose_name="عکس صفحه فروشگاه ها")
    phone=models.CharField(max_length=20,verbose_name="تلفن")
    description=models.CharField(max_length=3000,verbose_name="توضیحات")
    phase=models.IntegerField(default=2,verbose_name="کتگری فاز")
    
    
    def __str__(self) :
        return self.name
    
class contactcls(models.Model):
    name=models.CharField(max_length=40,verbose_name="نام") 
    email=models.CharField(max_length=50,verbose_name="ایمیل")
    subject=models.CharField(max_length=200,verbose_name="موضوع")
    message=models.CharField(max_length=500,verbose_name="پیام")  

    def __str__(self) :
        return self.subject
    
class blogcls(models.Model):
    blog_pic=models.ImageField(upload_to="imgs3",verbose_name="عکس خبر")
    blog_title=models.CharField(max_length=100,verbose_name="عنوان خبر")
    blog_desc=models.CharField(max_length=3000,verbose_name="توضیحات خبر") 

    def __str__(self) :
        return self.blog_title

class officecls(models.Model):
    off_name=models.CharField(max_length=50,verbose_name="نام ادراه")
    off_pic=models.ImageField(upload_to="imgs4",verbose_name="عکس")
    off_web=models.CharField(max_length=50,verbose_name="آدرس وب") 

    def __str__(self) :
        return self.off_name   

class servicescls(models.Model):
    serv_name=models.CharField(max_length=50,verbose_name="نام خدمات")
    serv_pic=models.ImageField(upload_to="imgs5",verbose_name="عکس")
    serv_desc=models.CharField(max_length=2000,verbose_name="توضیحات خدمات")

    def __str__(self) :
        return self.serv_name
    
class aboutcls(models.Model):
    ab_title=models.CharField(max_length=100,verbose_name="عنوان درباره ما")
    ab_pic=models.ImageField(upload_to="imgs6",verbose_name="عکس") 
    ab_desc=models.CharField(max_length=3000,verbose_name="توضیحات درباره ما")

    def __str__(self) :
        return self.ab_title   
