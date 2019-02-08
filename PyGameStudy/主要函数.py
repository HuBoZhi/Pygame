# -*- coding: utf-8 -*- 
# Time : 2019/1/29 18:00 
# Author : hubozhi
#
# pygame.cdrom	访问光驱
# pygame.cursors	加载光标
# pygame.display	访问显示设备
# pygame.draw	    绘制形状、线和点
# pygame.event	   管理事件
# pygame.font	   使用字体
# pygame.image	  加载和存储图片
# pygame.joystick	  使用游戏手柄或者 类似的东西
# pygame.key	   读取键盘按键
# pygame.mixer	   声音
# pygame.mouse	   鼠标
# pygame.movie	    播放视频
# pygame.music	    播放音频
# pygame.overlay	访问高级视频叠加
# pygame	       就是我们在学的这个东西了……
# pygame.rect	   管理矩形区域
# pygame.sndarray	操作声音数据
# pygame.sprite	操作移动图像
# pygame.surface	管理图像和屏幕
# pygame.surfarray	管理点阵图像数据
# pygame.time	管理时间和帧信息
# pygame.transform	缩放和移动图像

# pygame.display.set_mode((x,x),特性)
# x,x 分辨率
# 特性列表
# 标志位	          功能
# FULLSCREEN	  创建一个全屏窗口
# DOUBLEBUF	  创建一个“双缓冲”窗口，建议在HWSURFACE或者OPENGL时使用
# HWSURFACE	  创建一个硬件加速的窗口，必须和FULLSCREEN同时使用
# 2 OPENGL	      创建一个OPENGL渲染的窗口
# RESIZABLE	  创建一个可以改变大小的窗口
# NOFRAME	      创建一个没有边框的窗口