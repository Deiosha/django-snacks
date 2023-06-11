# What is going to be 'invoked' when a user visits your website?
from django.views.generic import TemplateView


# fancy way of using templates
class HomePageView(TemplateView):
    template_name = 'home.html'

    # emulate retrieving 'things' from a db
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # we assign a list to a key called "things" inside of context
        context["things"] = [
            {
                "title": "chips",
                "description": "Yummy and salty.",
            }, {
                "title": "cookies",
                "description": "chewy and soft",
            }, {
                "title": "candy",
                "description": "sweet.",
            },
        ]

        return context


class AboutView(TemplateView):
    template_name = 'about.html'
