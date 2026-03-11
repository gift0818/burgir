from django.shortcuts import render
from . models import Student
# Create your views here.
def enrol(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname", "").strip()
        lastname = request.POST.get("lastname", "").strip()
        age = request.POST.get("age", "").strip()
        gender = request.POST.get("gender", "").strip()

        student = Student.objects.create(
            firstname=firstname,
            lastname=lastname,
            age=int(age) if age else 0,
            gender=gender
        )
        info = {
            "submitted": True,
            "firstname": firstname,
            "lastname": lastname,
            "age": age,
            "gender": gender,
        }
        return render(request, "enroll.html", info)
    return render(request, "enroll.html")

