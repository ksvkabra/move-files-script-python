import os
import shutil

src_folder = r"E:\pynative\reports\\"
dst_folder = r"E:\pynative\account\\"
file_name = 'sales.csv'

# check if file exist in destination
if os.path.exists(dst_folder + file_name):
    # Split name and extension
    data = os.path.splitext(file_name)
    only_name = data[0]
    extension = data[1]
    # Adding the new name
    new_base = only_name + '_new' + extension
    # construct full file path
    new_name = os.path.join(dst_folder, new_base)
    # move file
    shutil.move(src_folder + file_name, new_name)
else:
    shutil.move(src_folder + file_name, dst_folder + file_name)
