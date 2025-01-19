# PDF to JPG Converter Tool

## Purpose
The **PDF to JPG Converter Tool** is a Python-based utility that converts all PDF files in a selected folder into high-quality JPEG images. It creates a new folder named `conversion` to store the resulting images, ensuring the output maintains the original PDF filenames (even Arabic names).

## Features
- Batch conversion of PDF files to JPEG images.
- Handles non-Latin filenames (e.g., Arabic).
- Outputs images with the same name as the original PDFs for easy organization.
- High-quality image output (300 DPI by default).
- Logs any errors encountered during the process.

## How to Use
1. Run the tool using Python.
2. Select the folder containing your PDF files when prompted.
3. The tool will convert all PDF files in the folder and save the JPEG images in a subfolder named `conversion`.
4. A completion message will be displayed, and any errors will be logged in `conversion/error_log.txt`.

## Requirements
To use this tool, you need the following:

### Python Libraries
Install the required Python libraries using the following command:
```bash
pip install -r requirements.txt
```

### Poppler
This tool uses **Poppler**, an external library, to handle PDF conversion.

#### For Windows:
1. Download and extract Poppler from [Poppler for Windows](http://blog.alivate.com.au/poppler-windows/) or [Poppler on GitHub](https://github.com/oschwartz10612/poppler-windows).
2. Add the `bin` directory (e.g., `C:\path\to\poppler\Library\bin`) to your system's PATH environment variable.

#### For Linux (Debian-based):
Install Poppler using the following command:
```bash
sudo apt-get install poppler-utils
```

#### For Linux (Arch-based):
Install Poppler using the following command:
```bash
sudo pacman -S poppler
```

## Files Included
- **main.py**: The Python script for the conversion process.
- **requirements.txt**: Contains the list of Python dependencies.

## Additional Information
The `bin` directory from the Poppler folder is essential for Windows users to enable the script to locate the necessary executables for PDF processing. Without it, the tool will not function properly. On Linux, the `poppler-utils` package provides the required utilities.

## Made by Hacko with Greed
A simple yet powerful tool for all your PDF-to-JPEG conversion needs!