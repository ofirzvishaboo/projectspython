def rewrite_file(file_path, new_content):
    try:
        with open(file_path, 'w') as file:
            file.write(new_content)
        print(f"File '{file_path}' has been rewritten successfully.")
    except IOError:
        print(f"An error occurred while rewriting the file '{file_path}'.")
