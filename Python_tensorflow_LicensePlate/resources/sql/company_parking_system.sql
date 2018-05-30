/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50534
Source Host           : localhost:3306
Source Database       : company_parking_system

Target Server Type    : MYSQL
Target Server Version : 50534
File Encoding         : 65001

Date: 2018-05-30 14:47:53
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for parklock
-- ----------------------------
DROP TABLE IF EXISTS `parklock`;
CREATE TABLE `parklock` (
  `ParkLockID` int(11) NOT NULL AUTO_INCREMENT COMMENT '车位锁的id默认自动递增',
  `status` int(11) DEFAULT '0' COMMENT '车位锁的状态默认是关闭状态 0:关闭  1：打开',
  PRIMARY KEY (`ParkLockID`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8 COMMENT='车位锁表';

-- ----------------------------
-- Records of parklock
-- ----------------------------
INSERT INTO `parklock` VALUES ('1', '0');
INSERT INTO `parklock` VALUES ('2', '0');
INSERT INTO `parklock` VALUES ('3', '0');
INSERT INTO `parklock` VALUES ('4', '0');
INSERT INTO `parklock` VALUES ('5', '0');
INSERT INTO `parklock` VALUES ('6', '0');
INSERT INTO `parklock` VALUES ('7', '0');
INSERT INTO `parklock` VALUES ('8', '0');
INSERT INTO `parklock` VALUES ('9', '0');
INSERT INTO `parklock` VALUES ('10', '0');
INSERT INTO `parklock` VALUES ('11', '0');
INSERT INTO `parklock` VALUES ('12', '0');

-- ----------------------------
-- Table structure for parkplace
-- ----------------------------
DROP TABLE IF EXISTS `parkplace`;
CREATE TABLE `parkplace` (
  `parkPlaceID` int(11) NOT NULL AUTO_INCREMENT COMMENT '车位的id作为主键默认自动递增',
  `parkLockID` int(11) DEFAULT NULL COMMENT '车位的外键指向车位锁的id',
  `parkPlaceType` int(11) DEFAULT NULL COMMENT '车位的类型：外部类型：1，内部类型：0',
  `useCarNumber` varchar(255) DEFAULT NULL COMMENT '车位分配的车id车牌号',
  PRIMARY KEY (`parkPlaceID`),
  KEY `ParkLockID` (`parkLockID`),
  CONSTRAINT `parkplace_ibfk_1` FOREIGN KEY (`ParkLockID`) REFERENCES `parklock` (`ParkLockID`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8 COMMENT='车位表';

-- ----------------------------
-- Records of parkplace
-- ----------------------------
INSERT INTO `parkplace` VALUES ('1', '1', '0', null);
INSERT INTO `parkplace` VALUES ('2', '2', '1', null);
INSERT INTO `parkplace` VALUES ('3', '3', '1', null);
INSERT INTO `parkplace` VALUES ('4', '4', '0', null);
INSERT INTO `parkplace` VALUES ('5', '5', '0', null);
INSERT INTO `parkplace` VALUES ('6', '6', '1', null);
INSERT INTO `parkplace` VALUES ('7', '7', '1', null);
INSERT INTO `parkplace` VALUES ('8', '8', '0', null);
INSERT INTO `parkplace` VALUES ('9', '9', '1', null);
INSERT INTO `parkplace` VALUES ('10', '10', '0', null);
INSERT INTO `parkplace` VALUES ('11', '11', '0', null);
INSERT INTO `parkplace` VALUES ('12', '12', '1', null);

-- ----------------------------
-- Table structure for record
-- ----------------------------
DROP TABLE IF EXISTS `record`;
CREATE TABLE `record` (
  `RID` int(11) NOT NULL AUTO_INCREMENT COMMENT '车辆进出记录的id默认自增',
  `PNumber` varchar(255) DEFAULT NULL COMMENT '车牌号',
  `inTime` datetime DEFAULT NULL COMMENT '车辆进入时间',
  `outTime` datetime DEFAULT NULL COMMENT '车辆离开时间',
  `vehicletype` int(11) DEFAULT NULL COMMENT '车辆类型 0：内部车   1:外部车',
  `fee` double DEFAULT '0' COMMENT '停车所交费用默认为0.0',
  `feeStatus` int(11) DEFAULT '0' COMMENT '缴费状态默认是没有缴费  0：没交 1：交',
  PRIMARY KEY (`RID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COMMENT='车辆进出记录表，有关车辆缴费状态及缴费情况，通过此表可以获取财务记录情况';

-- ----------------------------
-- Records of record
-- ----------------------------
INSERT INTO `record` VALUES ('1', '豫A55555', '2018-05-29 11:17:17', '2018-05-29 11:23:21', '0', '0', '0');
INSERT INTO `record` VALUES ('2', '豫B55555', '2018-05-28 11:35:48', '2018-05-29 11:35:55', '1', '5.6', '1');
INSERT INTO `record` VALUES ('3', '京RD34F4', '2018-05-22 15:00:58', '2018-05-22 20:01:19', '1', '15', '1');
INSERT INTO `record` VALUES ('4', '豫B82343', '2018-05-23 15:01:46', '2018-05-24 15:01:50', '0', '0', '0');
INSERT INTO `record` VALUES ('5', '豫S34234', '2018-05-08 15:04:45', '2018-05-09 15:04:48', '1', '6.3', '1');
INSERT INTO `record` VALUES ('6', '京G34553', '2018-05-24 15:05:58', '2018-05-24 18:06:01', '1', '20', '1');

-- ----------------------------
-- Table structure for staff
-- ----------------------------
DROP TABLE IF EXISTS `staff`;
CREATE TABLE `staff` (
  `SID` varchar(50) NOT NULL COMMENT '员工号作为主键',
  `vehicleQuantity` int(11) DEFAULT '0' COMMENT '员工拥有的车数量',
  `name` varchar(255) DEFAULT NULL COMMENT '员工的姓名',
  `phoneNumber` varchar(255) DEFAULT NULL COMMENT '员工的手机号',
  `gender` int(11) DEFAULT '0' COMMENT '员工性别 male:0  female:1',
  `department` varchar(255) DEFAULT NULL COMMENT '员工部门',
  PRIMARY KEY (`SID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='这是一个员工的实体表';

-- ----------------------------
-- Records of staff
-- ----------------------------
INSERT INTO `staff` VALUES ('0001', '1', 'tom', '1539928163', '0', '开发部');
INSERT INTO `staff` VALUES ('0002', '1', 'Jike', '1565626854', '1', '销售部');
INSERT INTO `staff` VALUES ('0003', '0', 'rose', '1535456456', '1', '开发部');
INSERT INTO `staff` VALUES ('0004', '2', 'wang', '1545454242', '0', '研发部');
INSERT INTO `staff` VALUES ('0005', '1', 'mike', '1535445874', '0', '销售部');

-- ----------------------------
-- Table structure for vehicle
-- ----------------------------
DROP TABLE IF EXISTS `vehicle`;
CREATE TABLE `vehicle` (
  `PlateID` varchar(255) NOT NULL COMMENT '车牌号作为主键',
  `owner` varchar(255) DEFAULT NULL COMMENT '这个车的驾驶人（不一定是车主）',
  `Vehicle_identity` varchar(255) DEFAULT NULL COMMENT '车的唯一标识的机架号用UUID生成32位',
  `SID` varchar(255) DEFAULT NULL COMMENT '车对应的员工外键',
  PRIMARY KEY (`PlateID`),
  KEY `staffforeigner` (`SID`),
  CONSTRAINT `staffforeigner` FOREIGN KEY (`SID`) REFERENCES `staff` (`SID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='车辆表';

-- ----------------------------
-- Records of vehicle
-- ----------------------------
INSERT INTO `vehicle` VALUES ('京B82234', 'mike', 'SDFWSESGED', '0005');
INSERT INTO `vehicle` VALUES ('京B82343', 'wang', 'SSDFSDFESFS', '0004');
INSERT INTO `vehicle` VALUES ('豫A55555', 'Tome', 'SDHDSBIEFSH', '0001');
INSERT INTO `vehicle` VALUES ('豫B82343', 'wang', 'SFDSSESFSDF', '0004');
INSERT INTO `vehicle` VALUES ('豫B88888', 'Jike', 'SDFHIESEFISS', '0002');
