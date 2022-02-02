# nft-generator
Generate any number of ducks with randomized colors and accessories.

## Getting started

### Installation
- Clone the repo & install dependencies with pip
```
git clone https://github.com/poonchoi/nft-generator
```
```
pip install -r requirements.txt
```

## Usage

<!-- <details>
<summary>v1.0</summary>
Version 1 will generate ducks with randomized colors based on weighted rarity's.<br>
In my opinion the images that are generated don't look as good as v2 but make sure to check out both versions!<br>

<img src="https://i.ibb.co/WzWzLyp/duck-74.png" width=90 height=90 alt="image of duck">
<img src="https://i.ibb.co/mtmD7Kx/duck-70.png" width=90 height=90 alt="image of duck">
<img src="https://i.ibb.co/TgPC1FF/duck-77.png" width=90 height=90 alt="image of duck">
<img src="https://i.ibb.co/9Gf9GWF/duck-62.png" width=90 height=90 alt="image of duck">
 
- cd into <code>v1</code><br>
 
- Run <code>image_generator.py</code><br>
<pre>
python image_generator.py
</pre>
- The generated images will appear in the  <code>Images</code> folder<br>
</details>

<details>
<summary>v2.0</summary>
Version 2 will generate ducks with randomized colors and different accessories.<br>
 
<img src="https://i.ibb.co/5r414Zc/duck-3.png" width=90 height=90 alt="image of duck">
<img src="https://i.ibb.co/L9YQyxc/duck-21.png" width=90 height=90 alt="image of duck">
<img src="https://i.ibb.co/4894P0q/duck-17.png" width=90 height=90 alt="image of duck">
<img src="https://i.ibb.co/b1YmZr2/duck-18.png" width=90 height=90 alt="image of duck">
 
 
- cd into <code>v2</code><br>
 
- Run <code>image_generator_v2.py</code><br>
<pre>
python main.py [NUM_OF_IMAGES]
</pre>
- The generated images will appear in the  <code>Images</code> folder
</details> -->
### v1.0
Version 1 will generate ducks with randomized colors based on weighted rarity's.
<br><img src="https://i.ibb.co/WzWzLyp/duck-74.png" width=90 height=90 alt="image of duck">
<img src="https://i.ibb.co/mtmD7Kx/duck-70.png" width=90 height=90 alt="image of duck">
<img src="https://i.ibb.co/TgPC1FF/duck-77.png" width=90 height=90 alt="image of duck">
<img src="https://i.ibb.co/9Gf9GWF/duck-62.png" width=90 height=90 alt="image of duck">
<img src="https://i.ibb.co/frD40h8/duck-26.png" width=90 height=90 alt="image of duck">
<img src="https://i.ibb.co/CtMg6JH/duck-90.png" width=90 height=90 alt="image of duck"><br>

- CD into `v1`

- To generate an image, run
```
python image_generator.py
```

### v2.0
Version 2 will generate ducks with randomized colors and different accessories.
<br><img src="https://i.ibb.co/5r414Zc/duck-3.png" width=90 height=90 alt="image of duck">
<img src="https://i.ibb.co/L9YQyxc/duck-21.png" width=90 height=90 alt="image of duck">
<img src="https://i.ibb.co/4894P0q/duck-17.png" width=90 height=90 alt="image of duck">
<img src="https://i.ibb.co/b1YmZr2/duck-18.png" width=90 height=90 alt="image of duck">
<img src="https://i.ibb.co/7yrm1GL/duck-92.png" width=90 height=90 alt="image of duck">
<img src="https://i.ibb.co/D5wKYmG/duck-109.png" width=90 height=90 alt="image of duck"><br>

- CD into `v2`

- To generate an image, run
```
python main.py [NUM_OF_IMAGES] [OPTION]...
```
```
Arguments:
  NUM_OF_IMAGES [required]   Number of images you want to generate
 
Options:
  -b, --bar     Show progress bar when generating images
  -s, --show    Open image folder on completion
  --help        Show all options
```
### Commuity v3.0
This program was made by <a href="https://github.com/besir660">@besir660</a>.<br>
The program will function similarly to v2.0 but is slightly quicker at generating the images.

- CD into `'Community v3'/v3`

- To generate an image, run
```
python image_generator_v3.py
```

