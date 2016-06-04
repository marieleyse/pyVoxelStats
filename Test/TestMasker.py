from Util.Masker import Masker

masker = Masker('nifti', 'VoxelStatsTestData/Masks/FullBrain.nii')
image_masked = masker.__mask_image('VoxelStatsTestData/NIFTY/I300779.nii')
masker.save_image_from_data(image_masked, 'Test/MincWrite.nii')
