import bpy
from math import *
import math
import bpy, bmesh

# ------------------ This portion of the script generates the actual geometry from imported or default data ------------------ #
def createMeshFromData(name, origin, verts, edges, faces):
    # Create mesh and object
    me = bpy.data.meshes.new(name+'Mesh')
    ob = bpy.data.objects.new(name, me)
    ob.location = origin
    ob.show_name = False
    # Link object to scene and make active
    bpy.context.collection.objects.link(ob)
    ob.select_set(True)

    # Create mesh from given verts, faces.
    me.from_pydata(verts, edges, faces)

    # Update mesh with new data
    me.update()

C = 8.47799 # Sets x origin.

# ---- default data ---- # comment this portion out if using imported data
# verts1 contains all xyz coordinates
# default - based off 40 tooth gear

verts1 = [[18.7939, 0.0, 0], [18.8227186176212, 0.0010648578906716144, 0], [18.90890914624056, 0.008511021290507648, 0], [19.05167697002892, 0.02868062520523285, 0], [19.249702246453555, 0.0678376439337713, 0], [19.50114666167366, 0.1321292607273673, 0], [19.80366284741993, 0.22754777540109491, 0], [20.154406418876736, 0.35989322578595173, 0], [20.550050581793805, 0.5347368959872805, 0], [20.986803245966822, 0.7573858807833217, 0]]
# ---------------------- #

# ---- imported data ---- # comment this portion out if using default / internal data
#read_mesh = open("C:\\Users\chris\OneDrive\\Nefari0 Repository\Python\Blender\mesh_data.txt","r")
#is_read = read_mesh.read()
#read_mesh.close()

#read_list = list(is_read.split('>>')) # converts to python array
## list_index = read_list.split('<')
##new_coords = []
#verts1 = []

#for i in range(len(read_list)-1):
#    list_index = read_list[i].split('<') # converts each array element into floats, stores in new_coord array
#    coords = [float(list_index[1]),float(list_index[3]),float(list_index[5])]
#    verts1.append(coords)
# ------------------------#

# This calculates the edges based on the verts1 array
edges1 = [[len(verts1) - 1, 0]]
for i in range( 0, len(verts1)-1):
    edges1.append( [i, i+1] )

# Generate the actual Blender geometry:(name, origin, verts, edges, faces)

# ----------------------------------------------------------------------------------------------------------------- #

# ---- Create Gear Profile ---- #

# generate gear tooth
teeth = 40

createMeshFromData( 'Geometry_init', [0, 0, 0], verts1, edges1, [] ) # initial side tooth geometry
bpy.ops.transform.rotate(value=math.pi, orient_axis='X')
bpy.ops.transform.rotate(value=2*math.pi/teeth, orient_axis='Z')
#bpy.ops.object.select_all(action='DESELECT')

##context.view_layer.objects.active = context.scene.objects.get(target)
#bpy.ops.object.mode_set(mode='EDIT')
##bpy.ops.mesh.duplicate_move(MESH_OT_duplicate={"mode":1})

# need to remove line connecting ends

#bpy.ops.object.select_all(action='DESELECT')
createMeshFromData( 'Geometry', [0, 0, 0], verts1, edges1, [] )

#bpy.ops.objects.join()
for obj in bpy.context.selected_objects:
    obj.name = "Cyl"
    obj.data.name = "Cyl"
    bpy.ops.object.select_by_type(extend=False, type='MESH')
    bpy.ops.object.join()
    bpy.ops.object.select_all(action='DESELECT')
#    obj.name = "GEO_sphere"
#    obj.data.name = "GEO_sphere"

#bpy.ops.transform.rotate(value=math.pi, orient_axis='X')
#bpy.ops.transform.rotate(value=2*math.pi/teeth, orient_axis='Z')
#bpy.ops.object.select_all(action='SELECT')

# rotate gear tooth to it's position # this may not be used as is
#teeth = 40
#z_rotate_init = 0# inition z rotation
#zRotation = 0.07853981633974483096156608458199
#for i in range(teeth):
#    createMeshFromData( 'Geometry', [0, 0, 0], verts1, edges1, [] )
#    bpy.ops.transform.rotate(value=z_rotate_init, orient_axis='Z')
#    z_rotate_init += zRotation


print('script running')