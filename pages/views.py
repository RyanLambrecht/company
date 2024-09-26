from django.shortcuts import render
from django.views.generic import TemplateView

def home_page_view(request):
    
    context = {
        "inventory_list": ["Widget 1", "Widget 2", "Widget 3"],
        "greeting": "THAnk you FOR visitING.", 
    }
    return render(request, "home.html", context)

class AboutPageView(TemplateView):
    template_name = "about.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact_address"] = "123 Main Street"
        context["phone_number"] = "555-555-5555"
        return context
    
class ProductPageView(TemplateView):
    template_name = "product.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product_1"] = "apples"
        context["product_2"] = "oranges"
        context["product_3"] = "bananas"
        context["product_4"] = "watermelon"
        return context
    