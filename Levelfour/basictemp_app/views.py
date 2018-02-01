from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text':'this is interesting','number': 637773}
    return render(request, 'basictemp_app/index.html', context_dict)


def other(request):
    return render(request, 'basictemp_app/other.html')

def relative(request):
    return render(request, 'basictemp_app/relative_url_templates.html')
