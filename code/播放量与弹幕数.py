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
plt.plot(favorite,coin)
conn.close()