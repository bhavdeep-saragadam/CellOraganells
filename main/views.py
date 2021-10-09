from django.shortcuts import render

# Create your views here.



def main(request):
	return render(request, 'home.html')

def Nucleus(request):
	return render(request, 'nucleus.html')

def cell_mem(request):
	return render(request, 'cell-membrane.html')