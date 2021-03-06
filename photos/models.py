from django.db import models

class Photo(models.Model):
  image = models.ImageField(upload_to="images")
  title = models.CharField(max_length=128, blank=True, null=True)
  description = models.TextField(blank=True, null=True)
  gallery = models.ForeignKey("Gallery")

  def __unicode__(self):
    return self.title

class Gallery(models.Model):
  name = models.CharField(max_length=128)
  description = models.TextField()
  created = models.DateField(auto_now_add=True)
  category = models.ForeignKey('Category')
  
  def date(self):
    return self.created
  
  def __unicode__(self):
    return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)
    slug = models.CharField(max_length=64)
    
    def __unicode__(self):
        return self.name
