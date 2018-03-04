# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 09:10:58 2018

@author: peter
"""
import matplotlib.pyplot as plt
import sqlite3

conn=sqlite3.connect(r"C:\Users\peter\Desktop\bilibili\bilibili-spider\data.db")
favorite=conn.execute("select favorite from data order by id;").fetchall()
coin=conn.execute("select coin from data order by id;").fetchall()
plt.title("收藏数与硬币数关系图",fontproperties='SimHei',fontsize=25)
plt.xlabel("收藏数",fontproperties='SimHei',fontsize=15)
plt.ylabel("硬币数",fontproperties='SimHei',fontsize=15)
plt.plot(favorite,coin,'o')
conn.close()