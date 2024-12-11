# ポケモンの情報取得(pokemon-info)  
ポケモンの名前を入力すると、タイプや重さなどの情報を取得し、画像と一緒に表示します。  

## 概要  
- **ジャンル**:ポケモン情報取得
- **目的**:指定したポケモンの情報と画像を表示

## 改善点  
- 図鑑番号や進化前後のポケモンや特性、HPなどのステータスの追加  
- タイプなどからの逆検索  
- 表から選択  
- 入力言語の日本語対応  

## 使用技術  
- **プログラミング言語**:Python
- **ライブラリ**:requests Pillow BytesIO

## 使い方  

1. **Pythonをインストール**  
   [公式サイト](https://www.python.org/)からインストールしてください。

2. **クローンorダウンロード**
```
git clone https://github.com/cinamocha/pokemon_info
cd pokemon-info
```

3. **ライブラリのインストール**
```
pip install requests
pip install Pillow
```

4. **実行**
```
python get_pokemon.py
```
