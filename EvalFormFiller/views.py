from django.shortcuts import render
from EvalFormFiller import form_filler
import threading


# Create your views here.
def index(request):
    if request.POST.get('id'):
        input_data = request.POST
        threading.Thread(target=lambda: form_filler.main(input_data['id'], input_data['password'])).start()
        return render(request, 'valid.html')
        # return render(request, 'invalid.html')
    return render(request, "login.html")
