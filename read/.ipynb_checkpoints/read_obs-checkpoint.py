import xarray as xr
import numpy as np
import pandas as pd
import sys

def read_obs(directory, type):
    types = ['AIRS', 'Cosmic-Ionosphere', 'WOD', 'GPS', 'Ionosphere']
    obs = xr.open_mfdataset(directory + '*.nc', combine='nested', concat_dim='OL_vec')

def checktype(type):
    # List of valid types
    valid_types = ['AIRS', 'Cosmic-Ionosphere', 'WOD', 'GPS', 'Ionosphere']

    # Check if the provided type is in the list of valid types
    if type not in valid_types:
        raise ValueError(f"Invalid type '{type}'. Expected one of {valid_types}.")

def handle_AIRS(directory):

def handle_GPS(directory):

def handle_CI(directory):

def handle_WOD(directory):

def handle_Ion(directory):


    