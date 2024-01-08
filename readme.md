##A Texture to Model converter for Minecraft
*Note, only support for 32x32 textures\** 

A tool to make items in your resource packs which are larger than usual (up to twice the size).

Converts a texture to a model file, that should look identical to the texture, except without being scaled. 
Normally when using a 32x32 texture for an item in a resourcepack, the item will still be the same size as usual, just with a more high-res texture.
This converter won't do that, and the item will instead be twice the size ingame.

I made this for a datapack where I added longswords. To make the longswords, long, I used this tool.

###Usage

1. Install Python
2. Install PIL with the following command: `pip install pillow`
3. Replace texture.png with whatever texture you want.
4. Open the start.bat
5. Enter the model path, if you want to replace an ingame item, simply enter the item's name. 
6. The converter generates an assets/ folder, that can be added to your resourcepack.

###Advanced:
If you don't want to replace an item, you can instead at Step 5 have the path be in a subdirectory, example: custom/iron_longsword.
CustomModelData is a way to create variations of texture for a single item. The different variations can be spawned with commands.
To do that you will need a second model file in the assets/minecraft/model/item folder, with the name of the base item (with the .json file extension).

The following example is to make it so that an iron_sword with the CustomModelData of 1, will instead use custom/iron_longsword as model.
```{
	"parent": "item/handheld",
	"textures": {
		"layer0": "item/iron_sword"
	},
	"overrides": [
		{ "predicate": {  "custom_model_data": 1 }, "model": "item/custom/iron_longsword"}
	]
}```

Do note, if the base item is not a sword, "parent" should be "generated".