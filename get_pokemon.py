import requests
from PIL import Image
from io import BytesIO

#Pillow(PIL)はポケモン画像を取得して表示するライブラリ
#BytesIOは画像データを直接メモリに読み込んで操作する

#get_japanese_nameで日本語名を取得できる関数を定義する
def get_japanese_name(species_url):
  response = requests.get(species_url)
  if response.status_code == 200:
    data = response.json()
    for name_entry in data['names']:
      if name_entry['language']['name'] == 'ja':
        return name_entry['name']
  return '名前不明'

#get_japanese_typeでタイプ名を日本語で取得できる関数を定義
def get_japanese_type(type_url):
  response = requests.get(type_url)
  if response.status_code == 200:
    data = response.json()
    for name_entry in data['names']:
      if name_entry['language']['name'] == 'ja':
        return name_entry['name']
  return 'タイプ不明'

#get_japanese_abilityで特性を日本語で取得できる関数を定義
def get_japanese_ability(ability_url):
  response = requests.get(ability_url)
  if response.status_code == 200:
    data = response.json()
    for name_entry in data['names']:
      if name_entry['language']['name'] == 'ja':
        return name_entry['name']
  return '特性不明'

#get_evolution_chainは進化チェーンのURLを取得し、g_e_names関数を呼び出す
def get_evolution_chain(species_url):
  response = requests.get(species_url) #ここで種族データ取得
  if response.status_code == 200:
    data = response.json() #JSONデータを代入
    chain_url = data['evolution_chain']['url'] #ここで進化チェーンのURL取得
    return get_evolution_names(chain_url) #名前リスト取得
  return ['進化情報なし']

#進化段階に含まれるポケモンをすべて日本語名で取得
def get_evolution_names(chain_url):
  response = requests.get(chain_url)
  if response.status_code == 200:
    data = response.json()
    chain = data['chain']
    evolution_names = []

    while chain: #進化段階がなくなるまでたどっていく
      species_url = chain['species']['url']
      evolution_names.append(get_japanese_name(species_url))
      if chain['evolves_to']:
        chain = chain['evolves_to'][0]
      else:
        chain = None

    return evolution_names
  return ['進化情報なし']

def pokemon_info(pokemon_name):
  url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}'
  response = requests.get(url)
  
  if response.status_code == 200:
    data = response.json()
    species_url = data['species']['url']
    japanese_name = get_japanese_name(species_url)
    
    name = data['name']
    pokedex_id = data['id']
    types = [t['type']['name'] for t in data['types']]
    abilities = [get_japanese_ability(a['ability']['url']) for a in data ['abilities']]
    weight = data['weight']
    height = data['height']
    image_url = data['sprites']['front_default']
    evolution_chain = get_evolution_chain(species_url)
    
    print(f'図鑑番号：{pokedex_id}')
    print(f'名前：{japanese_name} (英語名：{name})')
    print(f'タイプ：{','.join(types)}')
    print(f'特性：{',' .join(abilities)}')
    print(f'重さ：{weight}kg')
    print(f'高さ：{height}m')
    print(f'進化チェーン：{'→' .join(evolution_chain)}')
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

#メイン処理
pokemon_name = input('ポケモンの名前を入力してください！')
pokemon_info(pokemon_name)