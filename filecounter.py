import os
from collections import defaultdict
from tabulate import tabulate

folder_path = r'C:\\Users\\arif9\\Desktop\\projects\\file-count' #modify this folder path according to need

def count_files_in_folders(directory, ignored_extensions, ignored_folders):
    folder_counts = []
    total_file_count = 0

    # Convert ignored extensions and folders to lowercase for case-insensitive comparison
    ignored_extensions = [ext.lower() for ext in ignored_extensions]
    ignored_folders = [folder.lower() for folder in ignored_folders]

    for dirpath, dirnames, filenames in os.walk(directory):
        # Ignore specified folders
        if any(ignored_folder in dirpath.lower() for ignored_folder in ignored_folders):
            continue

        # Filter out the ignored files
        filtered_filenames = [f for f in filenames if os.path.splitext(f)[1].lower() not in ignored_extensions]
        file_count = len(filtered_filenames)
        folder_counts.append((dirpath, file_count))
        total_file_count += file_count

    return folder_counts, total_file_count

# Specify the directory you want to count files in
ignored_files = ['.tmp', '.log']  # Add the extensions you want to ignore
ignored_dirs = ['.git', '.idea']  # Add folder names you want to ignore
folder_counts, total_files = count_files_in_folders(folder_path, ignored_files, ignored_dirs)

# Prepare data for tabulation
formatted_data = sorted(folder_counts)

# Add a total row
formatted_data.append(('Total', total_files))

# Print the results in a tabular format
print(tabulate(formatted_data, headers=['Folder Name', 'File Count'], tablefmt='grid'))
