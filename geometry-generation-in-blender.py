
import bpy
from math import *
import math

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

read_mesh = open("C:\\Users\\chris\\OneDrive\\Nefari0 Repository\\Python\\Blender\mesh_data.txt","r")
is_read = read_mesh.read()
read_mesh.close()

read_list = list(is_read.split('>>')) # converts to python array
# list_index = read_list.split('<')
#new_coords = []
verts1 = []

for i in range(len(read_list)-1):
    list_index = read_list[i].split('<') # converts each array element into floats, stores in new_coord array
    coords = [float(list_index[1]),float(list_index[3]),float(list_index[5])]
    verts1.append(coords)

print(verts1)

# This calculates the edges based on the verts1 array
edges1 = [[len(verts1) - 1, 0]]
for i in range( 0, len(verts1)-1):
    edges1.append( [i, i+1] )


# Generate the actual Blender geometry:(name, origin, verts, edges, faces)
createMeshFromData( 'Geometry', [0, 0, 0], verts1, edges1, [] )