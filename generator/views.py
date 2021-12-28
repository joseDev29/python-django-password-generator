from django.shortcuts import render
import random

# from django.http import HttpResponse

about = lambda request: render(request, "pages/about.html")

home = lambda request: render(request, "pages/home.html")

LOWER_CASE_CHARACTERS = "abcdefghigklmnopqrstuvwxyz"
UPPER_CASE_CHARACTERS = "ABCDEFGHIJKLMNOPRQSTUWWXYZ"
NUMBERS_CHARACTERS = "1234567890"
SPECIAL_CHARACTERS = '!@#$%^&&*()_+}{"<>,.?/'


def password(request):
    # list permite generar una lista a partir del parametro recibido
    characters = list(LOWER_CASE_CHARACTERS)

    add_characters = lambda value: characters.extend(list(value))

    generated_password = ""

    length = int(request.GET.get("length"))
    uppercase = request.GET.get("uppercase") or False
    numbers = True if request.GET.get("numbers") else False
    special = request.GET.get("special")

    if uppercase:
        add_characters(UPPER_CASE_CHARACTERS)

    numbers and characters.extend(list(NUMBERS_CHARACTERS))

    special and add_characters(list(SPECIAL_CHARACTERS))

    for _ in range(length):
        # Choice selecciona elementos de una lista de manera aleatoria
        generated_password += random.choice(characters)

    is_active = lambda value: "Active" if value else "No active"

    return render(
        request,
        "pages/password.html",
        {
            "password": generated_password,
            "length": length,
            "uppercase": is_active(uppercase),
            "special": is_active(special),
            "numbers": is_active(numbers),
        },
    )
