import bpy
import csv
import os

blend_dir = os.path.dirname(bpy.data.filepath)

#############################################################################

# Set path to your local directory with results of PCoA. Default is the same where .blend file is stored

Path = (blend_dir + "\\data\\")

# Set the name of the exported CSV file from the R script

csv_file = "Hindex dataset.csv" #Hindex and technology (just type the name of the .csv file output from .R script)



#############################################################################
##########################Do not change a thing below this line##############
############################################################################

csv_file_path = str(Path + csv_file)
# Base structure to load data
mds_data = []
mds_var_per = [0, 0, 0]  # Defined three coordinates for each axe

# Load up CSV file with percentage loads of PCoA and coortindates
with open(csv_file_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # First row define the percentage of each axe (in the columns PCoA1, PCoA2 a PCoA3)
    first_row = next(reader)
    mds_var_per[0] = float(first_row['PCoA1'])
    mds_var_per[1] = float(first_row['PCoA2'])
    mds_var_per[2] = float(first_row['PCoA3'])
    
    # Next rows include coordinates of PCoA results in the x,y,z
    for row in reader:
        sample_name = row['Sample']  # Name of the object is defined in the 'Sample' column
        x = float(row['X'])
        y = float(row['Y'])
        z = float(row['Z'])
        mds_data.append((sample_name, x, y, z))

# Function of moving the object points into the 3D coortinate space
def place_model(object_name, x, y, z):
    # Najdeme objekt podle jména
    obj = bpy.data.objects.get(object_name)
    
    if obj:
        # Přesuneme objekt na nové souřadnice
        obj.location = (x, y, z)
    else:
        print(f"Objekt s názvem {object_name} nebyl nalezen.")

# Move existing objects (their object origins) into the space coorditase based on the CSV dat
for sample_name, x, y, z in mds_data:
    place_model(sample_name, x, y, z)

# Create labels based on the CSV file in the 3D pace
def create_axis_labels():
    font_size = 0.012

    # X-osa (PCoA1)
    bpy.ops.object.text_add(location=(0.5, 0, 0))
    x_axis_label = bpy.context.object
    x_axis_label.data.body = f"PCoA1 - {mds_var_per[0]}%"
    x_axis_label.scale = (font_size, font_size, font_size)
    
    # Y-osa (PCoA2)
    bpy.ops.object.text_add(location=(0, 0.5, 0))
    y_axis_label = bpy.context.object
    y_axis_label.data.body = f"PCoA2 - {mds_var_per[1]}%"
    y_axis_label.scale = (font_size, font_size, font_size)
    
    # Z-osa (PCoA3)
    bpy.ops.object.text_add(location=(0, 0, 0.5))
    z_axis_label = bpy.context.object
    z_axis_label.data.body = f"PCoA3 - {mds_var_per[2]}%"
    z_axis_label.scale = (font_size, font_size, font_size)

# Create ticks in the 3D pace
def create_ticks():
    tick_size = 0.002
    rngA = -20
    rngB = 20
    loc = 0.01

    # X-osa tick
    for i in range(rngA, rngB):
        bpy.ops.mesh.primitive_cube_add(size=tick_size, location=(i * loc, 0, 0))

    # Y-osa tick
    for i in range(rngA, rngB):
        bpy.ops.mesh.primitive_cube_add(size=tick_size, location=(0, i * loc, 0))

    # Z-osa tick
    for i in range(rngA, rngB):
        bpy.ops.mesh.primitive_cube_add(size=tick_size, location=(0, 0, i * loc))

# Create axes in the 3D pace
def create_axes():
    rad = 0.001
    dpt = 1
    bpy.ops.mesh.primitive_cylinder_add(radius=rad, depth=dpt, location=(0, 0, 0))
    x_axis = bpy.context.object
    x_axis.rotation_euler = (0, 0, 1.5708)  # Rotace pro vytvoření X osy
    
    bpy.ops.mesh.primitive_cylinder_add(radius=rad, depth=dpt, location=(0, 0, 0))
    y_axis = bpy.context.object
    y_axis.rotation_euler = (0, 1.5708, 0)  # Rotace pro vytvoření X osy
    
    
    bpy.ops.mesh.primitive_cylinder_add(radius=rad, depth=dpt, location=(0, 0, 0))
    z_axis = bpy.context.object
    z_axis.rotation_euler = (1.5708, 0, 0)  # Rotace pro vytvoření Z osy

#Create axes, ticks and labels
create_axes()
create_axis_labels()
create_ticks()

print("Objects moved, axis labels created based on CSV data.")

