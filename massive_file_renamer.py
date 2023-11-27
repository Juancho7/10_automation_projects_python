import os


# function to add a preffix
def rename_files__preffix(directory, preffix):
    file_list = os.listdir(directory)

    for file_name in file_list:
        new_name = f"{preffix}_{file_name}"

        previous_file_path = os.path.join(directory, file_name)
        new_file_path = os.path.join(directory, new_name)

        os.rename(previous_file_path, new_file_path)

        print(f"Renamed: {file_name} -> {new_name}")


dir_path = "/path/example/"
preffix = "the preffix"

rename_files__preffix(dir_path, preffix)


# function to add a suffix
def rename_files_suffix(directory, suffix):
    file_list = os.listdir(directory)

    for file_name in file_list:
        base_name, file_extension = os.path.splitext(file_name)

        new_name = f"{base_name}_{suffix}{file_extension}"

        previous_file_path = os.path.join(directory, file_name)
        new_file_path = os.path.join(directory, new_name)

        os.rename(previous_file_path, new_file_path)

        print(f"Renamed: {file_name} -> {new_name}")


dir_path = "/path/example/"
preffix = "the suffix"

rename_files_suffix(dir_path, preffix)


# function to add a date
def rename_files_with_date(directory, position, date_text):
    file_list = os.listdir(directory)

    position_lower = position.lower()

    if position_lower == "before" or position_lower == "after":
        for file_name in file_list:
            base_name, file_extension = os.path.splitext(file_name)

            if position == "before":
                new_name = f"{date_text}_{base_name}{file_extension}"
            else:
                new_name = f"{base_name}_{date_text}{file_extension}"

            previous_file_path = os.path.join(directory, file_name)
            new_file_path = os.path.join(directory, new_name)

            os.rename(previous_file_path, new_file_path)

            print(f"Renamed: {file_name} -> {new_name}")
    else:
        print("Position not valid! It has to be before or after.")


dir_path = "/path/example/"
date_text = "16-11-2023"

rename_files_with_date(dir_path, "before", date_text)
rename_files_with_date(dir_path, "after", date_text)
