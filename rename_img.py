import os


def get_last_index(dir_path):
    list_images = []
    for file in os.listdir(dir_path):
        if file[:6] == 'image_':
            list_images.append(int(file[6:-4]))
    print(list_images)
    print(f'Last index:{max(list_images)}')
    return max(list_images)


dir_path = './rzd_traffic_lights_input/copy'
if os.path.exists(dir_path):
    print('Dirictory exist.')
    os.chdir(dir_path)
    print('CD dir')
    dir_path = os.getcwd()
    file_index = 0

    for filename in os.listdir(dir_path):
        print(filename)
        if filename.lower().endswith(('.jpg', '.jpeg')):
            print('OK')
            if filename[0:6] == 'image_':
                print('File allredy has been renamed')
            else:
                print('Need rename')
                # find last index and + 1
                file_index = get_last_index(dir_path) + 1
                new_name = 'image_' + str(file_index) + '.jpg'
                if os.path.isfile(new_name):
                    print("The file already exists")
                else:
                    # Rename the file
                    os.rename(filename, new_name)


        else:
            print('It\'s not JPG !')



