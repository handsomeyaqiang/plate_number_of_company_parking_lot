#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# 省份简称训练
import sys
import os
import time
import random
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from PIL import Image

class predict:
    def __init__(self):
        self.SIZE = 1280
        self.WIDTH = 32
        self.HEIGHT = 40
        self.iterations = 400
        self.SAVER_DIR_DIGIT = "../resources/model/digit/"
        self.SAVER_DIR_PROVINCE = "../resources/model/province/"
        self.SAVER_DIR_LETTER = "../resources/model/letter/"
        self.TRAIN_DIR = "../resources/train-images/training-set/"
        self.VALIDATION_DIR = "../resources/train-images/validation-set/"
        self.PREDICT_DIR = "../resources/images/splitplateimages/"
        self.digit_lables = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                             'J', 'K', 'L',
                             'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.digit_Train_Dirs = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", 'A', 'B', 'C', 'D', 'E', 'F', 'G',
                                 'H', 'J', 'K',
                                 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.province_labels = ['川', '鄂', '赣', '甘', '贵', '桂', '黑', '沪', '冀', '津', '京', '吉', '辽',
                                '鲁', '蒙', '闽', '宁', '青', '琼', '陕', '苏', '晋', '皖', '湘', '新', '豫',
                                '渝', '粤', '云', '藏', '浙']
        self.letter_lables = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L',
                              'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.provice_NUM_CLASSES = len(self.province_labels)
        self.digit_NUM_CLASSES = len(self.digit_lables)
        self.seletter_NUM_CLASSES = len(self.letter_lables)

        # 定义输入节点，对应于图片像素值矩阵集合和图片标签(即所代表的数字)
        self.x = tf.placeholder(tf.float32, shape=[None, self.SIZE])
        self.y_ = tf.placeholder(tf.float32, shape=[None, self.digit_NUM_CLASSES])
        self.x_image = tf.reshape(self.x, [-1, self.WIDTH, self.HEIGHT, 1])


    # 定义卷积函数
    def conv_layer(self, inputs, W, b, conv_strides, kernel_size, pool_strides, padding):
        L1_conv = tf.nn.conv2d(inputs, W, strides=conv_strides, padding=padding)
        L1_relu = tf.nn.relu(L1_conv + b)
        return tf.nn.max_pool(L1_relu, ksize=kernel_size, strides=pool_strides, padding='SAME')


    # 定义全连接层函数
    def full_connect(self, inputs, W, b):
        return tf.nn.relu(tf.matmul(inputs, W) + b)


    def predict_license(self):
        license_num = ""
        for p in range(3):
            if p == 0:
                with tf.Session() as sess:
                    saver = tf.train.import_meta_graph("%smodel.ckpt.meta" % (self.SAVER_DIR_PROVINCE))
                    model_file = tf.train.latest_checkpoint(self.SAVER_DIR_PROVINCE)
                    saver.restore(sess, model_file)
                    print(tf.all_variables)
                    # 第一个卷积层
                    W_conv1 = sess.graph.get_tensor_by_name("W_conv1:0")
                    b_conv1 = sess.graph.get_tensor_by_name("b_conv1:0")
                    conv_strides = [1, 1, 1, 1]
                    kernel_size = [1, 2, 2, 1]
                    pool_strides = [1, 2, 2, 1]
                    L1_pool = self.conv_layer(self.x_image, W_conv1, b_conv1, conv_strides, kernel_size, pool_strides,
                                         padding='SAME')

                    # 第二个卷积层
                    W_conv2 = sess.graph.get_tensor_by_name("W_conv2:0")
                    b_conv2 = sess.graph.get_tensor_by_name("b_conv2:0")
                    conv_strides = [1, 1, 1, 1]
                    kernel_size = [1, 1, 1, 1]
                    pool_strides = [1, 1, 1, 1]
                    L2_pool = self.conv_layer(L1_pool, W_conv2, b_conv2, conv_strides, kernel_size, pool_strides,
                                         padding='SAME')

                    # 全连接层
                    W_fc1 = sess.graph.get_tensor_by_name("W_fc1:0")
                    b_fc1 = sess.graph.get_tensor_by_name("b_fc1:0")
                    h_pool2_flat = tf.reshape(L2_pool, [-1, 16 * 20 * 32])
                    h_fc1 = self.full_connect(h_pool2_flat, W_fc1, b_fc1)

                    # dropout
                    keep_prob = tf.placeholder(tf.float32)

                    h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

                    # readout层
                    W_fc2 = sess.graph.get_tensor_by_name("W_fc2:0")
                    b_fc2 = sess.graph.get_tensor_by_name("b_fc2:0")

                    # 定义优化器和训练op
                    conv = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)
                    nProvinceIndex = 0
                    for n in range(1, 2):
                        path = self.PREDICT_DIR + "%s.jpg" % n
                        img = Image.open(path)
                        width = img.size[0]
                        height = img.size[1]

                        img_data = [[0] * self.SIZE for i in range(1)]
                        for h in range(0, height):
                            for w in range(0, width):
                                if img.getpixel((w, h)) < 190:
                                    img_data[0][w + h * width] = 1
                                else:
                                    img_data[0][w + h * width] = 0

                        result = sess.run(conv, feed_dict={self.x: np.array(img_data), keep_prob: 1.0})
                        max1 = 0
                        max2 = 0
                        max3 = 0
                        max1_index = 0
                        max2_index = 0
                        max3_index = 0
                        # 获取前三个概率最大的省份及其索引
                        for j in range(self.provice_NUM_CLASSES):
                            if result[0][j] > max1:
                                max1 = result[0][j]
                                max1_index = j
                                continue
                            if (result[0][j] > max2) and (result[0][j] <= max1):
                                max2 = result[0][j]
                                max2_index = j
                                continue
                            if (result[0][j] > max3) and (result[0][j] <= max2):
                                max3 = result[0][j]
                                max3_index = j
                                continue
                        nProvinceIndex = max1_index
                        print("概率：  [%s %0.2f%%]    [%s %0.2f%%]    [%s %0.2f%%]" % (
                            self.province_labels[max1_index], max1 * 100, self.province_labels[max2_index], max2 * 100,
                            self.province_labels[max3_index], max3 * 100))
                    print("省份简称是: %s" % self.province_labels[nProvinceIndex])
                    license_num += self.province_labels[nProvinceIndex]
            elif p == 1:
                with tf.Session() as sess:
                    saver = tf.train.import_meta_graph("%smodel.ckpt.meta" % (self.SAVER_DIR_LETTER))
                    model_file = tf.train.latest_checkpoint(self.SAVER_DIR_LETTER)
                    saver.restore(sess, model_file)
                    # 第一个卷积层
                    W_conv1 = sess.graph.get_tensor_by_name("W_conv1:0")
                    b_conv1 = sess.graph.get_tensor_by_name("b_conv1:0")
                    conv_strides = [1, 1, 1, 1]
                    kernel_size = [1, 2, 2, 1]
                    pool_strides = [1, 2, 2, 1]
                    L1_pool = self.conv_layer(self.x_image, W_conv1, b_conv1, conv_strides, kernel_size, pool_strides, padding='SAME')

                    # 第二个卷积层
                    W_conv2 = sess.graph.get_tensor_by_name("W_conv2:0")
                    b_conv2 = sess.graph.get_tensor_by_name("b_conv2:0")
                    conv_strides = [1, 1, 1, 1]
                    kernel_size = [1, 1, 1, 1]
                    pool_strides = [1, 1, 1, 1]
                    L2_pool = self.conv_layer(L1_pool, W_conv2, b_conv2, conv_strides, kernel_size, pool_strides, padding='SAME')

                    # 全连接层
                    W_fc1 = sess.graph.get_tensor_by_name("W_fc1:0")
                    b_fc1 = sess.graph.get_tensor_by_name("b_fc1:0")
                    h_pool2_flat = tf.reshape(L2_pool, [-1, 16 * 20 * 32])
                    h_fc1 = self.full_connect(h_pool2_flat, W_fc1, b_fc1)

                    # dropout
                    keep_prob = tf.placeholder(tf.float32)

                    h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

                    # readout层
                    W_fc2 = sess.graph.get_tensor_by_name("W_fc2:0")
                    b_fc2 = sess.graph.get_tensor_by_name("b_fc2:0")

                    # 定义优化器和训练op
                    conv = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)
                    for n in range(2, 3):
                        path = self.PREDICT_DIR + "%s.jpg" % n
                        img = Image.open(path)
                        width = img.size[0]
                        height = img.size[1]

                        img_data = [[0] * self.SIZE for i in range(1)]
                        for h in range(0, height):
                            for w in range(0, width):
                                if img.getpixel((w, h)) < 190:
                                    img_data[0][w + h * width] = 1
                                else:
                                    img_data[0][w + h * width] = 0

                        result = sess.run(conv, feed_dict={self.x: np.array(img_data), keep_prob: 1.0})

                        max1 = 0
                        max2 = 0
                        max3 = 0
                        max1_index = 0
                        max2_index = 0
                        max3_index = 0
                        for j in range(self.letter_NUM_CLASSES):
                            if result[0][j] > max1:
                                max1 = result[0][j]
                                max1_index = j
                                continue
                            if (result[0][j] > max2) and (result[0][j] <= max1):
                                max2 = result[0][j]
                                max2_index = j
                                continue
                            if (result[0][j] > max3) and (result[0][j] <= max2):
                                max3 = result[0][j]
                                max3_index = j
                                continue
                        if n == 3:
                            license_num += "-"
                        license_num = license_num + self.letter_lables[max1_index]
                        print("概率：  [%s %0.2f%%]    [%s %0.2f%%]    [%s %0.2f%%]" % (
                            self.letter_lables[max1_index], max1 * 100, self.letter_lables[max2_index], max2 * 100,
                            self.letter_lables[max3_index],
                            max3 * 100))
                    print("城市代号是: 【%s】" % license_num)
            else:
                with tf.Session() as sess:
                    sess = tf.InteractiveSession()
                    saver = tf.train.import_meta_graph("%smodel.ckpt.meta" % (self.SAVER_DIR_DIGIT))
                    model_file = tf.train.latest_checkpoint(self.SAVER_DIR_DIGIT)
                    saver.restore(sess, model_file)
                    # 第一个卷积层
                    W_conv1 = sess.graph.get_tensor_by_name("W_conv1:0")
                    b_conv1 = sess.graph.get_tensor_by_name("b_conv1:0")
                    conv_strides = [1, 1, 1, 1]
                    kernel_size = [1, 2, 2, 1]
                    pool_strides = [1, 2, 2, 1]
                    L1_pool = self.conv_layer(self.x_image, W_conv1, b_conv1, conv_strides, kernel_size, pool_strides, padding='SAME')

                    # 第二个卷积层
                    W_conv2 = sess.graph.get_tensor_by_name("W_conv2:0")
                    b_conv2 = sess.graph.get_tensor_by_name("b_conv2:0")
                    conv_strides = [1, 1, 1, 1]
                    kernel_size = [1, 1, 1, 1]
                    pool_strides = [1, 1, 1, 1]
                    L2_pool = self.conv_layer(L1_pool, W_conv2, b_conv2, conv_strides, kernel_size, pool_strides, padding='SAME')

                    # 全连接层
                    W_fc1 = sess.graph.get_tensor_by_name("W_fc1:0")
                    b_fc1 = sess.graph.get_tensor_by_name("b_fc1:0")
                    h_pool2_flat = tf.reshape(L2_pool, [-1, 16 * 20 * 32])
                    h_fc1 = self.full_connect(h_pool2_flat, W_fc1, b_fc1)

                    # dropout
                    keep_prob = tf.placeholder(tf.float32)

                    h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

                    # readout层
                    W_fc2 = sess.graph.get_tensor_by_name("W_fc2:0")
                    b_fc2 = sess.graph.get_tensor_by_name("b_fc2:0")

                    # 定义优化器和训练op
                    conv = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)
                    for n in range(3, 8):
                        path = self.PREDICT_DIR + "%s.jpg" % n
                        img = Image.open(path)
                        gray = img.convert("L")
                        width = gray.size[0]
                        height = gray.size[1]

                        img_data = [[0] * self.SIZE for i in range(1)]
                        for h in range(0, height):
                            for w in range(0, width):
                                if gray.getpixel((w, h)) < 190:
                                    img_data[0][w + h * width] = 1
                                else:
                                    img_data[0][w + h * width] = 0

                        result = sess.run(conv, feed_dict={self.x: np.array(img_data), keep_prob: 1.0})
                        max1 = 0
                        max2 = 0
                        max3 = 0
                        max1_index = 0
                        max2_index = 0
                        max3_index = 0
                        # 获取前三个概率最大的字符及其索引
                        for j in range(self.digit_NUM_CLASSES):
                            if result[0][j] > max1:
                                max1 = result[0][j]
                                max1_index = j
                                continue
                            if (result[0][j] > max2) and (result[0][j] <= max1):
                                max2 = result[0][j]
                                max2_index = j
                                continue
                            if (result[0][j] > max3) and (result[0][j] <= max2):
                                max3 = result[0][j]
                                max3_index = j
                                continue

                        max_license_index = max1_index
                        print("概率：  [%s %0.2f%%]    [%s %0.2f%%]    [%s %0.2f%%]" % (
                            self.digit_lables[max1_index], max1 * 100, self.digit_lables[max2_index], max2 * 100, self.digit_lables[max3_index],
                            max3 * 100))
                        print("车牌号" + str(n) + "是: %s" % self.digit_lables[max_license_index])
                        license_num += self.digit_lables[max_license_index]
        print(license_num)
        return license_num

if __name__ == '__main__':
    p = predict()
    p.predict_license()
