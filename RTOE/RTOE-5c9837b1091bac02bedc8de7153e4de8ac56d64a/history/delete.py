import os

def delete_empty_txt_files(directory):
    # Check if the directory exists
    if not os.path.isdir(directory):
        print(f"The directory {directory} does not exist.")
        return

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        # Construct the full file path
        file_path = os.path.join(directory, filename)

        # Check if it is a .txt file and if it is empty
        if filename.endswith('.txt') and os.path.isfile(file_path) and os.path.getsize(file_path) == 0:
            # Delete the empty .txt file
            os.remove(file_path)
            print(f"Deleted empty file: {file_path}")

# Replace 'your_directory_path' with the path to your directory
delete_empty_txt_files('C://Users//jakub//Documents//Paradox Interactive//Europa Universalis IV//mod\RTOE//history//countries')