# 公司停车场车牌号自动识别系统
此分支项目开发的分支dev
#### 项目介绍
本项目是为了解决现在公司内部员工上下班停车不方便、停车慢、收费慢问题。本项目是一个公司停车场车牌号自动识别系统，能够检测到进出车辆并提取车辆牌照信息（含汉字字符、英文字母、阿拉伯数字及号牌颜色），进行记录，以及收费。

#### 软件架构
![项目的主架构](https://gitee.com/uploads/images/2018/0613/213006_6ab2966b_1800784.png "屏幕截图.png")
controller：是控制层包
dao：操作数据库包
front：前端开发包
service：业务类包
train：识别训练包
utils: 工具类包
entity: 实体类包
resources: 存放资源的文件目录

Entity层的结构：
![Entity层](https://gitee.com/uploads/images/2018/0613/213533_0b5039e3_1800784.png "屏幕截图.png")

Controller层的项目结构：
![Controller层的项目结构](https://gitee.com/uploads/images/2018/0613/214330_703857b9_1800784.png "屏幕截图.png")

Service层的项目结构：
![Service层的项目结构](https://gitee.com/uploads/images/2018/0613/213246_b0b1f0e8_1800784.png "屏幕截图.png")

Dao层的项目结构：
![Dao层的项目结构](https://gitee.com/uploads/images/2018/0613/213440_1560adb4_1800784.png "屏幕截图.png")

DaoImpl层的项目结构：
![DaoImpl层的项目结构](https://gitee.com/uploads/images/2018/0613/213452_a1536cb1_1800784.png "屏幕截图.png")

Resources资源目录结构：
![Resources资源目录结构](https://gitee.com/uploads/images/2018/0613/213507_44469ae4_1800784.png "屏幕截图.png")

train车牌识别模型的目录结构：


utils工具包结构：
![utils工具包结构](https://gitee.com/uploads/images/2018/0613/213422_e9a2e654_1800784.png "屏幕截图.png")




controller：ChargeController.py
	    FinancialController.py
            ParkPlaceController.py
	    StaffController.py
	    RecongiseController.py
	    VehicleRecordController.py
		
dao:  ChargeDao.py
      FinancialDao.py
      ParkPlaceDao.py
      RecongiseDao.py
      RecordDao.py
      StaffDao.py
      VehicleDao.py
	
entity:  ChargeRules.py
	 ParkPlace.py
	 Record.py
	 Staff.py
	 Vehicle.py
         Record.py
         Financial.py

service: ChargeService.py
	 FinancialService.py
	 ParkPlaceService.py
	 StaffService.py
	 RecongiseService.py
	 VehicleRecordService.py

utils: 存放工具类
train: 存放训练、切割、识别车牌的类
resources:   存放项目中使用的资源文件

#### 安装教程

1. xxxx
2. xxxx
3. xxxx

#### 使用说明

1. 本项目运行在python3.6

#### 参与贡献

1. Fork 本项目
2. 新建 Feat_xxx 分支
3. 提交代码
4. 新建 Pull Request
