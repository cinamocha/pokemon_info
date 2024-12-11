import requests
from PIL import Image
from io import BytesIO

#Pillow(PIL)はポケモン画像を取得して表示するライブラリ
#BytesIOは画像データを直接メモリに読み込んで操作する

def pokemon_info(pokemon_name):
  url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}'
  response = requests.get(url)
  
  if response.status_code == 200:
    data = response.json()
    name = data['name']
    types = [t['type']['name'] for t in data['types']]
    weight = data['weight']
    height = data['height']
    image_url = data['sprites']['front_default']
    
    print(f'名前：{name}')
    print(f'タイプ：{','.join(types)}')
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
  
  else:
    print(f'{pokemon_name}が見つかりません')

pokemon_name = input('ポケモンの名前を入力してください！')
pokemon_info(pokemon_name)