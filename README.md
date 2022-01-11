# Jupyter-blender
How to use this code.

Open 'blender-geometry-data-convertion.ipynb' in Jupyter Notebook

You must run each every code cell in it's order for this code to work. They are listed as follows:

“Import Libraries”

you can either run the “Internally generated plots” cell to generate plots from this script, or the “Import Data Coordinate Vectors” cell for imported plots. (Note that the default  'coord_data_[x,y,z]' txt files, and the mesh_data.txt file, have coordinates saved in them that can be run from the “Import Data Coordinate Vectors”  cell.

“Calculate and Export Plots”

There are two cells that are not meant to be run here. The "Extract Coordinates from External Script" cell is meant to be used in an external python script. It's included in the "math-object-sample.ipynb" file for demonstrative purposes.

The cell marked “Paste the text in this cell into Blenders scripting window” is clearly only meant to be used in Blender. 

Once the appropriate cells have been run, you can either paste the code from the “Paste the text in this cell into Blenders scripting window” cell into the Blender scripting window in a new file, or load “geometry-generation-in-blender.py” file directly into the Blender scripting window. 

If you're interested in beveling the objects as I've done in the .png photos, you'll have to convert the objects into curves first. I plan on adding instructions on how to do this in the future

