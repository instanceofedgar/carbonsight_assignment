import openstudio
import os

def modify_lpd_in_all_zones(osm_folder_path: str, target_lpd: float) -> None:
    """
    Modifies the Lighting Power Density (LPD) of all space types in all OSM files
    within the given folder.
    
    Parameters:
        osm_folder_path (str): Path to the folder containing OSM files.
        target_lpd (float): LPD (in W/m2) value to set for all space types in each OSM file.
    """
    # defines the path for the output folder
    output_folder = os.path.join(os.path.dirname(osm_folder_path), "modified_osm_files")
    
    # checks if the output folder exists and creates it if it does not
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # edit each OSM file in the input folder
    for osm_file in os.listdir(osm_folder_path):
        if osm_file.endswith(".osm"):
            osm_path = os.path.join(osm_folder_path, osm_file)
            model    = openstudio.model.Model.load(openstudio.path(osm_path))
            
            if model.is_initialized():
                model = model.get()
                for space_type in model.getSpaceTypes():
                    if space_type.lightingPowerPerFloorArea().is_initialized():
                        space_type.setLightingPowerPerFloorArea(target_lpd)
                
                # creates a modified osm file
                output_osm = os.path.join(output_folder, f"modified_{osm_file}")
                # saves new file in new specified folder
                model.save(openstudio.path(output_osm), True)
                
            else:
                # error handling
                raise RuntimeError(f"failed to load the OSM file: {osm_path}")