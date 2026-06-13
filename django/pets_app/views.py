from django.http import HttpResponse
from .models import Pet

def listPets(request):
    
    # Retrieve all the pets from the database.
    all_pets = Pet.objects.all()
    
    # Build a page that displays the properties of each pet.
    response = HttpResponse()
    response.write("<!doctype html>")
    response.write("<html lang='en'>")
    response.write("<head><title>Pets List</title></head>")
    response.write("<body>")
    response.write("<h1>List of Pets</h1>")
    
    for aPet in all_pets:
        response.write("<p>")
        response.write(f"Pet name: {aPet.name} <br>")
        response.write(f"Gender: {aPet.gender} <br>")
        response.write(f"Owner: {aPet.owner} <br>")
        response.write(f"Birthdate: {aPet.birth:%Y-%m-%d} <br>")
        response.write("</p>")
    
    response.write("</body>")
    response.write("</html>")
    
    # Return the response.
    return response
