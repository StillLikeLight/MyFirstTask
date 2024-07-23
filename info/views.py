from django.shortcuts import render, HttpResponse
from django.views.decorators.http import require_http_methods
from django.conf import settings
from .models import Info
from .forms import InfoForm
import os


@require_http_methods(['GET', 'POST'])
def info_get_post(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        form = InfoForm(request.POST, request.FILES)
        if form.is_valid():
            phone_number = form.cleaned_data.get('phone_number')
            address = form.cleaned_data.get('address')
            name = form.cleaned_data.get('name')
            position = form.cleaned_data.get('position')
            sOrb = form.cleaned_data.get('sOrb')
            file_license = form.cleaned_data.get('file_license')
            Info.objects.create(phone_number=phone_number, address=address, name=name, position=position, sOrb=sOrb,
                                file_license=file_license)

            with open(os.path.join(settings.MEDIA_ROOT, file_license.name), 'wb+') as destination:
                for chunk in file_license.chunks():
                    destination.write(chunk)
            return HttpResponse("Your info has been saved successfully")
        else:
            print(form.errors)
            return HttpResponse(f'error')

