from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.text import slugify
from home.validators import clean_image

status = [
    ("inreview","In review"),
    ("approved","Approved"),
    ("disapproved","Disapproved")
]
class segment(models.Model):
    title = models.CharField(max_length=26)
    image = models.ImageField(upload_to="subcategories/",validators=[clean_image])
    slug = models.SlugField(editable=False,default='')
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

class sub_category(models.Model):
    title = models.CharField(max_length=26)
    image = models.ImageField(upload_to="subcategories/",validators=[clean_image])
    slug = models.SlugField(editable=False,default='')
    segments = models.ManyToManyField(segment, blank=True)
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

class category(models.Model):
    title = models.CharField(max_length=26)
    image = models.ImageField(upload_to="categories/",validators=[clean_image])
    sub_categories = models.ManyToManyField(sub_category,blank=True)
    slug = models.SlugField(editable=False,default='')
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

class brand(models.Model):
    title = models.CharField(max_length=26)
    image = models.ImageField(upload_to="brands/",validators=[clean_image])
    slug = models.SlugField(editable=False,default='')
    status = models.CharField(choices=status,max_length=15,default="inreview")
    admin_remarks = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        if self.status=="approved":
            self.admin_remarks=""
        super().save(*args, **kwargs)

class specs_list(models.Model):
    key = models.CharField(max_length=26,blank=True,null=True)
    value = models.CharField(max_length=260)
    def __str__(self):
        if self.key:
            return self.key+": "+self.value
        else:
            return self.value

class specification(models.Model):
    title = models.CharField(max_length=26)
    content = models.ManyToManyField(specs_list)
    def __str__(self):
        return self.title

class highlight(models.Model):
    title = models.CharField(max_length=260)
    def __str__(self):
        return self.title

class product(models.Model):
    title = models.CharField(max_length=260)
    slug = models.SlugField(editable=False,default='')
    discount = models.IntegerField(editable=False,default=0)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(sub_category, on_delete=models.CASCADE, blank=True, null=True)
    segment = models.ForeignKey(segment, on_delete=models.CASCADE, blank=True, null=True)
    brand = models.ForeignKey(brand, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=26)
    mrp = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    status = models.CharField(choices=status,max_length=15,default="inreview")
    highlight = models.ManyToManyField(highlight)
    description = models.TextField()
    image = models.ImageField(upload_to="products/",validators=[clean_image])
    image1 = models.ImageField(upload_to="products/",validators=[clean_image])
    specification = models.ManyToManyField(specification)   
    selling_permission = models.BooleanField(default=True) 
    stock = models.PositiveIntegerField()
    admin_remarks = models.TextField(null=True, blank=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True) 
        self.discount = (self.mrp - self.price)/self.mrp*100
        if self.status=="approved":
            self.admin_remarks="" 
        super().save(*args, **kwargs)    
    def __str__(self) -> str:
        return self.title

class offer(models.Model):
    title = models.CharField(max_length=260)
    products = models.ManyToManyField(product)
    slug = models.SlugField(editable=False,default='')
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)    
