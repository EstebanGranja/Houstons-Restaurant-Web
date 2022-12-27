from django.db import models

# Create your models here.


# ------- Custom uploads to (delete old images) --------------------------

def about_upload_to(instance, filename):
    try:
        old_instance = About.objects.get(pk=instance.pk)
        old_instance.image.delete()
        return 'about/' + filename
    except:
        return 'about/' + filename


def special1_upload_to(instance, filename):
    try:
        old_instance = Special.objects.get(pk=instance.pk)
        old_instance.image1.delete()
        return 'specials/' + filename
    except:
        return 'specials/' + filename

def special2_upload_to(instance, filename):
    try:
        old_instance = Special.objects.get(pk=instance.pk)
        old_instance.image2.delete()
        return 'specials/' + filename
    except:
        return 'specials/' + filename

def special3_upload_to(instance, filename):
    try:
        old_instance = Special.objects.get(pk=instance.pk)
        old_instance.image3.delete()
        return 'specials/' + filename
    except:
        return 'specials/' + filename

def special4_upload_to(instance, filename):
    try:
        old_instance = Special.objects.get(pk=instance.pk)
        old_instance.image4.delete()
        return 'specials/' + filename
    except:
        return 'specials/' + filename

def special5_upload_to(instance, filename):
    try:
        old_instance = Special.objects.get(pk=instance.pk)
        old_instance.image5.delete()
        return 'specials/' + filename
    except:
        return 'specials/' + filename


def staff_upload_to(instance, filename):
    try:
        old_instance = Staff.objects.get(pk=instance.pk)
        old_instance.photo.delete()
        return 'staff/' + filename
    except:
        return 'staff/' + filename


def event_upload_to(instance, filename):
    try:
        old_instance = Event.objects.get(pk=instance.pk)
        old_instance.event_image.delete()
        return 'events/' + filename
    except:
        return 'events/' + filename


def testimonial_upload_to(instance, filename):
    try:
        old_instance = Testimonial.objects.get(pk=instance.pk)
        old_instance.photo.delete()
        return 'testimonials/' + filename
    except:
        return 'testimonials/' + filename


def gallery_upload_to(instance, filename):
    try:
        old_instance = Gallery.objects.get(pk=instance.pk)
        old_instance.image.delete()
        return 'gallery/' + filename
    except:
        return 'gallery/' + filename



#----------------------------------------------------------------------


#----------------------- About ------------------------------------------

class About(models.Model):
    video = models.URLField(max_length=200)
    headline = models.CharField(max_length=200, verbose_name='About section headline')
    subtitle = models.TextField()
    tick1 = models.CharField(max_length=300, verbose_name='Tick 1')
    tick2 = models.CharField(max_length=300, verbose_name='Tick 2')
    tick3 = models.CharField(max_length=300, verbose_name='Tick 3')
    content = models.TextField()
    image = models.ImageField(null=True, upload_to=about_upload_to)
    created = models.DateTimeField(null=True, auto_now_add=True)

    class Meta():
        verbose_name_plural = 'About'
    
    def __str__(self):
        return 'About Section'



#------------------ Why us section -----------------------------------------

class WhyUs(models.Model):
    number = models.IntegerField(default=0)
    short_title = models.CharField(null=True, max_length=30)
    reason = models.TextField()
    created = models.DateTimeField(null=True, auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Why us'
        ordering = ['number']

    def __str__(self):
        return str(self.number)



#------------------ Specials -----------------------------------------------

class Special(models.Model):
    special1 = models.CharField(default='Special 1', max_length=50, verbose_name='Special 1')
    description1 = models.TextField()
    image1 = models.ImageField(null=True, upload_to=special1_upload_to, verbose_name='Image Special 1')

    special2 = models.CharField(default='Special 2',max_length=50, verbose_name='Special 2')
    description2 = models.TextField()
    image2 = models.ImageField(null=True,upload_to=special2_upload_to, verbose_name='Image Special 2')

    special3 = models.CharField(default='Special 3', max_length=50, verbose_name='Special 3')
    description3 = models.TextField(null=True)
    image3 = models.ImageField(null=True,upload_to=special3_upload_to, verbose_name='Image Special 3')

    special4 = models.CharField(blank=True, null=True, max_length=50, verbose_name='Special 4 (optional)')
    description4 = models.TextField(blank=True, null=True)
    image4 = models.ImageField(null=True, blank=True,upload_to=special4_upload_to, verbose_name='Image Special 4')

    special5 = models.CharField(blank=True, null=True, max_length=50, verbose_name='Special 5 (optional)')
    description5 = models.TextField(blank=True, null=True)
    image5 = models.ImageField(null=True, blank=True, upload_to=special5_upload_to, verbose_name='Image Special 5')


    def __str__(self):
        return 'Specials'



#------------------ Events -----------------------------------------------

class Event(models.Model):
    event_name = models.CharField(max_length=100, verbose_name='Event name')
    price = models.IntegerField(verbose_name='Price (USD)')
    long_description = models.TextField(verbose_name='Long description')
    event_image = models.ImageField(verbose_name='Event image', upload_to=event_upload_to)
    created = models.DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
        return self.event_name

    class Meta:
        ordering = ['price']



#------------------ Testimonials -----------------------------------------------

class Testimonial(models.Model):
    name = models.CharField(max_length=30, verbose_name='Full name')
    job = models.CharField(max_length=30, verbose_name='Actual position / Job')
    photo = models.ImageField(upload_to=testimonial_upload_to, null=True, blank=True)
    testimonial = models.TextField()
    created = models.DateTimeField(null=True, auto_now_add=True)



#------------------ Staff  -----------------------------------------------------

class Staff(models.Model):
    name = models.CharField(max_length=100, verbose_name='Staff member name')
    position = models.CharField(max_length=100)
    twitter = models.URLField(verbose_name='Twitter link')
    facebook = models.URLField(blank=True, null=True, verbose_name='Facebook link')
    instagram = models.URLField(blank=True, null=True, verbose_name='Instagram link')
    photo = models.ImageField(blank=True, null=True, verbose_name='Employee photo', upload_to=staff_upload_to, 
            help_text='600x600px approximately images recomended')
    created = models.DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Staff'



#------------------ Gallery  -------------------------------------------------

class Gallery(models.Model):
    image = models.ImageField(upload_to=gallery_upload_to)
    order = models.PositiveSmallIntegerField(default=1, verbose_name='Image order')
    created = models.DateTimeField(null=True, auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Gallery'
        ordering = ['order']
     
    

#------------------ Contact --------------------------------------------------

class Contact(models.Model):
    address = models.CharField(max_length=70)
    city = models.CharField(max_length=70, verbose_name='City / Location')
    google = models.URLField(blank=True, null=True, verbose_name='Google Maps link')
    opentime = models.CharField(max_length=50, verbose_name='Open hours')
    email = models.EmailField(max_length=50)
    number = models.CharField(max_length=30, verbose_name='Phone number')
    tw = models.URLField(blank=True, null=True, verbose_name='Twitter link')
    face = models.URLField(blank=True, null=True, verbose_name='Facebook link')
    insta = models.URLField(blank=True, null=True, verbose_name='Instagram link')
    created = models.DateTimeField(null=True, auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Contact'

    def __str__(self):
        return 'Contact Section'
