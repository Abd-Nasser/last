from django.shortcuts import render, redirect
from .api import get_devise_data

def dashboard(request, param_days, param_devises):
    days, devises = get_devise_data(param_devises.split(), param_days )
    page_labels={7:"Semaine", 30:"Mois", 365:"Année"}.get(param_days,"Personalisé")
    return render(request, "ss_templates/index.html", context={"days_data":days,
                                                                            "devises_data":devises,
                                                                            "page_labels": page_labels,
                                                                             "url_param": param_devises})


def redirect_index(request):
   return redirect("bord", param_days=30, param_devises="usd")

