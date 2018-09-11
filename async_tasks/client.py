# -*- coding: utf-8 -*-  
  
from celery_app import task1  
from celery_app import task2  
from datetime import datetime, timedelta 
  
task1.add.apply_async(args=[2, 8])        # 也可用 task1.add.delay(2, 8)  
task2.multiply.apply_async(args=[3, 7])   # 也可用 task2.multiply.delay(3, 7)  

# task.delay 為 task.apply_async 的封裝，apply_async可以帶入更多參數

task1.add.apply_async(args=(2, 3), countdown=5)    # 5 秒后执行任务 

# 当前 UTC 时间再加 10 秒后执行任务 
task2.multiply.apply_async(args=[3, 7], eta=datetime.utcnow() + timedelta(seconds=10)) 

task2.multiply.apply_async(args=[3, 7], expires=10)    # 10 秒后过期 
  
print('hello world')