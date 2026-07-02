from django.db import models

class GradeTrack(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    Kannada_mark=models.IntegerField()
    English_mark = models.IntegerField()
    Hindi_mark=models.IntegerField()
    Maths_mark=models.IntegerField()

    @property
    def average(self):
        total = (
            self.Kannada_mark +
            self.English_mark +
            self.Hindi_mark +
            self.Maths_mark
        )
        return total / 4

    @property
    def grade(self):
        avg=self.average

        if avg>=90:
            return "A+"
        elif avg>=75:
            return "A"
        elif avg>=60:
            return "B+"
        elif avg>=50:
            return "B"
        else:
            return "C"


    @property
    def status(self):
        if (self.Kannada_mark>=35 and
            self.English_mark>=35 and
            self.Hindi_mark>=35 and
            self.Maths_mark>=35

            ):
            return "pass"
        else:
            return "Fail"



    def __str__(self):
        return self.name 
