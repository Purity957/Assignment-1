# This program reads a file and writes a modified version to a new file.
# It also handles errors if the file doesn't exist or can't be read.

def simple_file_modifier():
    # Ask the user for the name of the file to read
    filename = input("Enter the name of the file: ")

    try:
        # Try to open the file and read its content
        with open(filename, 'r') as file:
            content = file.read()

        # Add a simple message at the beginning of the content
        modified_content = "Modified File Content:\n" + content

        # Write the modified content to a new file
        new_filename = "new_" + filename
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)

        print("✅ File has been modified and saved as:", new_filename)

    except FileNotFoundError:
        print("❌ Error: File not found. Please check the filename and try again.")
    except Exception as e:
        print("❌ Error: Could not read or write the file.", str(e))

# Run the function
simple_file_modifier()

