from datetime import date
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from family.models import Family


def create_member(request, name: str, ages: int, birth: str):

    template = loader.get_template("template_family.html")

    family = Family(name=name, ages=ages, birth=birth)
    family.save()  # save into the DB

    context_dict = {"family": family}
    render = template.render(context_dict)
    return HttpResponse(render)


def familys(request):
    familys = Family.objects.all()

    context_dict = {"family": familys}

    return render(
        request=request,
        context=context_dict,
        template_name="family/family_list.html",
    )