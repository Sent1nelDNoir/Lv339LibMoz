from django.db import models


# Create your models here.

class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)

    def __str__(self):
        return "{}, {}, {}".format(self.id,self.fname, self.lname)


    # here we enforce the name of the database(Table) to the one we like

    class Meta:
        db_table = 'Users'


class Books(models.Model):
    id = models.IntegerField(primary_key=True)
    author = models.CharField(max_length=50)
    name = models.CharField(max_length=100)

    def __str__(self):
        return "{}, {}, {}".format(self.id,self.author, self.name)

    class Meta:
        db_table = 'Books'


class Borrowed(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Books, on_delete=models.CASCADE)

    def __str__(self):
        return '{}, {}'.format(self.book_id, self.user_id)

    class Meta:
        db_table = 'Borrowed'





