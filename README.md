# 雷霆战机小程序脚本

## 介绍
雷霆战机小程序脚本，基于Python语言，实现了自动化的刷金币、积分功能。
### 功能
基于ui自动化，不存在修改数据，目前没有封号的风险。

## 使用
### 环境准备
基于airtest框架，需要安装airtest库，请参考[airtest安装文档](https://airtest.doc.io.netease.com/IDEdocs/3.1getting_started/AirtestIDE_install/)。
### 运行脚本
1. 打开雷霆战机小程序，并进入游戏界面。
2. 在airtest IDE中选择游戏画面，将画面嵌入ide中。
3. 进入游戏首页后，点击IDE中的运行按钮，即可运行脚本。


#### 刷金币
刷金币脚本中有个sleep可控制刷金币的间隔时间，比如调整为300秒，则脚本每隔300秒会自动挂机一次无尽模式，避免体力不足。

#### 积分
积分脚本默认挂机2000金币场，挂机10次。

