from django.db import models

#News table
class News(models.Model):
    title = models.CharField(max_length=255,verbose_name='News Title')
    content = models.TextField(verbose_name='News Content')
    news_date = models.DateField(verbose_name='News Date', auto_now_add=True)
    views_count = models.IntegerField(verbose_name='News Count', default=0)

    def __str__(self):
        return self.title

class Meta:
    db_table = 'news'
    verbose_name = 'News_list'
    ordering = ('id',)


# Members table
class Members(models.Model):
    member_name = models.CharField(max_length=50,verbose_name='Member Name')
    add_date = models.DateField(verbose_name='Add date')
    about_member = models.TextField(verbose_name='About Member')
    member_image = models.ImageField(upload_to='members/', verbose_name='Member Image', blank=True, null=True)

    def __str__(self):
        return self.member_name


class Meta2:
    db_table = 'members'
    verbose_name = 'Members_list'
    ordering = ('id',)

class Users(models.Model):
    full_name = models.CharField(max_length=100,verbose_name='Full Name')
    email = models.EmailField(verbose_name='Email')
    password = models.CharField(max_length=50,verbose_name='Password')
    phone = models.CharField(max_length=10,verbose_name='Phone')


    def __str__(self):
        return self.full_name

class Meta3:
    db_table = 'users'
    verbose_name = 'Users_list'
    ordering = ('id',)