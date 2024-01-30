import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import xarray as xr
import numpy as np
import pandas as pd
import sys

# set number of file handling
def get_plotvars(obs, obstype):
    vars = list(obs.keys())
    
    if type == 'AIRS':
        return None
    elif type == 'Cosmic-Ionosphere':
        items_to_remove = {'GEO_lat', 'GEO_lon'} 
        vars = [item for item in vars if item not in items_to_remove]
        return vars
    elif type == 'GPS':
        return None
    elif type == 'Ionosphere':
        items_to_remove = {'GEO_lat', 'GEO_lon'} 
        vars = [item for item in vars if item not in items_to_remove]
        return vars
    elif type == 'WOD':
        return vars
    elif type == 'mixed':
        return None
    else:
        return None

def plot_obs(obs, obstype, var, savename):

    if obstype == 'AIRS':
        return plot_AIRS(obs, var, savename)
    elif obstype == 'Cosmic-Ionosphere':
        return plot_CI(obs, var, savename)
    elif obstype == 'GPS':
        return plot_GPS(obs, var, savename)
    elif obstype == 'Ionosphere':
        return plot_Ion(obs, var, savename)
    elif obstype == 'WOD':
        return plot_WOD(obs, var, savename)
    elif obstype == 'mixed':
        return plot_mix(obs, var, savename)
    else:
        return plot_gen(obs, var, savename)

def plot_AIRS(obs, var, savename):
    return False
    
def plot_GPS(obs, var, savename): 
    return False
    
    
def plot_CI(obs, var, savename):
    if var == 'OCC_azi':
        unit = ' [deg]'
    elif var == 'TEC_cal':
        unit = ' [TECU]'
    else:
        unit = ' [el/cm3]'
        
    plt.figure(figsize=(12, 6))
    plt.plot(obs['MS_alt'], obs[var], label=var)
    plt.xlabel('MSL_alt')
    plt.ylabel(var + unit)
    plt.title(var + ' vs. MSL_alt')
    plt.legend()
    plt.savefig('./figures/' + savename + '.png', dpi=300, bbox_inches='tight')
    plt.show()
    return True


def plot_WOD(obs, var, savename):
    if var == 'sla_filtered' or var == 'adt_filtered':
        unit = ' [m]'
    else:
        unit = ''
        
    plt.figure(figsize=(12, 6))
    ax = plt.axes(projection=ccrs.PlateCarree())  # PlateCarree is a common projection for global maps
    ax.coastlines()
    ax.set_global()

    # Plotting cycle data
    scatter = ax.scatter(obs['longitude'], obs['latitude'], c=obs[var], cmap='viridis', marker='o')

    # Adding a color bar
    plt.colorbar(scatter, ax=ax, orientation='vertical', label=var + unit)

    # Adding titles and labels
    plt.title('Geographical Distribution of '  + var)
    plt.savefig('./figures/' + savename + '.png', dpi=300, bbox_inches='tight')
    plt.show()
    return True
    
def plot_Ion(obs, var, savename):
    if var == 'OCC_azi':
        unit = ' [deg]'
    elif var == 'TEC_cal':
        unit = ' [TECU]'
    else:
        unit = ' [el/cm3]'
        
    plt.figure(figsize=(12, 6))
    plt.plot(obs['MS_alt'], obs[var], label=var)
    plt.xlabel('MSL_alt')
    plt.ylabel(var + unit)
    plt.title(var + ' vs. MSL_alt')
    plt.legend()
    plt.savefig('./figures/' + savename + '.png', dpi=300, bbox_inches='tight')
    plt.show()
    return True


    