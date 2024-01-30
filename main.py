from read import read_obs as ro
from plot import plot_obs as po
import xarray as xr
import numpy as np
import pandas as pd
import warnings
import sys
import os
import argparse

def main():
    # Create the parser
    obsparser = argparse.ArgumentParser(description='Process observational data.')

    # Add the arguments
    obsparser.add_argument('directory', metavar='directory', type=str, help='the path to the data directory')

    obsparser.add_argument('obstype', metavar='obstype', type=str, help='the type of observation (e.g., WOD, Cosmic-Ionosphere)')

    obsparser.add_argument('filetype', metavar='filetype', type=str, help='the file type (e.g., nc, hdf)')

    # Execute the parse_args() method
    args = obsparser.parse_args()

    # Read observations based on provided arguments
    try:
        obs_data = ro.read_obs(args.directory, args.obstype, args.filetype)
        print("Successfully read data.")
    except Exception as e:
        print(f"An error occurred: {e}")

    type = args.obstype
    
    plotparser = argparse.ArgumentParser(description='Plot observational data.')

    varoptions = po.get_plotvars(obs_data, type)
    
    print('Available variables: ' + str(varoptions))

    plotparser.add_argument('var', metavar='var', type=str, help='the variable to plot')

    plotparser.add_argument('savename', metavar='savename', type=str, help='filename of figure')

    # Execute the parse_args() method
    args = obsparser.parse_args()

    # Read observations based on provided arguments
    try:
        plot = plot_obs(obs_data, type, var)
        
        print("Successfully plotted data. Check figures directory for output.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()