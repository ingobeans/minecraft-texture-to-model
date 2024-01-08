from PIL import Image
from json import dumps
import shutil, os

base = {
	"credit": "Made with minecraft-texture-to-model converter by https://github.com/ingobeans",
    "textures": {
		"0": "item/undefined",
		"particle": "item/undefined"
	},
	"elements": [
	],	
    "gui_light": "front",
	"display": {
		"thirdperson_righthand": {
			"rotation": [0, -90, 55],
			"translation": [0.5, 3.5, 1],
			"scale": [0.85, 0.85, 0.85]
		},
		"thirdperson_lefthand": {
			"rotation": [0, 90, -55],
			"translation": [-0.5, 3.75, 1.5],
			"scale": [0.85, 0.85, 0.85]
		},
		"firstperson_righthand": {
			"rotation": [0, -90, 25],
			"translation": [5.65, -0.05, -2.85]
		},
		"firstperson_lefthand": {
			"rotation": [0, 90, -25],
			"translation": [4.65, -0.05, -2.85]
		},
		"ground": {
			"translation": [0, 2, 0],
			"scale": [0.5, 0.5, 0.5]
		},
		"gui": {
			"translation": [0, 0, 80]
		},
		"fixed": {
			"rotation": [0, 180, 0],
			"translation": [0, -1, 0.75]
		}
	}
}

faces = ["north","east","south","west","up","down"]
elements = []
image_path = "texture.png"
image = Image.open(image_path)
image = image.convert("RGBA")
width, height = image.size
if width != 32 and height != 32:
    print("Texture must be 32x32 resolution")
    quit()
pixels = [[(0, 0, 0,0) for _ in range(width)] for _ in range(height)]
image_scale_multiplier = width/16

file_name = input("Enter the model path. Ex. 'apple', which would replace the default apple or 'custom/iron_longsword', which doesn't replace an in-game item: ")

for y in range(height):
    for x in range(width):
        pixel = image.getpixel((x, y))
        pixels[y][x] = pixel


for y in range(height-1,-1,-1):
    for x in range(width):
        r,g,b,a = pixels[y][x]
        if a == 0:
            continue
        elements.append({"from":[x,height-y-1,8],"to":[x+1,height-y-1+1,9],"faces":{}})
        for face in faces:
            elements[-1]["faces"][face] = {"uv":[x/image_scale_multiplier,y/image_scale_multiplier,x/image_scale_multiplier+1/image_scale_multiplier,y/image_scale_multiplier+1/image_scale_multiplier],"texture":f"#0"}

base["textures"]["0"] = f"item/{file_name}"
base["textures"]["particle"] = f"item/{file_name}"
base["elements"] = elements

if os.path.isdir("assets"):
	shutil.rmtree("assets")
os.makedirs("assets/minecraft/models/item/",exist_ok=True)
os.makedirs("assets/minecraft/textures/item/",exist_ok=True)

root = "assets/minecraft"

with open(f"{root}/models/item/{file_name}.json","w") as f:
    f.write(dumps(base))

shutil.copyfile(image_path, f"{root}/textures/item/{file_name}.png")

print("Converted texture to model. Generated an assets folder, that can be added to a resource pack.")