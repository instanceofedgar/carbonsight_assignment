# Assignement - Lighting Power Density (LPD) Measure for OpenStudio Files
## Prepared by: Edgar Lopez

## Overview

This assignment consists of a measure that modifies the Lighting Power Density (LPD) of all space types for OpenStudio Model (`.osm`) files. The modifications are performed using a Python script and OpenStudio SDK libraries (source: https://openstudio-sdk-documentation.s3.amazonaws.com/index.html)


## Files

- `lighting_measure.ipynb`: A Jupyter Notebook that uses the `modify_lpd_in_all_zones` function from the `openstudio_measures.py` script.
- `openstudio_measures.py`: A Python script containing the function to modify the LPD values in `.osm` files.
- `/osm_files/`: A folder containing `.osm` files to be processed.


## Requirements

command to install required packages:
    ```
    pip install openstudio
    ```


## Usage

1. **Prepare your `.osm` files**: Place your `.osm` files in the `/osm_files/` directory. This directory should be at the same level as your script and notebook files.

2. **Run the Jupyter Notebook**:
    - Open `lighting_measure.ipynb` in Jupyter Notebook.
    - Modify the `osm_folder_path` variable to point to the directory containing your `.osm` files.
    - Set the desired Lighting Power Density (`target_ldp`).
    - Run the cells to process the `.osm` files.


## Details

- **`openstudio_measures.py`**:
  - `modify_lpd_in_all_zones(osm_folder_path: str, target_lpd: float) -> None`:
    - **Parameters**:
      - `osm_folder_path` (str): Path to the folder containing `.osm` files.
      - `target_lpd` (float): New LPD value (in W/m²) to set for all space types in each `.osm` file.
    - **Functionality**:
      - Creates a new folder `modified_osm_files` adjacent to the input folder.
      - Modifies the LPD values in all `.osm` files and saves them in the `modified_osm_files` folder.
