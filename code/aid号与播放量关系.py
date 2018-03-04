# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 08:41:55 2018

@author: peter
"""
import matplotlib.pyplot as plt
import sqlite3

conn=sqlite3.connect(r"C:\Users\peter\Desktop\bilibili\bilibili-spider\data.db")
aid=conn.execute("select aid from data order by id;").fetchall()
view=conn.execute("select view from data order by id;").fetchall()
danmakeu=conn.execute("select danmaku from data order by id;").fetchall()
reply=conn.execute("select reply from data order by id;").fetchall()
plt.title("aid号与播放量关系图",fontproperties='SimHei',fontsize=25)
plt.xlabel("aid号",fontproperties='SimHei',fontsize=15)
plt.ylabel("播放量",fontproperties='SimHei',fontsize=15)
plt.plot(aid,view)
conn.close()