import os


# Creates the data directory
def create_directory(directory_name="Data"):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
    else:
        print(f'Directory {directory_name} already exist.')


# Create the queue and crawled files
def create_data_files(STARTING_URL="https://www.google.gr"):
    queue = "Data" + "/queue.txt"
    crawled = "Data" + "/crawled.txt"
    if not os.path.isfile(queue):
        write_file(queue, STARTING_URL)
    if not os.path.isfile(crawled):
        write_file(crawled, "")


# Write data to a file
def write_file(path, data):
    f = open(path, 'w')
    f.write(data)
    f.close()


# Add data onto an existing file
def append_to_file(path, data):
    with open(path, "a") as file:
        file.write(data + "\n")


# Delete the contents of a file
def delete_data(path):
    with open(path, "w"):
        pass


# # Read a file and convert each line to set items
# def file_to_set(file_name):
#     results = set()
#     with open(file_name, "rt") as file:
#         for line in file:
#             results.add(line.replace("\n", ""))
#     return results
#
#
# # Iterate through a set, each item will be a new line in the file
# def set_to_file(links, file):
#     # delete_data(file)  ############# to do ###########
#     for link in sorted(links):
#         append_to_file(file, link)
