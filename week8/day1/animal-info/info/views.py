from django.shortcuts import render

# Create your views here.

def page(request):
    animals= [
        {
            "id" :1,
            "name": "Dog",
            "legs": 4,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 2
        },
        {
            "id": 2,
            "name": "Domestic Cat",
            "legs": 4,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 1
        },
        {
            "id": 3,
            "name": "Panther",
            "legs": 4,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 1 
        },
        {
            "id": 4,
            "name": "Darter",
            "legs": 4,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 5 
        },
        {
            "id": 5,
            "name": "Rabbit",
            "legs": 4,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 3 
        },
        {
            "id": 6,
            "name": "Pig",
            "legs": 4,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 3 
        },
        {
            "id": 7,
            "name": "Monkey",
            "legs": 4,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 3 
        },
        {
            "id": 8,
            "name": "Tiger",
            "legs": 4,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 1 
        },
        {
            "id": 9,
            "name": "Fox",
            "legs": 4,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 2 
        },
        {
            "id": 10,
            "name": "Wolf",
            "legs": 4,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 2 
        },
        {
            "id": 11,
            "name": "Butterfly",
            "legs": 4,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 5 
        },
        {
            "id": 12,
            "name": "Ant",
            "legs": 4,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 5 
        },
        {
            "id": 13,
            "name": "Serpent",
            "legs": 4,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 4 
        },
        {
            "id": 14,
            "name": "Alligator",
            "legs": 4,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 4 
        },
        {
            "id": 15,
            "name": "Crocodile",
            "legs": 4,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 4 
        },
        {
            "id": 16,
            "name": "Spider",
            "legs": 4,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 6 
        },
        {
            "id": 17,
            "name": "Scorpion",
            "legs": 4,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 6 
        },
        {
            "id": 18,
            "name": "Mite",
            "legs": 4,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 6 
        },
        {
            "id": 19,
            "name": "Blindworm",
            "legs": 4,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 7 
        },
        {
            "id": 20,
            "name": "Salamander",
            "legs": 4,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 7 
        },
        {
            "id": 21,
            "name": "Toad",
            "legs": 4,
            "weight": 5.67,
            "height":4.2,
            "speed": 34,
            "family": 7 
        }
    ]

    families= [
        {
            "id": 1,
            "name": "Felidae"
        },
        {
            "id": 2,
            "name": "Caninae"
        },

        {
            "id": 3,
            "name": "Mammal"
        },
        {
            "id": 4,
            "name": "Reptile"
        },
        {
            "id": 5,
            "name": "Insect"
        },
        {
            "id": 6,
            "name": "Arachnid"
        },
        {
            "id": 7,
            "name": "Amphibian"
        }
    ]

    context ={
        'animals': animals,
        'families': families
    }
    
    return render(request, "info/page.html", context)

