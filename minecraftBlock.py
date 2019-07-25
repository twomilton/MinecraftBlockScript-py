import bpy

block_radius = 1
block_position = (0,0,block_radius)
texture_map_image = "textureMapImage.jpg"
texture_file_path = "C:\\imageFolder\\textureMapImage.jpg"
texture_file_dir = "C:\\imageFolder\\"
material_name = "Block Material"

def clearStage():
    # Delete default Blender objects
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
    bpy.ops.image.open(
        filepath= texture_file_path, 
        directory=texture_file_dir, 
        files=[{"name":texture_map_image, "name":texture_map_image}], 
        relative_path=True, show_multiview=False)
    bpy.data.images[texture_map_image].use_fake_user = True
    bpy.ops.object.editmode_toggle()
    cube = bpy.context.selected_objects[0]
    tx_image = bpy.data.images[texture_map_image]
    for uv_face in cube.data.uv_textures.active.data:
        uv_face.image = tx_image

def makeMaterial():
    # Cube Material
    cube = bpy.context.selected_objects[0]
    bpy.data.materials[0].name = material_name
    cube_material = bpy.data.materials.get(material_name)
    cube.data.materials.append(cube_material)
    cube.data.materials[material_name].diffuse_intensity = 1
    cube.data.materials[material_name].specular_intensity = 0
    
def makeTexture():    
    # Cube Texture
    texture = bpy.data.materials[material_name].active_texture
    bpy.data.textures["Tex"].type = 'IMAGE'
    bpy.data.textures["Tex"].image = bpy.data.images[texture_map_image]
    bpy.data.materials[material_name].texture_slots[0].texture_coords = 'UV'
    
    
clearStage()
addCube(block_radius, block_position)
addMap()
makeMaterial()
makeTexture()