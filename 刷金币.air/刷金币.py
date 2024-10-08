# -*- encoding=utf8 -*-
__author__ = "22118"

from airtest.core.api import *

import time

auto_setup(__file__)
cont = 0;
current_time = time.time()
touch(Template(r"tpl1727976837903.png", record_pos=(-0.262, 0.778), resolution=(450, 844)))

while(1==1):
    wait(Template(r"tpl1727976850214.png", record_pos=(-0.138, 0.822), resolution=(450, 844)),999999)
    
    touch(Template(r"tpl1727976855057.png", record_pos=(-0.131, 0.822), resolution=(450, 844)))
    wait(Template(r"tpl1727976877335.png", record_pos=(0.0, 0.82), resolution=(450, 844)),999999)
    touch(Template(r"tpl1727976871351.png", record_pos=(0.002, 0.82), resolution=(450, 844)))
    wait(Template(r"tpl1727976896309.png", record_pos=(0.004, 0.827), resolution=(450, 844)),999999)
    touch(Template(r"tpl1727976903902.png", record_pos=(0.007, 0.827), resolution=(450, 844)))
    sleep(80.0)
    wait(Template(r"tpl1727977908109.png", record_pos=(0.002, 0.047), resolution=(450, 844)),99999999)
    touch(Template(r"tpl1727977299064.png", record_pos=(0.342, -0.069), resolution=(450, 844)))
    wait(Template(r"tpl1727976956785.png", record_pos=(0.002, 0.713), resolution=(450, 844)),999999)
    touch(Template(r"tpl1727976962626.png", record_pos=(0.002, 0.713), resolution=(450, 844)))
    sleep(10.0)
    if exists(Template(r"tpl1727976956785.png", record_pos=(0.002, 0.713), resolution=(450, 844))):
        wait(Template(r"tpl1727976956785.png", record_pos=(0.002, 0.713), resolution=(450, 844)),999999)
        touch(Template(r"tpl1727976962626.png", record_pos=(0.002, 0.713), resolution=(450, 844)))
    cont=cont+1
    print("总运行时间------------------毫秒：",((time.time()-current_time)))
    print("当前平均耗时------------------毫秒：",((time.time()-current_time)/cont))



