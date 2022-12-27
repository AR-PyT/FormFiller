from django.shortcuts import render
import form_filler
# from . import form_filler
import threading

# Create your views here.
def index(request):
    if request.POST.get('id'):
        input_data = request.POST
        if form_filler.check_login_credentials(input_data['id'], input_data['password']):
            threading.Thread(target=form_filler.main, args=(input_data['id'], input_data['password'])).start()
            return render(request, 'valid.html')
        return render(request, 'invalid.html')
    return render(request, "login.html")
