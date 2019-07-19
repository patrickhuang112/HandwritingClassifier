import os

for i in os.listdir('words'):
    if i == '.DS_Store':
        continue

    if len(os.listdir('words/' + i)) < 10:
        to_delete = 'words/' + i
        os.system("rm -rf {} ".format(to_delete))
        print("deleted {}".format(to_delete))
        continue

    for ii in os.listdir('words/' + i):
        if ii == '.DS_Store':
            continue

        if len(os.listdir('words/' + i + '/' + ii)) < 20:
            to_delete = 'words/' + i + '/' + ii
            os.system("rm -rf {} ".format(to_delete))
            print("deleted {} ".format(to_delete))
    
        while len(os.listdir('words/' + i + '/' + ii)) > 20:
            os.system("rm {}".format('words/' + i + '/' + ii + '/' + (os.listdir('words/' + i + '/' + ii)[0])))
