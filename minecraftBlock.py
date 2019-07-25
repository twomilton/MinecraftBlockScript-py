import bpy

blockRadius = 1
halfRadius = blockRadius/2
blockPosition = (0,0,blockRadius)
textureFilePath = "C:\\users\\mike\\pictures\\businesses\\mikeitall\\minecraftBlockTexture2.jpg"
textureFileDir = "C:\\users\\mike\\pictures\\businesses\\mikeitall\\"

def clearStage():
    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.object.delete()

def addCube(radius, pos):
    # Add Cube
    bpy.ops.mesh.primitive_cube_add(
        radius=radius, 
        enter_editmode=False, 
        location=pos)
    bpy.ops.object.editmode_toggle()
    bpy.ops.mesh.mark_seam(clear=False)
    bpy.ops.uv.smart_project(stretch_to_bounds=False)
    
def addMap():    
    # Map Texture
    textureMap = bpy.ops.image.open(
        filepath= textureFilePath, 
        directory=textureFileDir, 
        files=[{"name":"minecraftBlockTexture2.jpg", "name":"minecraftBlockTexture2.jpg"}], 
        relative_path=True, show_multiview=False)
    bpy.data.images["minecraftBlockTexture2.jpg"].use_fake_user = True
    bpy.ops.object.editmode_toggle()
    cube = bpy.context.selected_objects[0]
    tx_image = bpy.data.images["minecraftBlockTexture2.jpg"]
    for uv_face in cube.data.uv_textures.active.data:
        uv_face.image = tx_image
    #bpy.ops.object.bake_image()

def makeMaterial():
    # Cube Material
    cube = bpy.context.selected_objects[0]
    bpy.data.materials[0].name = "Block Material"
    cubeMaterial = bpy.data.materials.get("Block Material")
    cube.data.materials.append(cubeMaterial)
    cube.data.materials["Block Material"].diffuse_intensity = 1
    cube.data.materials["Block Material"].specular_intensity = 0
    
def makeTexture():    
    # Cube Texture
    texture = bpy.data.materials["Block Material"].active_texture
    bpy.data.textures["Tex"].type = 'IMAGE'
    bpy.data.textures["Tex"].image = bpy.data.images["minecraftBlockTexture2.jpg"]
    bpy.data.materials["Block Material"].texture_slots[0].texture_coords = 'UV'
    
    
clearStage()
addCube(blockRadius, blockPosition)
addMap()
makeMaterial()
makeTexture()