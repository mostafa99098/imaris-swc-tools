# Imaris SWC Tools v2.0

Enhanced tools for importing and exporting SWC (neuronal morphology) files in Bitplane Imaris.

## Features

### Export SWC v2.0
- **Single File Export**: Export selected Filaments object to SWC format
- **Batch Export**: Process entire folders and subfolders of .ims/.imsr files automatically
- **Recursive Processing**: Automatically finds all Imaris files in nested folder structures
- **Smart Output Organization**: Preserves folder structure in output to avoid file conflicts
- **Enhanced Logging**: Comprehensive error tracking and progress monitoring
- **Robust File Handling**: Improved coordinate transformations and edge case handling

### Import SWC v2.0
- **Single File Import**: Import individual SWC files as Filaments objects
- **User-Friendly Interface**: Simple file picker dialog
- **Automatic Naming**: Filaments objects named after source SWC file
- **Coordinate Conversion**: Proper scaling and offset handling for Imaris coordinates

## Installation

1. Copy the script files to your Imaris XTensions directory:
   - Windows: C:\Program Files\Bitplane\Imaris X.X\XT\python3\
   - macOS: /Applications/Imaris X.X/XT/python3/

2. Restart Imaris

3. The tools will appear in the Image Processing menu:
   - **SWC Exporter v2.0**: Export single selected Filaments
   - **SWC Exporter v2.0 (Batch)**: Batch process multiple files
   - **SWC Importer v2.0**: Import single SWC file

## Usage

### Export Workflow
1. **Single Export**: Select a Filaments object in Surpass, run "SWC Exporter v2.0"
2. **Batch Export**: Run "SWC Exporter v2.0 (Batch)", select input folder with .ims files, choose output folder

### Import Workflow
1. Load your image dataset in Imaris
2. Run "SWC Importer v2.0"
3. Select the SWC file to import
4. The Filaments object will be added to the Surpass scene

## Requirements

- Bitplane Imaris (tested on 10.2.0)
- Python environment with NumPy
- tkinter for GUI dialogs

## Changelog

### v2.0 (August 2025)
- **NEW**: Batch processing with recursive folder scanning
- **NEW**: Preserves folder structure in batch output
- **NEW**: Enhanced error handling and logging
- **NEW**: Automatic Filaments detection in batch mode
- **IMPROVED**: Single file import interface (file picker instead of folder picker)
- **IMPROVED**: Coordinate transformation robustness
- **IMPROVED**: Memory management for large batch operations
- **FIXED**: Edge cases in SWC parsing and generation
- **FIXED**: File naming conflicts in batch mode

### v1.0 (Previous)
- Basic SWC export from selected Filaments
- Directory-based SWC import
- Basic coordinate transformations

## License

This project is developed for research purposes. Please cite appropriately when used in publications.

## Author

@Mostafa Bakhshi
