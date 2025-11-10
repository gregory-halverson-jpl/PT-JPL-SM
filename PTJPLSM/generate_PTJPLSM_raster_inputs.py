"""
Module: generate_PTJPLSM_raster_inputs.py
----------------------------------------
This module provides a function to generate all required raster inputs for the PT-JPL-SM model.
It loads or computes all necessary variables from spatial data sources and meteorological data,
returning a dictionary of Raster objects that can be directly passed to the PTJPLSM model
without requiring any side-loading of additional data.
"""
import logging
from typing import Dict, Union
from datetime import datetime

import numpy as np
import rasters as rt
from rasters import Raster, RasterGeometry
from GEOS5FP import GEOS5FP

from PTJPL import load_Topt, load_fAPARmax
from soil_capacity_wilting import load_field_capacity, load_wilting_point
from gedi_canopy_height import load_canopy_height

from .constants import *

logger = logging.getLogger(__name__)

def generate_PTJPLSM_raster_inputs(
        time_UTC: datetime,
        geometry: RasterGeometry,
        GEOS5FP_connection: GEOS5FP = None,
        resampling: str = RESAMPLING,
        field_capacity_directory: str = None,
        wilting_point_directory: str = None,
        canopy_height_directory: str = None
        ) -> Dict[str, Raster]:
    """
    Generate a dictionary of all required raster inputs for the PT-JPL-SM model.

    This function loads or computes all variables needed by the PTJPLSM model to run
    without requiring any side-loading of additional data. It provides a complete set
    of input rasters that can be directly passed to the model.

    Parameters
    ----------
    time_UTC : datetime
        UTC datetime for the observation
    geometry : RasterGeometry
        Spatial geometry defining the area and resolution for the rasters
    GEOS5FP_connection : GEOS5FP, optional
        GEOS-5 FP meteorological data connection. If None, a new connection will be created.
    resampling : str, optional
        Resampling method for spatial data (default from constants)
    field_capacity_directory : str, optional
        Directory containing field capacity data (default from soil_capacity_wilting)
    wilting_point_directory : str, optional
        Directory containing wilting point data (default from soil_capacity_wilting)
    canopy_height_directory : str, optional
        Directory containing canopy height data (default from gedi_canopy_height)

    Returns
    -------
    Dict[str, Raster]
        Dictionary containing all required raster inputs for PTJPLSM:
        - 'Ta_C': Air temperature in Celsius
        - 'RH': Relative humidity (0-1)
        - 'soil_moisture': Soil moisture
        - 'SWin_Wm2': Incoming shortwave radiation
        - 'Topt_C': Optimal plant temperature
        - 'fAPARmax': Maximum fraction of absorbed PAR
        - 'field_capacity': Soil field capacity
        - 'wilting_point': Soil wilting point
        - 'canopy_height_meters': Canopy height in meters

    Notes
    -----
    - This function loads all optional parameters that the PTJPLSM model can side-load,
      ensuring the model runs without additional data loading.
    - The returned rasters can be combined with observation-based inputs (NDVI, ST_C,
      emissivity, albedo) to provide a complete input set for PTJPLSM.
    - All rasters are resampled to match the provided geometry.

    Example
    -------
    ```python
    from datetime import datetime
    from rasters import RasterGeometry
    from PTJPLSM.generate_PTJPLSM_raster_inputs import generate_PTJPLSM_raster_inputs

    # Define spatial geometry and time
    geometry = RasterGeometry(...)  # Your target geometry
    time_UTC = datetime(2023, 6, 15, 12, 0, 0)

    # Generate all required inputs
    inputs = generate_PTJPLSM_raster_inputs(time_UTC, geometry)

    # Add observation-based inputs (NDVI, ST_C, emissivity, albedo)
    # ... load your observation data ...

    # Run PTJPLSM with complete inputs
    from PTJPLSM import PTJPLSM
    results = PTJPLSM(
        time_UTC=time_UTC,
        geometry=geometry,
        NDVI=NDVI,  # from observations
        ST_C=ST_C,  # from observations
        emissivity=emissivity,  # from observations
        albedo=albedo,  # from observations
        **inputs  # all generated inputs
    )
    ```
    """
    logger.info(f"generating PTJPLSM raster inputs for {time_UTC} UTC")
    
    inputs = {}
    
    # Create GEOS5FP connection if not provided
    if GEOS5FP_connection is None:
        logger.info("creating GEOS-5 FP connection")
        GEOS5FP_connection = GEOS5FP()
    
    # Load meteorological variables from GEOS-5 FP
    logger.info("loading air temperature (Ta_C) from GEOS-5 FP")
    inputs['Ta_C'] = GEOS5FP_connection.Ta_C(
        time_UTC=time_UTC,
        geometry=geometry,
        resampling=resampling
    )
    
    logger.info("loading relative humidity (RH) from GEOS-5 FP")
    inputs['RH'] = GEOS5FP_connection.RH(
        time_UTC=time_UTC,
        geometry=geometry,
        resampling=resampling
    )
    
    logger.info("loading soil moisture (SM) from GEOS-5 FP")
    inputs['soil_moisture'] = GEOS5FP_connection.SM(
        time_UTC=time_UTC,
        geometry=geometry,
        resampling=resampling
    )
    
    logger.info("loading incoming shortwave radiation (SWin_Wm2) from GEOS-5 FP")
    inputs['SWin_Wm2'] = GEOS5FP_connection.SWin(
        time_UTC=time_UTC,
        geometry=geometry,
        resampling=resampling
    )
    
    # Load vegetation parameters
    logger.info("loading optimal temperature (Topt_C)")
    inputs['Topt_C'] = load_Topt(geometry=geometry)
    
    logger.info("loading maximum fAPAR (fAPARmax)")
    inputs['fAPARmax'] = load_fAPARmax(geometry=geometry)
    
    # Load soil properties
    logger.info("loading field capacity")
    inputs['field_capacity'] = load_field_capacity(
        geometry=geometry,
        directory=field_capacity_directory,
        resampling=resampling
    )
    
    logger.info("loading wilting point")
    inputs['wilting_point'] = load_wilting_point(
        geometry=geometry,
        directory=wilting_point_directory,
        resampling=resampling
    )
    
    # Load canopy structure
    logger.info("loading canopy height")
    inputs['canopy_height_meters'] = load_canopy_height(
        geometry=geometry,
        source_directory=canopy_height_directory,
        resampling=resampling
    )
    
    logger.info("completed generating PTJPLSM raster inputs")
    
    return inputs