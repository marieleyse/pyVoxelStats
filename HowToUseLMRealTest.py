from pyVoxelStatsLM import pyVoxelStatsLM
import yappi

#yappi.start()
model_string = 'Flubet_scan ~ MMSE + Age + C(Gender_code)'
csv_file = '/data/data03/sulantha/VoxelStatsPaper/CSVs/DataCSV.csv'
mask_file = '/data/data03/sulantha/VoxelStatsPaper/Masks/mni_icbm152_t1_tal_nlin_sym_09a_mask2.mnc'
voxel_variables = ['Flubet_scan']
#subset_string = ''
file_type = 'minc'

lm = pyVoxelStatsLM(file_type, model_string, csv_file, mask_file, voxel_variables)
lm.set_up_cluster(profile_name='sgeov', workers=215, no_start=True)
#lm.set_up_cluster(profile_name='default')
results = lm.evaluate()

lm.save('/home/sulantha/Desktop/MMSE_Flu2.mnc', 'tvalues', 'MMSE')

# stats = yappi.get_func_stats()
# stats.save('pstatsreal.stats', type='pstat')
# with open('statsreal.stats', 'w') as f:
#     import pstats
#
#     ps = pstats.Stats('pstatsreal.stats', stream=f)
#     ps.sort_stats('cumtime')
#     ps.print_stats()