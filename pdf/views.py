from django.shortcuts import render
from .models import Profile
from django.http import HttpResponse
from django.template import loader
import pdfkit
import io

# Create your views here.
def accept(request):
    if request.method == 'POST':
        name = request.POST.get("name","")
        phone = request.POST.get("phone", "")
        email = request.POST.get("email", "")
        school = request.POST.get("school", "")
        degree = request.POST.get("degree", "")
        university = request.POST.get("university", "")
        skills = request.POST.get("skills", "")
        work_exp = request.POST.get("work_exp", "")
        about_you = request.POST.get("about_you", "")
        profile = Profile(name=name,phone=phone,email=email,school=school,degree=degree,university=university,skills=skills,work_exp=work_exp,about_you=about_you)
        profile.save()

    return render(request,'accept.html')

def resume(request,id):
    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template("resume.html")
    html = template.render({"user_profile": user_profile})
    option = {
        'page-size':'Letter',
        'encoding':'UTF-8'
    }
    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pdf = pdfkit.from_string(html,False,option,configuration=config)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition']='attachment'
    return response

def list(request):
    profiles = Profile.objects.all()
    return render(request,"list.html",{'profiles': profiles})

