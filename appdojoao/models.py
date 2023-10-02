from django.db import models

class Cups(models.Model):
  year=models.CharField(max_length=50)
  place=models.CharField(max_length=50)
  champion=models.CharField(max_length=50)
  finalists=models.CharField(max_length=50)

class Individual_awards(models.Model):
  year=models.CharField(max_length=50)
  golden_ball=models.CharField(max_length=50)
  golden_boot=models.CharField(max_length=50)
  golden_glove=models.CharField(max_length=50)
  young_player_trophy=models.CharField(max_length=50)
   
  
  
  

