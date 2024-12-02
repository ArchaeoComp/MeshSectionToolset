# MeshSectionToolset

An open-source toolkit for archaeologists and researchers to explore 3D artifacts, especially pottery. This project simplifies morphometric analysis by leveraging Blender's Geometry Nodes and Python scripting.

---

## Description

MeshSectionToolset facilitates the semi-automated generation of virtual cross-sections for 3D models. Designed for non-standard, asymmetrical, handmade artifacts like pottery, it extracts morphometric data and exports it for further analysis. The toolset is optimized for speed, precision, and accessibility to researchers with minimal programming experience.
**Note**: Basic knowledge of 3D concepts and Blender software is required.

---

## Features

### Virtual Cross-Sections
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
   - Use the `Extract_modd_data.py` script:
     - **Line 4**: Set the path to your Python library.
     - **Line 11**: Specify the Blender collection containing analyzed 3D slices.
     - **Line 20**: Define the output path for the exported `.csv` data.

---

## Requirements

- Blender 4.0+ with Geometry Nodes support.
- Python 3.x with Pandas and Numpy libraries.

---

## License

Released under the **CC BY 3.0 License**, encouraging modifications and adaptations for academic and research purposes.

Acknowledgments: This toolset was developed under the GAČR EXPRO GX21-17092X grant and tested on early medieval Slavic pottery from the Czech Republic.
