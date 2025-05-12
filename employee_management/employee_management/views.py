from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context

def index(request):
    my_html = open("/Users/juanpa/Documents/projects/python/employee-management/employee_management/templates/index.html")
    template = Template(my_html.read())
    my_html.close

    context = Context()
    document = template.render(context)

    return HttpResponse(document)