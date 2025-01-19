import os
import sys
import time
from pathlib import Path
from mimetypes import guess_type
from tkinter import Tk, filedialog
from pdf2image import convert_from_path
from concurrent.futures import ThreadPoolExecutor

# Check if running as a packaged .exe
if getattr(sys, 'frozen', False):
    poppler_path = os.path.join(sys._MEIPASS, "poppler", "bin")
else:
    poppler_path = os.path.join(os.path.dirname(__file__), "poppler", "bin")

os.environ["PATH"] += os.pathsep + poppler_path

def select_folder():
    root = Tk()
    root.withdraw()  # Hide the root window
    folder_path = filedialog.askdirectory(title="Select Folder Containing PDFs")
    return folder_path

def is_pdf(file_path):
    mime_type, _ = guess_type(file_path)
    return mime_type == 'application/pdf'

def convert_pdf_to_jpg(pdf_file, pdf_folder, output_folder, log_file):
    pdf_path = os.path.join(pdf_folder, pdf_file)
    try:
        pdf_path = pdf_path.encode('utf-8').decode('utf-8')  # Ensure proper Unicode handling
        images = convert_from_path(pdf_path, fmt='jpeg', dpi=300)

        for i, image in enumerate(images):
            output_path = os.path.join(output_folder, f"{Path(pdf_file).stem}_{i+1}.jpg")
            image.save(output_path, "JPEG")

        print(f"Converted: {pdf_file}")
    except Exception as e:
        error_message = f"Failed to convert {pdf_file}: {e}\n"
        print(error_message.strip())
        with open(log_file, "a", encoding="utf-8") as log:
            log.write(error_message)

def convert_pdfs_to_jpgs(pdf_folder):
    output_folder = os.path.join(pdf_folder, "conversion")
    try:
        os.makedirs(output_folder, exist_ok=True)
    except OSError as e:
        print(f"Error creating directory '{output_folder}': {e}")
        return

    try:
        pdf_files = [file for file in os.listdir(pdf_folder) if is_pdf(os.path.join(pdf_folder, file))]
    except UnicodeDecodeError as e:
        print(f"Error reading file names: {e}")
        return

    if not pdf_files:
        print("No PDF files found in the selected folder.")
        return

    print("Starting conversion...")
    log_file = os.path.join(output_folder, "error_log.txt")
    
    # Start the timer
    start_time = time.time()

    # Use ThreadPoolExecutor to convert multiple PDFs simultaneously
    with ThreadPoolExecutor() as executor:
        for pdf_file in pdf_files:
            executor.submit(convert_pdf_to_jpg, pdf_file, pdf_folder, output_folder, log_file)

    # End the timer
    end_time = time.time()
    total_time = end_time - start_time

    print("\n" + "="*50)
    print("MADE BY HACKO WITH GREED")
    print("="*50)
    print("Conversion completed!")
    print(f"Total time taken: {total_time:.2f} seconds")  # Display the total time

def main():
    folder_path = select_folder()
    if not folder_path:
        print("No folder selected. Exiting...")
        return

    convert_pdfs_to_jpgs(folder_path)

    # Prompt the user to press any key to exit
    input("Press any button to exit...")

if __name__ == "__main__":
    main()
