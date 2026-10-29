from django.shortcuts import render
import re

def password(request):
    msg = ""

    if request.method == "POST":
        pwd = request.POST.get("password", "")

        pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%&*!])[A-Za-z\d@#$%&*!]{8,}$"

        if re.fullmatch(pattern, pwd):
            msg = "Valid Password"
        else:
            msg = "Invalid Password"

    return render(request, "password.html", {"msg": msg})