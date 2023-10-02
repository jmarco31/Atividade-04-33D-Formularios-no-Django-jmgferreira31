from django.shortcuts import render, redirect
from .models import Cups, Individual_awards

# Create your views here.
def home(request):
  cups=Cups.objects.all()
  ind_awards=Individual_awards.objects.all()
  return render(request, "home.html", context={
    "cups": cups,
    "ind_awards": ind_awards
    
  })

def create_cup(request):
  if request.method == "POST":
    Cups.objects.create(
      year = request.POST["year"],
      place = request.POST["place"],
      champion = request.POST["champion"],
      finalists = request.POST["finalists"]
    )
    
    return redirect("home")
  return render(request, "forms.html", context={"action": "Adicionar"})

def update_cup(request, id):
  cup = Cups.objects.get(id = id)
  if request.method == "POST":
    cup.year = request.POST["year"]
    cup.place = request.POST["place"]
    cup.champion = request.POST["champion"]
    cup.finalists = request.POST["finalists"]
    cup.save()

    return redirect("home")
  return render(request, "forms.html", context={"action": "Atualizar","cup": cup})

def delete_cup(request, id):
  cup = Cups.objects.get(id = id)
  if request.method == "POST":
    if "confirm" in request.POST:
      cup.delete()

    return redirect("home")
  return render(request, "are_you_sure.html", context={"cup": cup})

def create_ind_award(request):
  if request.method == "POST":
    Individual_awards.objects.create(
      year = request.POST["year"],
      golden_ball = request.POST["golden_ball"],
      golden_boot = request.POST["golden_boot"],
      golden_glove = request.POST["golden_glove"],
      young_player_trophy = request.POST["young_player_trophy"]
    )
    
    return redirect("home")
  return render(request, "forms2.html", context={"action": "Adicionar"})

def update_ind_award(request, id):
  ind_award = Individual_awards.objects.get(id = id)
  if request.method == "POST":
    ind_award.year = request.POST["year"]
    ind_award.golden_ball = request.POST["golden_ball"]
    ind_award.golden_boot = request.POST["golden_boot"]
    ind_award.golden_glove = request.POST["golden_glove"]
    ind_award.young_player_trophy = request.POST["young_player_trophy"]
    ind_award.save()

    return redirect("home")
  return render(request, "forms2.html", context={"action": "Atualizar","ind_award": ind_award})

def delete_ind_award(request, id):
  ind_award = Individual_awards.objects.get(id = id)
  if request.method == "POST":
    if "confirm" in request.POST:
      ind_award.delete()

    return redirect("home")
  return render(request, "are_you_sure2.html", context={"ind_award": ind_award})
