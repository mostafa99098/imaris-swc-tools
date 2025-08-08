# Imaris SWC Tools

**Professional tools for importing and exporting SWC neuronal morphology files in Bitplane Imaris**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Imaris](https://img.shields.io/badge/Imaris-10.x-green.svg)](https://imaris.oxinst.com/)

##  Features

### Export Tools
- ** Batch Export** (ExportSWC_Batch.py) - Process multiple Imaris files automatically with recursive folder scanning
- ** Single Export** (ExportSWC_Single.py) - Export individual Filaments objects with manual selection

### Import Tools  
- ** Single File Import** (ImportSWC_Single.py) - Import individual SWC files with file picker dialog
- ** Folder Import** (ImportSWC_Folder.py) - Import SWC files from a selected folder

##  Requirements

- **Bitplane Imaris** 10.x or later
- **Python** 3.x (included with Imaris installation)
- **NumPy** (for coordinate transformations)
- **tkinter** (for GUI dialogs)

##  Installation

1. **Download the tools**:
   `ash
   git clone https://github.com/mostafa99098/imaris-swc-tools.git
   `

2. **Copy to Imaris XTensions folder**:
   - Copy all .py files to your Imaris XTensions directory
   - Default location: C:\Program Files\Bitplane\Imaris [version]\XT\python3\

3. **Restart Imaris** - The tools will appear in the XTensions menu

##  Usage

### Batch Export (Recommended)
1. Open Imaris and go to **Image Processing > XTensions > ExportSWC_Batch**
2. Select the root folder containing your .ims files
3. The tool will:
   - Recursively scan all subfolders
   - Process each .ims file automatically
   - Export SWC files with matching names
   - Preserve your folder structure

### Single File Export
1. Open your .ims file in Imaris
2. Go to **Image Processing > XTensions > ExportSWC_Single**
3. Select the Filaments object to export
4. Choose save location and filename

### Import SWC Files
1. **Single File**: Use ImportSWC_Single to select and import one SWC file
2. **Multiple Files**: Use ImportSWC_Folder to import all SWC files from a folder

##  File Structure

`
imaris-swc-tools/
 ExportSWC_Batch.py      #  Batch export tool (v2.0)
 ExportSWC_Single.py     #  Single export tool  
 ImportSWC_Single.py     #  Single file import
 ImportSWC_Folder.py     #  Folder import
 ImarisLib.py            #  Imaris API wrapper
 _utils.py               #  Utility functions
 README.md               #  This documentation
`

##  What's New in v2.0

-  **Batch Processing**: Automatically process multiple Imaris files
-  **Recursive Scanning**: Handle nested folder structures
-  **Auto-Detection**: Automatically find Filaments objects in Surpass scene
-  **Enhanced Error Handling**: Comprehensive logging and error reporting
-  **Improved UI**: Better file selection dialogs
-  **Preserved Structure**: Maintain folder hierarchy during batch processing

##  SWC Format

The tools support the standard SWC format for neuronal morphology:
`
# node_id  type  x  y  z  radius  parent_id
1         1     0  0  0  1.0     -1
2         3     1  0  0  0.8     1
...
`

##  Troubleshooting

**Common Issues:**
- **"No Filaments found"**: Ensure your Surpass scene contains Filaments objects
- **"Dataset not ready"**: Wait for Imaris to fully load the dataset before running tools
- **Import errors**: Check that SWC files follow the standard 7-column format

##  Contributing

Contributions are welcome! Please feel free to:
- Report bugs
- Suggest new features  
- Submit pull requests

##  License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

##  Author

**Mostafa Bakhshi** - [GitHub](https://github.com/mostafa99098)

##  Acknowledgments

- Bitplane for the Imaris software and XTensions framework
- The neuroscience community for SWC format standardization

---

 **If you find these tools useful, please consider giving this repository a star!**
