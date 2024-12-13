import requests
from PIL import Image
from io import BytesIO

#Pillow(PIL)はポケモン画像を取得して表示するライブラリ
#BytesIOは画像データを直接メモリに読み込んで操作する

def fetch_evolution_chain(species_url):
  species_response = requests.get(species_url)
  
  if species_response.status_code == 200:
    species_data = species_response.json()
    evolution_url = species_data['evolution_chain']['url']

    evolution_response = requests.get(evolution_url)
    if evolution_response.status_code == 200:
      evolution_data = evolution_response.json()
      chain = evolution_data['chain']
      evolution_chain = extract_evolution_chain(chain)
      print('進化チェーン:' + ' → '.join(evolution_chain))
    else:
      print('進化チェーン情報が取得できませんでした。')
  else:
    print('ポケモンの種情報が取得できませんでした。')

def extract_evolution_chain(chain):
  evolution_chain = []
  while chain:
    evolution_chain.append(chain['species']['name'])
    if chain['evolves_to']:
      chain = chain['evolves_to'][0]
    else:
      break
  return evolution_chain

def pokemon_info(pokemon_name):
  url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}'
  response = requests.get(url)
  
  if response.status_code == 200:
    data = response.json()
    name = data['name']
    pokedex_id = data['id']
    types = [t['type']['name'] for t in data['types']]
    abilities = [a['ability']['name'] for a in data ['abilities']]
    weight = data['weight']
    height = data['height']
    image_url = data['sprites']['front_default']
    
    print(f'図鑑番号：{pokedex_id}')
    print(f'名前：{name}')
    print(f'タイプ：{','.join(types)}')
    print(f'特性：{',' .join(abilities)}')
    print(f'重さ：{weight}kg')
    print(f'高さ：{height}m')
    print(f'画像：{image_url}')
    
    #画像の表示
    #PILのImage.openで画像を開く、.showで表示
    if image_url:
      image_response = requests.get(image_url)
      img = Image.open(BytesIO(image_response.content))
      img.show()
    else:
      print('画像が見つかりませんでした')
    
    species_url = data['species']['url']
    fetch_evolution_chain(species_url)
  
  else:
    print(f'{pokemon_name}が見つかりません')

pokemon_name = input('ポケモンの名前を入力してください！')
pokemon_info(pokemon_name)