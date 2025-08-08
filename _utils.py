# Utility functions for Imaris plugins
# This file provides compatibility functions for the IOF-PyImaris plugin system

import functools
import traceback
import time


def exceptionPrinter(func):
    """
    Decorator to catch and print exceptions from Imaris plugin functions.
    This ensures that errors are visible to the user and don't crash Imaris.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error in function {func.__name__}:")
            print(traceback.format_exc())
            input("Press Enter to continue...")
            raise
    return wrapper


def getImaris(aImarisId):
    """
    Get Imaris application instance and related objects.
    
    Args:
        aImarisId: Imaris application ID
    
    Returns:
        tuple: (vImaris, V, scene) where:
            - vImaris: Imaris application object
            - V: Current dataset/volume
            - scene: Surpass scene object
    """
    try:
        import ImarisLib
        
        # Connect to Imaris
        vImarisLib = ImarisLib.ImarisLib()
        vImaris = vImarisLib.GetApplication(aImarisId)
        
        if vImaris is None:
            raise RuntimeError("Could not connect to Imaris. Make sure Imaris is running.")
        
        # Get the dataset
        V = vImaris.GetDataSet()
        if V is None:
            raise RuntimeError("No dataset loaded in Imaris.")
        
        # Get the surpass scene
        scene = vImaris.GetSurpassScene()
        if scene is None:
            raise RuntimeError("No surpass scene available in Imaris.")
        
        return vImaris, V, scene
        
    except ImportError as e:
        print("Error importing ImarisLib:")
        print(str(e))
        print("Make sure this script is run from within Imaris as a plugin.")
        time.sleep(4)
        raise
    except Exception as e:
        print(f"Error connecting to Imaris: {str(e)}")
        time.sleep(4)
        raise
