from django.shortcuts import render
from EvalFormFiller import form_filler
import threading

# Create your views here.
def index(request):
    if request.POST.get('id'):
        input_data = request.POST
        valid = form_filler.check_login_credentials(input_data['id'], input_data['password'])
        if valid:
            threading.Thread(target=lambda: form_filler.main(valid)).start()
            return render(request, 'valid.html')
        return render(request, 'invalid.html')
    return render(request, "login.html")
