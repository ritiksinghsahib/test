from django.db import models


class rassavni_foundation(models.Model):
    rss_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50,default="")
    img=models.ImageField(upload_to="blog/images", default="")
    body=models.TextField(default="")
    draft=models.BooleanField(default=True)
    last=models.DateTimeField(auto_now=True)
    writer=models.CharField(max_length=40,default="")

    def __str__(self):
        return self.title

