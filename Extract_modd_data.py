# Import libraries
import bpy
import sys
sys.path.append("setpaht to python libraries") #usually C:/Users/NAME/AppData/Roaming/Python/PYTHON_VERSION/site-packages
import numpy as np
import pandas as pd
import os
import glob

# Set up name of collections with cuts
sel = "Pritluky"

# Set variable for later collection operations
col = bpy.data.collections[sel]

# Create list of objects inside the selected collection
ob = col.objects[:]

# Set path to the folder where you desire to save your exported data
pth = ("set path where you want to save your data" + "/" + col.name)

# If path does not exist, create it
if not os.path.exists(pth):
    os.makedirs(pth)

# Print the number of cross-sections in the collection to the console
print("Number of objects inside the collection " + col.name + " is " + str(len(ob)))

# Create count variable for while loop, based on the number of cross-sections in the collection
count = int(len(ob))

# Create counter for while loop
X = 0

# Specify columns to remove (add the column names you want to delete here)
columns_to_remove = ['.select_vert', '.select_poly', '.select_edge','Counter_linear', '.edge_verts', '.corner_vert', '.corner_edge', 'Counter', 'position', 'face_normal', 'inside', 'coutner_linear', '_outsideSlice_middle', 'POR', 'Z_percentage', 'Z_percentage_new', 'Radius_int', 'Slice_middle_outside', 'Inside']  # replace with your column names


# List to hold all DataFrames for merging at the end
all_dataframes = []
# List to hold only the second row from each object for a separate file
second_row_dataframes = []

# While loop that exports data from every cross-section in the collection
while X < count:
    
    # Select the nth element from the 'ob' list and make it active
    bpy.context.view_layer.objects.active = ob[X]
    print(ob[X])
    
    # Get final data about the mesh with all modifiers and changes
    obj = bpy.context.object.evaluated_get(bpy.context.evaluated_depsgraph_get()).data
    
    # Initialize an empty DataFrame to hold all attribute data
    all_attributes_df = pd.DataFrame()

    # Iterate over all attributes
    for attr in obj.attributes:
        attr_name = attr.name
        try:
            # Attempt to read the attribute's data as value
            data = [i.value for i in obj.attributes[attr_name].data]
            print(f"Loaded attribute '{attr_name}' as value.")
        
        except AttributeError:
            try:
                # If 'value' fails, attempt to read the attribute's data as vector
                data = [i.vector for i in obj.attributes[attr_name].data]
                print(f"Loaded attribute '{attr_name}' as vector.")
                
            except AttributeError:
                # Skip this attribute if neither 'value' nor 'vector' works
                print(f"Skipping attribute '{attr_name}' due to AttributeError.")
                continue
        
        # Create a DataFrame for the current attribute
        attr_df = pd.DataFrame(data, columns=[attr_name])
        
        # Concatenate the current attribute DataFrame with the main DataFrame
        all_attributes_df = pd.concat([all_attributes_df, attr_df], axis=1)
    
    # Access the position variable for each vertex as a numpy array
    coords = np.zeros(len(obj.vertices) * 3, dtype=float)
    obj.vertices.foreach_get("co", coords)
    np.round(coords, decimals=7, out=coords)
    
    # Convert numpy array of positions into a tuple of 3
    coords = coords.reshape(len(obj.vertices), 3)
    
    # Create a DataFrame for the coordinates
    coords_df = pd.DataFrame(coords, columns=['X', 'Y', 'Z'])
    
    # Join all attributes and coordinates DataFrame into one based on the index
    result = pd.concat([all_attributes_df, coords_df], axis=1)

    # Add a column with the object name
    result['Object'] = ob[X].name
    
    # Drop specified columns
    result = result.drop(columns=columns_to_remove, errors='ignore')  # 'errors=ignore' will ignore columns that are not present

    # Sort columns alphabetically
    result = result.sort_index(axis=1)

    # Append the result DataFrame to the list for merging later
    all_dataframes.append(result)
    
    # Extract the second row (index 1) of the DataFrame for this object
    if len(result) >= 1:  # Ensure there are at least two rows
        second_row = result.iloc[[0]]  # Extract the second row
        second_row = second_row.sort_index(axis=1)  # Sort columns alphabetically
        second_row_dataframes.append(second_row)  # Add to the list of second rows

    # Export the result to individual CSV (.txt), separator is tab
    result.to_csv(pth + "\\" + ob[X].name + ".txt", sep="\t")
    
    # Increment counter
    X += 1
    
    # Deselect all, important for selection in every loop
    bpy.context.view_layer.objects.active = None
    
    print(X)

# Merge all DataFrames into one
final_result = pd.concat(all_dataframes, ignore_index=True)

# Sort columns alphabetically before saving
final_result = final_result.sort_index(axis=1)

# Export the final merged result to a single file
final_result.to_csv(pth + "\\" + "merged_result.txt", sep="\t", index=False, decimal=',', float_format='%11.4f')

# Merge all the second rows into one DataFrame
second_row_result = pd.concat(second_row_dataframes, ignore_index=True)

# Sort columns alphabetically before saving
second_row_result = second_row_result.sort_index(axis=1)

# Export the result of the second rows into a separate file
second_row_result.to_csv(pth + "\\" + "second_row_merged_result.txt", sep="\t", index=False, decimal=',', float_format='%11.4f')

# Get the list of exported files
file_list = glob.glob(pth + "\\" + "*.txt")
print(file_list)

print("Done")
