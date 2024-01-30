import xarray as xr
import numpy as np
import pandas as pd
import warnings
import sys
import os

# set number of file handling
def read_obs(directory, obstype, filetype):
    check_obstype(obstype)
    check_filetype(filetype)

    if obstype == 'AIRS':
        return handle_AIRS(directory, filetype)
    elif obstype == 'Cosmic-Ionosphere':
        return handle_CI(directory, filetype)
    elif obstype == 'GPS':
        return handle_GPS(directory, filetype)
    elif obstype == 'Ionosphere':
        return handle_Ion(directory, filetype)
    elif obstype == 'WOD':
        return handle_WOD(directory, filetype)
    elif obstype == 'mixed':
        return handle_mix(directory, filetype)
    else:
        return handle_gen(directory, filetype)


        
    
def check_obstype(obstype):
    # List of valid types
    valid_obstypes = ['AIRS', 'Cosmic-Ionosphere', 'WOD', 'GPS', 'Ionosphere', 'mixed', 'generic']

    # Check if the provided type is in the list of valid types
    if obstype not in valid_obstypes:
        raise ValueError(f"Invalid obs type '{obstype}'. Expected one of {valid_obstypes}.")

def check_filetype(filetype):
    # List of valid types
    valid_filetype = ['nc','hdf']

    # Check if the provided type is in the list of valid types
    if filetype not in valid_filetype:
        raise ValueError(f"Invalid file type '{valid_filetype}'. Expected one of {valid_filetype}.")
        
def checksize(directory):
    files = os.listdir(directory)

    if len(files) > 10000:
        warnings.warn(f"The directory contains {len(files)} files, which exceeds the recommended limit of 10,000, so this processing may be slow.")


def handle_AIRS(directory, filetype):
    checksize(directory)
    # Figure out hdf issue
    obs = xr.open_mfdataset(directory + '*' + filetype)
    return obs
    
def handle_GPS(directory, filetype): 
    checksize(directory)
    
    obs = xr.open_mfdataset(directory + '*' + filetype, combine='nested', concat_dim='OL_vec', chunks={'OL_vec': 9649})
    obs = obs.drop_dims('OL_par')
    return obs
    
    
def handle_CI(directory, filetype):
    checksize(directory)
    # combines along MS_alt
    obs = xr.open_mfdataset(directory + '*' + filetype)
    return obs
    
def handle_WOD(directory, filetype):
    checksize(directory)
    # combines along time
    obs = xr.open_mfdataset(directory + '*' + filetype)
    return obs
    
def handle_Ion(directory, filetype):
    checksize(directory)
    
    obs = xr.open_mfdataset(directory + '*' + filetype, combine='nested', concat_dim='MSL_alt')
    return obs


    