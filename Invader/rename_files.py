import os

path = '//Games1/frames'
i = 0
for filename in os.listdir(path):
    try:
        os.rename(os.path.join(path, filename), os.path.join(path, 'frame_' + str(i) + '_delay-0.03s.png'))
        i = i + 1
    except FileExistsError:
        print("{} files have been modified".format(i))
        # print('all files names have been modified')
