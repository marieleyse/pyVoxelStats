from pyVoxelStats.pyVoxelStatsLM import pyVoxelStatsLM



model_string = 'Flubet_scan ~ MMSE + Age + C(Gender_code)'
csv_file = '/data/data03/sulantha/VoxelStatsPaper/CSVs/DataCSV.csv'
mask_file = '/data/data03/sulantha/VoxelStatsPaper/Masks/mni_icbm152_t1_tal_nlin_sym_09a_mask2.mnc'
voxel_variables = ['Flubet_scan']
#subset_string = ''
file_type = 'minc'

lm = pyVoxelStatsLM(file_type, model_string, csv_file, mask_file, voxel_variables)
lm.enable_save_model()
lm.set_no_parallel(True)

lm.set_up_cluster()

#lm.set_up_cluster(profile_name='default')
results = lm.evaluate()

lm.save('/home/sulantha/Desktop/MMSE_Flu2_pyV.mnc', 'tvalues', 'MMSE')

