/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 50534
Source Host           : localhost:3306
Source Database       : company_parking_system

Target Server Type    : MYSQL
Target Server Version : 50534
File Encoding         : 65001

Date: 2018-06-12 14:18:23
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for administrater
-- ----------------------------
DROP TABLE IF EXISTS `administrater`;
CREATE TABLE `administrater` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL COMMENT '管理员账号',
  `password` varchar(255) DEFAULT NULL COMMENT '管理员密码',
  `gender` int(11) DEFAULT '0',
  `phone` varchar(255) DEFAULT NULL COMMENT '手机号',
  `question` varchar(255) DEFAULT NULL COMMENT '密保问题',
  `answer` varchar(255) DEFAULT NULL COMMENT '密保问题答案',
  `identity` int(11) DEFAULT NULL COMMENT '管理员身份 0：信息管理员   1：财务管理员  2：停车场管理员',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of administrater
-- ----------------------------
INSERT INTO `administrater` VALUES ('1', '123456', '123456', '0', '15639928163', null, null, null);

-- ----------------------------
-- Table structure for chargerules
-- ----------------------------
DROP TABLE IF EXISTS `chargerules`;
CREATE TABLE `chargerules` (
  `rid` int(11) NOT NULL COMMENT 'id主键',
  `nightprice` double DEFAULT NULL COMMENT '夜间收费价格',
  `nightbegintime` time NOT NULL COMMENT '夜间开始时间',
  `nightendtime` time NOT NULL COMMENT '夜间结束时间',
  `daybegintime` time DEFAULT NULL COMMENT '白天开始时间',
  `dayendtime` time DEFAULT NULL COMMENT '白天结束时间',
  `dayprice` double(10,0) DEFAULT NULL COMMENT '白天收费价格',
  `dayfirsthourprice` double DEFAULT NULL COMMENT '白天第一个小时收费价格',
  PRIMARY KEY (`rid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of chargerules
-- ----------------------------
INSERT INTO `chargerules` VALUES ('1', '5', '21:00:00', '07:00:00', '07:00:00', '21:00:00', '1', '2');

-- ----------------------------
-- Table structure for financial
-- ----------------------------
DROP TABLE IF EXISTS `financial`;
CREATE TABLE `financial` (
  `Fid` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `ParkPlaceID` int(11) DEFAULT NULL COMMENT '车位号',
  `chargetime` datetime DEFAULT NULL COMMENT '收费时间',
  `money` double DEFAULT NULL COMMENT '收费金额',
  PRIMARY KEY (`Fid`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of financial
-- ----------------------------
INSERT INTO `financial` VALUES ('1', '1', '2018-06-09 13:39:26', '12');
INSERT INTO `financial` VALUES ('2', '2', '2018-06-09 13:40:11', '10');
INSERT INTO `financial` VALUES ('3', '1', '2018-05-01 13:40:46', '2');
INSERT INTO `financial` VALUES ('4', '2', '2018-04-18 13:41:11', '3');

-- ----------------------------
-- Table structure for parkplace
-- ----------------------------
DROP TABLE IF EXISTS `parkplace`;
CREATE TABLE `parkplace` (
  `parkPlaceID` int(11) NOT NULL AUTO_INCREMENT COMMENT '车位的id作为主键默认自动递增',
  `lockStatus` int(11) DEFAULT '0' COMMENT '车位锁状态：0：关闭  1：打开',
  `parkPlaceType` int(11) DEFAULT NULL COMMENT '车位的类型：外部类型：1，内部类型：0',
  `useCarNumber` varchar(255) DEFAULT NULL COMMENT '车位分配的车id车牌号',
  PRIMARY KEY (`parkPlaceID`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8 COMMENT='车位表';

-- ----------------------------
-- Records of parkplace
-- ----------------------------
INSERT INTO `parkplace` VALUES ('1', '0', '0', null);
INSERT INTO `parkplace` VALUES ('2', '0', '1', null);
INSERT INTO `parkplace` VALUES ('3', '0', '1', null);
INSERT INTO `parkplace` VALUES ('4', '0', '0', null);
INSERT INTO `parkplace` VALUES ('5', '0', '0', null);
INSERT INTO `parkplace` VALUES ('6', '0', '1', null);
INSERT INTO `parkplace` VALUES ('7', '0', '1', null);
INSERT INTO `parkplace` VALUES ('8', '0', '0', null);
INSERT INTO `parkplace` VALUES ('9', '0', '1', null);
INSERT INTO `parkplace` VALUES ('10', '0', '0', null);
INSERT INTO `parkplace` VALUES ('11', '0', '0', null);
INSERT INTO `parkplace` VALUES ('12', '0', '1', null);

-- ----------------------------
-- Table structure for record
-- ----------------------------
DROP TABLE IF EXISTS `record`;
CREATE TABLE `record` (
  `rid` int(11) NOT NULL AUTO_INCREMENT COMMENT '车辆进出记录的id默认自增',
  `platenumber` varchar(255) DEFAULT NULL COMMENT '车牌号',
  `intime` datetime DEFAULT NULL COMMENT '车辆进入时间',
  `outtime` datetime DEFAULT NULL COMMENT '车辆离开时间',
  `vehicletype` int(11) DEFAULT NULL COMMENT '车辆类型 0：内部车   1:外部车',
  `feestatus` int(11) DEFAULT '0' COMMENT '缴费状态默认是没有缴费  0：没交 1：交',
  PRIMARY KEY (`rid`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COMMENT='车辆进出记录表，有关车辆缴费状态及缴费情况，通过此表可以获取财务记录情况';

-- ----------------------------
-- Records of record
-- ----------------------------
INSERT INTO `record` VALUES ('1', '豫A55555', '2018-05-29 11:17:17', '2018-05-29 11:23:21', '0', '0');
INSERT INTO `record` VALUES ('2', '豫B55555', '2018-05-28 11:35:48', '2018-05-29 11:35:55', '1', '1');
INSERT INTO `record` VALUES ('3', '京RD34F4', '2018-05-22 15:00:58', '2018-05-22 20:01:19', '1', '1');
INSERT INTO `record` VALUES ('4', '豫B82343', '2018-05-23 15:01:46', '2018-05-24 15:01:50', '0', '0');
INSERT INTO `record` VALUES ('5', '豫S34234', '2018-05-08 15:04:45', '2018-05-09 15:04:48', '1', '1');
INSERT INTO `record` VALUES ('6', '京G34553', '2018-05-24 15:05:58', '2018-05-24 18:06:01', '1', '1');

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
