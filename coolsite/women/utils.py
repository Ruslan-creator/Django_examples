from .models import *

menu = [
    {"title": "About site", "url_name": "about"},
    {"title": "Add title", "url_name": "add_page"},
    {"title": "Feedback", "url_name": "contact"},
]


class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        context["menu"] = menu
        context["cats"] = cats
        if "cat_selected" not in context:
            context["cat_selected"] = 0
        return context
