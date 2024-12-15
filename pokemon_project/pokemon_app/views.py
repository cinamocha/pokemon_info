from django.shortcuts import render
import requests

# Create your views here.
def index(request):
  pokemon_data = None #ポケモン情報の初期値
  pokemon_name = request.GET.get('pokemon_name')  #フォームの入力を取得

  if pokemon_name:  #名前が入力された場合
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
      data = response.json()
      pokemon_data = {
        'name': data['name'],
        'types': [t['type']['name'] for t in data['types']],
        'weight': data['weight'],
        'height': data['height'],
        'image_url': data['sprites']['front_default'],
      }
    else:
      pokemon_data = {'error': f"ポケモン '{pokemon_name}' が見つかりませんでした！"}

  return render(request, 'pokemon_app/index.html', {'pokemon_data': pokemon_data})