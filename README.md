# lidar_data_convert
用于数据集中激光点云格式的转换

可以把一些数据集中用npy以及bin格式无法直接可视化的点云格式数据转换成pcd格式的点云方便可视化

执行方法： python lidar_data_convert.py --input_velodyne {待转换的原始点云数据路径} --output_pcd {转换后结果路径}

本程序 采用了多线程处理，直接输入待转换的原始点云数据路径，即可对路径中所有的点云数据进行格式转换
