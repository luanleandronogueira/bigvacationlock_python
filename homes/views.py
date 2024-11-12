from django.shortcuts import render, redirect
from .models import House
from django.contrib import messages

# views here.
def dashboard(request):
    return render(request, 'homes/dashboard.html')

def houses(request):
    return render(request, 'homes/houses.html')

def create_house(request):
    return render(request, 'homes/create_house.html')

def insert_house(request):
  if request.method == 'POST':

    address = request.POST.get('address')
    house_name = request.POST.get('house_name')
    door_code = request.POST.get('door_code')
    gate_code = request.POST.get('gate_code')
    community_pool = request.POST.get('community_pool')
    fitness_center = request.POST.get('fitness_center')
    wifi_network = request.POST.get('wifi_network')
    wifi_password = request.POST.get('wifi_password')
    who_cares = request.POST.get('who_cares')
    observations = request.POST.get('observations')
    photo_house = request.FILES.get('photo_house')

    try:
      new_house = House(
          address=address,
          house_name=house_name,
          door_code=door_code,
          gate_code=gate_code,
          community_pool=community_pool,
          fitness_center=fitness_center,
          wifi_network=wifi_network,
          wifi_password=wifi_password,
          who_cares=who_cares,
          observations=observations,
      )
      new_house.save()
      messages.success(request, 'Casa cadastrada com sucesso!')  # Passa o request como argumento
      return redirect('houses')

    except Exception as e:
      messages.error(request, f'Erro ao cadastrar a casa: {str(e)}')

  return redirect('create_house')