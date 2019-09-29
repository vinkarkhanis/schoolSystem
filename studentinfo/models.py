from django.db import models




class Fees(models.Model):
    std = models.IntegerField()
    fees = models.FloatField()
    def __str__(self):
        return  "Std: "+str(self.std) + ' = ' + "₹"+str(self.fees)+"/-"

    class Meta:
        verbose_name_plural = "Fees"

class Student(models.Model):
    rollNum = models.IntegerField()
    name = models.TextField()
    gender = models.CharField(max_length=10)
    address = models.TextField()
    std = models.IntegerField()
    div = models.TextField()
    religion = models.TextField()
    cast = models.TextField()
    category = models.TextField()
    fees=models.FloatField(blank=True, null=True)

    def __str__(self):
        return  "Name - "+self.name+" --> "+"Class - "+str(self.std)+":"+self.div



