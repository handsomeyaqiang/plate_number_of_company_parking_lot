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


class trainDigit:
    def __init__(self):
        self.SIZE = 1280
        self.WIDTH = 32
        self.HEIGHT = 40
        self.iterations = 400
        self.SAVER_DIR = "../resources/model/digit/"
        self.TRAIN_DIR = "../resources/train-images/training-set/"
        self.VALIDATION_DIR = "../resources/train-images/validation-set/"
        self.PREDICT_DIR = "../resources/images/splitplateimages/"
        self.digit_lables = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                             'J', 'K', 'L',
                             'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.digit_Train_Dirs = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", 'A', 'B', 'C', 'D', 'E', 'F', 'G',
                                 'H', 'J', 'K',
                                 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.digit_NUM_CLASSES = len(self.digit_lables)
        # 定义输入节点
        self.x = tf.placeholder(tf.float32, shape=[None, self.SIZE])
        self.y_ = tf.placeholder(tf.float32, shape=[None, self.digit_NUM_CLASSES])
        self.x_image = tf.reshape(self.x, [-1, self.WIDTH, self.HEIGHT, 1])

    # 卷积层函数
    def conv_layer(self, inputs, W, b, conv_strides, kernel_size, pool_strides, padding):
        L1_conv = tf.nn.conv2d(inputs, W, strides=conv_strides, padding=padding)
        L1_relu = tf.nn.relu(L1_conv + b)
        return tf.nn.max_pool(L1_relu, ksize=kernel_size, strides=pool_strides, padding='SAME')

    # 全连接层函数
    def full_connect(self, inputs, W, b):
        return tf.nn.relu(tf.matmul(inputs, W) + b)

    # 训练函数
    def train_license(self):
        time_begin = time.time()
        # 遍历获取训练图片的数量
        input_count = 0
        for dir_name in self.digit_Train_Dirs:
            dir = self.TRAIN_DIR + "%s/" % dir_name
            for rt, dirs, files in os.walk(dir):
                for filename in files:
                    input_count += 1

        # 定义对应维数和各维长度的数组
        input_images = np.array([[0] * self.SIZE for i in range(input_count)])
        input_labels = np.array([[0] * self.digit_NUM_CLASSES for i in range(input_count)])

        # 遍历训练目录生成图片及图片对应的标签数据
        index = 0
        hot = 0
        for dir_name in self.digit_Train_Dirs:
            dir = self.TRAIN_DIR + "%s/" % dir_name  # i为分类目录
            for rt, dirs, files in os.walk(dir):
                for filename in files:
                    filename = dir + filename
                    img = Image.open(filename)
                    gray = img.convert("L")
                    # 将图片转化为灰度图
                    width = gray.size[0]
                    height = gray.size[1]
                    for h in range(0, height):
                        for w in range(0, width):
                            # 将读取的图片数据的每行数据一次放入input_images中
                            # 通过这样的处理，使数字的线条变细，有利于提高识别准确率
                            if gray.getpixel((w, h)) > 230:
                                input_images[index][w + h * width] = 0
                            else:
                                input_images[index][w + h * width] = 1
                    # 是每张图片的标签对应的值为1其他的值为0 例如：[0,0,0,1,0]
                    input_labels[index][hot] = 1
                    # print(hot, input_labels[index])
                    index += 1
            hot += 1

        # 遍历获取预测图片的数量
        val_count = 0
        for dir_name in self.digit_Train_Dirs:
            dir = self.VALIDATION_DIR + "%s/" % dir_name
            for rt, dirs, files in os.walk(dir):
                for filename in files:
                    val_count += 1

        # 定义对应维数和各维长度的数组
        val_images = np.array([[0] * self.SIZE for i in range(val_count)])
        val_labels = np.array([[0] * self.digit_NUM_CLASSES for i in range(val_count)])

        # 遍历预测目录生成图片及图片对应的标签数据
        index = 0
        hot = 0
        for dir_name in self.digit_Train_Dirs:
            dir = self.VALIDATION_DIR + "%s/" % dir_name
            for rt, dirs, files in os.walk(dir):
                for filename in files:
                    filename = dir + filename
                    img = Image.open(filename)
                    gray = img.convert("L")
                    width = gray.size[0]
                    height = gray.size[1]
                    for h in range(0, height):
                        for w in range(0, width):
                            # 通过这样的处理，使数字的线条变细，有利于提高识别准确率
                            if gray.getpixel((w, h)) > 230:
                                val_images[index][w + h * width] = 0
                            else:
                                val_images[index][w + h * width] = 1
                    val_labels[index][hot] = 1
                    index += 1
            hot += 1

        with tf.Session() as sess:
            # 第一个卷积层
            W_conv1 = tf.Variable(tf.truncated_normal([8, 8, 1, 16], stddev=0.1), name="W_conv1")
            b_conv1 = tf.Variable(tf.constant(0.1, shape=[16]), name="b_conv1")
            conv_strides = [1, 1, 1, 1]
            kernel_size = [1, 2, 2, 1]
            pool_strides = [1, 2, 2, 1]
            L1_pool = self.conv_layer(self.x_image, W_conv1, b_conv1, conv_strides, kernel_size, pool_strides, padding='SAME')

            # 第二个卷积层
            W_conv2 = tf.Variable(tf.truncated_normal([5, 5, 16, 32], stddev=0.1), name="W_conv2")
            b_conv2 = tf.Variable(tf.constant(0.1, shape=[32]), name="b_conv2")
            conv_strides = [1, 1, 1, 1]
            kernel_size = [1, 1, 1, 1]
            pool_strides = [1, 1, 1, 1]
            L2_pool = self.conv_layer(L1_pool, W_conv2, b_conv2, conv_strides, kernel_size, pool_strides, padding='SAME')

            # 全连接层
            W_fc1 = tf.Variable(tf.truncated_normal([16 * 20 * 32, 512], stddev=0.1), name="W_fc1")
            b_fc1 = tf.Variable(tf.constant(0.1, shape=[512]), name="b_fc1")
            h_pool2_flat = tf.reshape(L2_pool, [-1, 16 * 20 * 32])
            h_fc1 = self.full_connect(h_pool2_flat, W_fc1, b_fc1)

            # dropout
            keep_prob = tf.placeholder(tf.float32)

            h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

            # readout层
            W_fc2 = tf.Variable(tf.truncated_normal([512, self.digit_NUM_CLASSES], stddev=0.1), name="W_fc2")
            b_fc2 = tf.Variable(tf.constant(0.1, shape=[self.digit_NUM_CLASSES]), name="b_fc2")

            # 定义优化器和训练op
            y_conv = tf.matmul(h_fc1_drop, W_fc2) + b_fc2
            cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=self.y_, logits=y_conv))
            train_step = tf.train.AdamOptimizer((1e-4)).minimize(cross_entropy)

            correct_prediction = tf.equal(tf.argmax(y_conv, 1), tf.argmax(self.y_, 1))
            accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

            # 初始化saver
            saver = tf.train.Saver()

            sess.run(tf.global_variables_initializer())

            time_elapsed = time.time() - time_begin
            print("读取图片文件耗费时间：%d秒" % time_elapsed)
            time_begin = time.time()

            print("一共读取了 %s 个训练图像， %s 个标签" % (input_count, self.digit_NUM_CLASSES))

            # 设置每次训练op的输入个数和迭代次数，这里为了支持任意图片总数，定义了一个余数remainder，譬如，如果每次训练op的输入个数为60，图片总数为150张，则前面两次各输入60张，最后一次输入30张（余数30）
            batch_size = 60
            batches_count = int(input_count / batch_size)
            remainder = input_count % batch_size
            print("训练数据集分成 %s 批, 前面每批 %s 个数据，最后一批 %s 个数据" % (batches_count + 1, batch_size, remainder))

            # 执行训练迭代
            for it in range(self.iterations):
                print("第" + str(it) + "次迭代开始......")
                # 这里的关键是要把输入数组转为np.array
                for n in range(batches_count):
                    train_step.run(feed_dict={self.x: input_images[n * batch_size:(n + 1) * batch_size],
                                              self.y_: input_labels[n * batch_size:(n + 1) * batch_size], keep_prob: 0.5})
                if remainder > 0:
                    start_index = batches_count * batch_size;
                    train_step.run(feed_dict={self.x: input_images[start_index:input_count - 1],
                                              self.y_: input_labels[start_index:input_count - 1], keep_prob: 0.5})

                # 完成五次迭代，判断准确度是否已达到99%并且判断
                # 迭代次数大于等于300轮，达到则退出迭代循环
                iterate_accuracy = 0
                if it % 5 == 0:
                    iterate_accuracy = accuracy.eval(feed_dict={self.x: val_images, self.y_: val_labels, keep_prob: 1.0})
                    print('第 %d 次训练迭代: 准确率 %0.5f%%' % (it, iterate_accuracy * 100))
                    if iterate_accuracy >= 0.99 and it >= 300:
                        break

            print('完成训练!')
            time_elapsed = time.time() - time_begin
            print("训练耗费时间：%d秒" % time_elapsed)

            # 保存训练模型
            if not os.path.exists(self.SAVER_DIR):
                print('不存在训练数据保存目录，现在创建保存目录')
                os.makedirs(self.SAVER_DIR)
            saver.save(sess, "%smodel.ckpt" % (self.SAVER_DIR))

    def predict(self):
        with tf.Session() as sess2:
            saver = tf.train.import_meta_graph("%smodel.ckpt.meta" % (self.SAVER_DIR))
            model_file = tf.train.latest_checkpoint(self.SAVER_DIR)
            saver.restore(sess2, model_file)
            # 第一个卷积层
            W_conv1 = sess2.graph.get_tensor_by_name("W_conv1:0")
            b_conv1 = sess2.graph.get_tensor_by_name("b_conv1:0")
            conv_strides = [1, 1, 1, 1]
            kernel_size = [1, 2, 2, 1]
            pool_strides = [1, 2, 2, 1]
            L1_pool = self.conv_layer(self.x_image, W_conv1, b_conv1, conv_strides, kernel_size, pool_strides, padding='SAME')

            # 第二个卷积层
            W_conv2 = sess2.graph.get_tensor_by_name("W_conv2:0")
            b_conv2 = sess2.graph.get_tensor_by_name("b_conv2:0")
            conv_strides = [1, 1, 1, 1]
            kernel_size = [1, 1, 1, 1]
            pool_strides = [1, 1, 1, 1]
            L2_pool = self.conv_layer(L1_pool, W_conv2, b_conv2, conv_strides, kernel_size, pool_strides, padding='SAME')

            # 全连接层
            W_fc1 = sess2.graph.get_tensor_by_name("W_fc1:0")
            b_fc1 = sess2.graph.get_tensor_by_name("b_fc1:0")
            h_pool2_flat = tf.reshape(L2_pool, [-1, 16 * 20 * 32])
            h_fc1 = self.full_connect(h_pool2_flat, W_fc1, b_fc1)

            # dropout
            keep_prob = tf.placeholder(tf.float32)

            h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

            # readout层
            W_fc2 = sess2.graph.get_tensor_by_name("W_fc2:0")
            b_fc2 = sess2.graph.get_tensor_by_name("b_fc2:0")

            # 定义优化器和训练op
            conv = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)
            license_num = ""
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

                result = sess2.run(conv, feed_dict={self.x: np.array(img_data), keep_prob: 1.0})
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
                    self.digit_lables[max1_index], max1 * 100, self.digit_lables[max2_index], max2 * 100, self.digit_lables[max3_index], max3 * 100))
                print("车牌号" + str(n) + "是: %s" % self.digit_lables[max_license_index])
                license_num += self.digit_lables[max_license_index]
        return license_num

if __name__ == '__main__':
    p = trainDigit()
    p.predict()
