from Util.StatsUtil import Dataset, StringModel, LM
from Util.Masker import Masker
from Util.VoxelOperation import VoxelOperation

string_model = 'A ~ e + C_d + C(f)'
data_file = 'VoxelStatsTestData/CSV/Data.csv'
mask_file = 'VoxelStatsTestData/Masks/FullBrain.mnc'
voxel_vars = ['A', 'C_d']
filter_string = 'b > 1'

string_model_obj = StringModel(string_model, voxel_vars)
data_set = Dataset(data_file, filter_string=filter_string, string_model_obj=string_model_obj)
masker = Masker('minc', mask_file)
stats_model = LM(string_model_obj)

voxel_op = VoxelOperation(string_model_obj, data_set, masker, stats_model)
voxel_op.set_up_cluster()
voxel_op.set_up()
voxel_op.execute()
res = voxel_op.results.get_results()
masker.save_image_from_data(res['tvalues']['C_d'], 'pyVS_output.mnc')
