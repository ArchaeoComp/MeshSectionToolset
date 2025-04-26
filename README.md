# MeshSectionToolset

An open-source toolkit for archaeologists and researchers to explore 3D artifacts, especially pottery. This project simplifies morphometric analysis by leveraging Blender's Geometry Nodes and Python scripting.

---

## Description

MeshSectionToolset facilitates the semi-automated generation of virtual cross-sections for 3D models. Designed for non-standard, asymmetrical, handmade artifacts like pottery, it extracts morphometric data and exports it for further analysis. The toolset is optimized for speed, precision, and accessibility to researchers with minimal programming experience. This archive contains two subfolders:

### Data_extraction_blend_files
 - Slicing_tool_pottery.blend - file with geometry nodes setup to perform 3D model to 2D sections (polylines)
 - Extract_modd_data_v2.py - python file for extraction of data from GeometryNodes spreadsheets into the .txt file table (use /t as separator). It is mandatory to run this  from the "Scripting" tab in the Blender software (see the one of the example files) 
 - Vertical_att_only_extraction_example.blend - example file with modifiers and preloaded "Extract_modd_data_v2.py", used to extract all the data for the article. In general it can be used without applycation of Slicing_tool_pottery modifier, but at a cost of slower performance (depends on your hardware).
 - Slicing_tool_pottery_COHL_att_example.blend - example file with possible extraction of COHL attribute together with Slicing_tool_pottery modifier and with preloaded "Extract_modd_data_v2.py"
 

### R_code_and_visualization

 - JASC24-639_PCoA_analysis_used.R - the R code used for calculation of the PCoA based on the extracted datasets
 - Folder data/JASC24-639_Data_PCoA_used.txt - dataset used in the article: article_doi
 - All_pots_decimated_for_PCoA_visualization.blend - example blend file with decimated 3D models (used only for visualizations)
 - Load_CSV_file_with_coordinates.py - python file for loading of the data from the datasets (in .txt format, extracted by "Extract_modd_data_v2.py"). It is mandatory to run this  from the "Scripting" tab in the Blender software (see the All_pots_decimated_for_PCoA_visualization.blend)   

**Note**: The Numpy and Pandas python lybraries must be installed in the python libraries (look at the end of the README file for tips). Also, basic knowledge of 3D concepts and Blender software is recommended

---
## Features

### Virtual Cross-Sections (Slicing_tool_pottery.blend)

- Generates horizontal and vertical cross-sections using Geometry Nodes as modifiers in Blender.
- Implements the Möller-Trumbore ray intersection algorithm for fast and precise slicing.

### Attribute Extraction
- Computes key metrics like wall thickness, concentricity, and profile dimensions.
- Extracts descriptive points (e.g., maximum bulge, neck width) from 3D artifact geometry.

### Data Export
- Includes Python scripts to export computed attributes to `.csv` format.
- Compatible with Pandas and Numpy for seamless data processing.

### Efficiency
- Processes complex 3D models in seconds.
- Supports batch operations for large datasets.

### Applications
- Tested on 175 medieval pottery models, analyzing shape variability and production techniques.
- Adaptable to other archaeological or historical artifacts.

---

## Basic Usage

All files contains examples

1. **Prepare 3D Model**:
   - Open `Slicing_tool_pottery.blend` in Blender.
   - Append or import your 3D scan of pottery into the project.

2. **Generate Sections**:
   - Use the Geometry Nodes modifiers to interactively generate horizontal and vertical sections.

3. **Extract Attributes**:
   - Apply modifiers to the 3D scan in `Slicing_tool_pottery.blend`.
   - Open `Attribute_extraction_used.blend`, append your slices, and use the "P1-P5 extraction" and "Prepare for export by python script" GeoNodes setup.

4. **Export Data**:
   - Use the `Extract_modd_data_v2.py` script (start it from Scripting tab inside Blender):
     - **Line 4**: Set the path to your Python library.
     - **Line 11**: Specify the Blender collection containing analyzed 3D slices.
     - **Line 20**: Define the output path for the exported `.csv` data.

---
## Basic/Optional workflow (tutorial)

 - 1. Import your pre-oriented data into the Blender (or orinet them in Blender instead), and apply their scale and transformation (select all objects in Blender, press "Ctrl+A" and select "Rotation & Scale" option.
 - 2. Append "Centre_bottom_to_origin_v2" from Centre_bottom_to_origin.blend file (In blender select "File -> Append...", the context menu will appears, find "Centre_bottom_to_origin.blend" and double click on it -> NodeTree/Centre_bottom_to_origin_v2_append_this (same logic will be used for every other append)).
 - 3. Select one of our 3D scans, switch to modifier tab (blue spanner icon) and click od "Add Modifier", than select "Geometry nodes" and search for "Centre_bottom_to_origin_v2_append_this". Apply modifier.
 - 4. Repeat the process but for SlicingTool Pottery. before applying, you can set vertical distance between cuts (Distance) and angular distance bewteen cuts (degree). By rotate to origin, you will set all cuts to z,y plane. Partial curves allows quick check if selection of inside/outside of pottery works (this should be turned off for next processing).
 - 5. Now, you have got slices of pottery! You can export the curves to other softwares (such as R, Matlab etc.), or use our prebuild data extractors (see article) 
 - 6. Repeat the process of adding modifiers with adding Vertical or Horizontal analyzers. For proper order of modifiers, pleas check provided example files. 

---

## Requirements

- Blender 4.0+ with Geometry Nodes support.
- Python 3.x with Pandas and Numpy libraries.

---

## License

Released under the **CC BY 3.0 License**, encouraging modifications and adaptations for academic and research purposes.

Acknowledgments: This toolset was developed under the GAČR EXPRO GX21-17092X grant and tested on early medieval Slavic pottery from the Czech Republic.
