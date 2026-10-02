from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import RegistroCheckInForm


def index(request):
	if request.method == 'POST':
		form = RegistroCheckInForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(
				request,
				'Seu check-in foi salvo. Obrigado por reservar esse momento para você.',
			)
			return redirect('checkin:index')
	else:
		form = RegistroCheckInForm()

	return render(request, 'checkin/index.html', {'form': form})
