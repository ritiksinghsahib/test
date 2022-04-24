from django.db import models


class rassav(models.Model):
    rassav_id= models.AutoField
    rassav_name=models.CharField(max_length=50)
    desc=models.CharField(max_length=250 , default="")
    current_position=models.CharField(max_length=200 , default="")
    image =models.ImageField(upload_to="media",default="")
    back_img=models.ImageField(upload_to="media",default="")

    def __str__(self):
        return self.rassav_name



class aboutme(models.Model):
    about_id=models.AutoField(primary_key=True)
    about_Desc=models.CharField(max_length=350,default="")
    
    def __str__(self):
        return self.about_Desc

class ProfessionalExperience(models.Model):
    ProfessionalExperience_id=models.AutoField(primary_key=True)
    ProfessionalExperience_post=models.CharField(max_length=120, default="")
    ProfessionalExperience_company=models.CharField(max_length=120, default="")
    ProfessionalExperience_description=models.CharField(max_length=350,default="")

    def __str__(self):
        return self.ProfessionalExperience_post


class skill(models.Model):
    skill_id=models.AutoField(primary_key=True)
    skill_name=models.CharField(max_length=350, default="" )

    def __str__(self):
        return self.skill_name


class cert(models.Model):
    cert_id=models.AutoField(primary_key=True)
    cert_names=models.CharField(max_length=120, default="")
    cert_images=models.ImageField(upload_to="media",default="")

    def __str__(self):
        return self.cert_names


class ed_qua(models.Model):
    ed_qua_id=models.AutoField(primary_key=True)
    ed_qua_name=models.CharField(max_length=201,default="")
    ed_qua_descr=models.CharField(max_length=201,default="")

    def __str__(self):
        return self.ed_qua_name

class cop(models.Model):
    cop_id=models.AutoField(primary_key=True)
    cop_name=models.CharField(max_length=65, default="")
    cop_img=models.ImageField(upload_to="media",default="")

    def __str__(self):
        return self.cop_name

class events(models.Model):
    eve_id=models.AutoField(primary_key=True)
    eve_name=models.CharField(max_length=120, default="")
    eve_desc=models.CharField(max_length=620, default="")
    img=models.ImageField( upload_to="media",default="")
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.eve_name


