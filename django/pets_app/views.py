from .models import Pet, VetVisit
from django.shortcuts import render
from datetime import datetime

# New view 
def pet(request, pet_id):
    # 1 - prepare application data in a context dict
    context = {"pet": Pet.objects.filter(id=pet_id).first()}

    # 2-3-4 - load template, render it and return the HTTP response
    return render(request, "pets_app/pet.html", context)

def listPets(request):
    context = {
        'pets': Pet.objects.all()
    }

    return render(request, "pets_app/pets.html", context)

def visit(request, pet_id, vaccine):
    pet = Pet.objects.filter(id=pet_id).first()
    lastvisit = pet.vetvisit_set.last()
    
    vet = "Unknown"
    if lastvisit:
        vet = lastvisit.vet
        
    today = datetime.today().date()
    already_vaccinated_today = pet.vetvisit_set.filter(date=today, notes=f"{vaccine} vaccination").exists()
    if not already_vaccinated_today:
        VetVisit(pet=pet, vet=vet, date=today, notes=f"{vaccine} vaccination").save()
        setattr(pet.card, vaccine, today)
        pet.card.save()
    context = {'pet': pet}
    return render(request, "pets_app/pet.html", context)