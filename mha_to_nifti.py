import SimpleITK as sitk
mha_path='mr.nii'

nii_path='mr.mha'

img = sitk.ReadImage(nii_path)

sitk.WriteImage(img,mha_path)