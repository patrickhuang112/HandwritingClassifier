import os
for i in os.listdir('words'):
    if i == '.DS_Store':
    	continue
    else:
	    print(i, len(os.listdir('words/' + i)))
    for ii in os.listdir('words/' + i):
        if ii == '.DS_Store':
            continue
        else:
            print('-', ii, len(os.listdir('words/' + i + '/' + ii)))

