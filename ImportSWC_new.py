#
#
#  Import SWC XTension  
#
#  @Mostafa Bakhshi
#
#    <CustomTools>
#      <Menu>
#       <Item name="SWC Importer 1.0" icon="Python3" tooltip="Calls the Imaris to import SWC">
#         <Command>Python3XT::XTImportSWC(%i)</Command>
#       </Item>
#      </Menu>
#    </CustomTools>


import ImarisLib
import time
import random
import numpy as np
import logging
# GUI imports
from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog,filedialog
import os 
logging.basicConfig(filename='', level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s') #add your filepath
def XTImportSWC(aImarisId):
	# Create an ImarisLib object
	vImarisLib = ImarisLib.ImarisLib()

	# Get an imaris object with id aImarisId
	vImaris = vImarisLib.GetApplication(aImarisId)

	if vImaris is None:
		print('Could not connect to Imaris!')
		time.sleep(10)
		return
	
	vFactory = vImaris.GetFactory()
	vFilaments = vFactory.ToFilaments(vImaris.GetSurpassSelection())
	root = Tk()
	root.withdraw()
	# Ask for a single SWC file instead of a directory
	swc_path = filedialog.askopenfilename(title='Select SWC file', filetypes=[('SWC files','*.swc'), ('All files','*.*')])
	root.destroy()
	if not swc_path: # dialog returns '' if cancelled
		print('No file selected')
		time.sleep(10)
		return
	print(swc_path)
	V = vImaris.GetDataSet()
	pixel_scale = np.array([V.GetSizeX() / (V.GetExtendMaxX() - V.GetExtendMinX()),
							V.GetSizeY() / (V.GetExtendMaxY() - V.GetExtendMinY()),
							V.GetSizeZ() / (V.GetExtendMaxZ() - V.GetExtendMinZ())])
	pixel_offset = np.array([V.GetExtendMinX(), V.GetExtendMinY(), V.GetExtendMinZ()])
	# ad-hoc fix Z-flip when |maxZ| < |minZ|
	if abs(V.GetExtendMinZ()) > abs(V.GetExtendMaxZ()):
		pixel_offset = np.array([V.GetExtendMinX(), V.GetExtendMinY(), V.GetExtendMaxZ()])
		pixel_scale[2] = -pixel_scale[2]
	
	# Import the selected file
	try:
		print('Importing: ' + swc_path)
		swc = np.loadtxt(swc_path)
		# Ensure 2D array even for a single-node SWC
		if swc.ndim == 1:
			swc = swc.reshape(1, -1)

		N = swc.shape[0]
		vFilaments = vImaris.GetFactory().CreateFilaments()
		vPositions = swc[:, 2:5].astype(float) / pixel_scale
		vPositions = vPositions + pixel_offset
		vRadii = swc[:, 5].astype(float)
		vTypes = np.zeros((N))  # (0: Dendrite; 1: Spine)
		vEdges = swc[:, [6, 0]]
		idx = np.all(vEdges > 0, axis=1)
		vEdges = vEdges[idx, :] - 1
		vTimeIndex = 0
		vFilaments.AddFilament(vPositions.tolist(), vRadii.tolist(), vTypes.tolist(), vEdges.tolist(), vTimeIndex)
		vFilamentIndex = 0
		vVertexIndex = 1
		vFilaments.SetBeginningVertexIndex(vFilamentIndex, vVertexIndex)
		# Name the filaments after the file
		try:
			vFilaments.SetName(os.path.basename(swc_path))
		except Exception:
			pass
		vScene = vImaris.GetSurpassScene()
		vScene.AddChild(vFilaments, -1)
		logging.info(f'Imported {os.path.basename(swc_path)}')
	except Exception as e:
		logging.error(f'Failed to import {os.path.basename(swc_path)}: {e}')
	print('SWC file imported')
