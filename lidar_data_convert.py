'''
用于批量把npy格式的点云数据转换成txt和pcd点云格式
'''
import os
import time
import numpy as np
import open3d
import sys
import argparse
from multiprocessing import Pool


def lidar_convert(velodyne_path, pcd_path, lidar_name):
    velodyne_flag = os.path.exists(velodyne_path)
    if (velodyne_flag == False):
        print("please input corrrect path!")

    try:
        per_velodyne_path = os.path.join(velodyne_path, lidar_name)
    except FileNotFoundError:
        print("reading velodyne_path path error")
    lidar_data = np.load(per_velodyne_path)
    print(lidar_data[:, :3].shape)
    print(lidar_data[:, :4].dtype)

    pcd = open3d.geometry.PointCloud()
    pcd.points = open3d.utility.Vector3dVector(lidar_data[:, :3])
    lidar_pcd_path = os.path.join(pcd_path, os.path.splitext(lidar_name)[0] + ".pcd")
    lidar_txt_path = os.path.join(pcd_path, os.path.splitext(lidar_name)[0] + ".txt")
    np.savetxt(lidar_txt_path, lidar_data)
    open3d.io.write_point_cloud(lidar_pcd_path, pcd)

if __name__ == '__main__':
    # 加入路径参数输入
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_velodyne", default="E:/Small_Obstacle_Dataset/lidar", type=str)
    parser.add_argument("--output_pcd", default="E:/Small_Obstacle_Dataset/result", type=str)

    args = parser.parse_args()

    # 获取视频列表,使用了函数式编程以及列表表达式
    lidar_list = list(filter(lambda x: x.endswith("npy"), os.listdir(args.input_velodyne)))

    # 多线程处理
    num_workers = 4
    pool = Pool(processes=num_workers)
    start_time = time.time()
    for lidar_name in lidar_list:
        if os.path.splitext(lidar_name)[1] == ".npy":
            print(lidar_name)
            pool.apply(lidar_convert, args=(args.input_velodyne, args.output_pcd, lidar_name))
    pool.close()
    pool.join()
    print("done")