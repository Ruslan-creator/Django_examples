from django.shortcuts import get_object_or_404, render

from .models import Accommodation, ListOfCountries


def main(request):
    return render(request, "mainapp/index.html")


def accommodations(request):
    title = "размещение"
    list_of_accommodations = Accommodation.objects.filter(is_active=True)
    content = {
        "title": title,
        "list_of_accommodations": list_of_accommodations,
    }

    return render(request, "mainapp/accommodations.html", content)


def accommodation(request, pk):
    title = "продукты"
    content = {
        "title": title,
        "links_menu": ListOfCountries.objects.all(),
        "accommodation": get_object_or_404(Accommodation, pk=pk),
    }

    return render(request, "mainapp/accommodation_details.html", content)
