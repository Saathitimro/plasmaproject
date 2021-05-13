from django.shortcuts import render
from .models import Donor, Blood
# Create your views here.
# go to home page
def home(request):
    return render(request,"index.html" )

# go to doner page
def doner(request):
    return render(request,"donor.html" )

#save in database after doner registration
def doner_submit(request):
    name = request.POST['donor-name']
    contact = request.POST["donor-contact"]
    address = request.POST["donor-address"]
    blood_type = request.POST["blood-type"]
    vaccin = request.POST["vaccin"]
    recovered_time = request.POST["recovered_time"]
    future_donation = request.POST["blood-req"]
    # this saves the future blood donators info
    if future_donation == "True" :
        add_blood = Blood(Name=name,Contact=contact,Blood_type=blood_type)
        add_blood.save()
    #this saves the data if condition is not satisfied
    if recovered_time == "3" and vaccin == "False":
        return render(request,"index.html")
    add_donor= Donor(Name=name,Contact=contact,Address=address,Blood_type=blood_type,Vacinated=vaccin,Recovered=future_donation)
    add_donor.save()
    return render(request,"index.html")
