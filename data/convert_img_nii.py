import os
import nibabel as nb

def list_files(directory, extension):
    return (f for f in os.listdir(directory) if f.endswith('.' + extension))

def my_makedirs(path):
    if not os.path.isdir(path):
        os.makedirs(path)

my_makedirs('iSEG/Training/T1')
my_makedirs('iSEG/Training/T2')
my_makedirs('iSEG/Training/label')
my_makedirs('iSEG/Testing/T1')
my_makedirs('iSEG/Testing/T2')

fname = '/root/BRATS/iSeg-2017-Training/'
files = list_files(fname, "img")
for file_name in files:
    print("Processing %s" % file_name)
    new_fname=os.path.join(fname, file_name)
    img = nb.load((new_fname))
    if 'T1' in new_fname:
        nb.save(img, 'iSEG/Training/T1/' + os.path.basename(new_fname).replace('.img', '.nii'))
    elif 'T2' in new_fname:
        nb.save(img, 'iSEG/Training/T2/' + os.path.basename(new_fname).replace('.img', '.nii'))
    elif 'label' in new_fname:
        nb.save(img, 'iSEG/Training/label/' + os.path.basename(new_fname).replace('.img', '.nii'))

fname = '/root/BRATS/iSeg-2017-Testing/'
files = list_files(fname, "img")
for file_name in files:
    print("Processing %s" % file_name)
    new_fname=os.path.join(fname, file_name)
    img = nb.load((new_fname))
    if 'T1' in new_fname:
        nb.save(img, 'iSEG/Testing/T1/' + os.path.basename(new_fname).replace('.img', '.nii'))
    elif 'T2' in new_fname:
        nb.save(img, 'iSEG/Testing/T2/' + os.path.basename(new_fname).replace('.img', '.nii'))
