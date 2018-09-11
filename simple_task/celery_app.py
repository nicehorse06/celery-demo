# -*- coding: utf-8 -*-  
  
import time  
from celery import Celery  
  
# 指定消息中間件用 redis，URL 為 redis://127.0.0.1:6379
broker = 'redis://127.0.0.1:6379'  

# 指定存儲用 redis，URL為 redis://127.0.0.1:6379/0
backend = 'redis://127.0.0.1:6379/0'  
  
# 創建了一個 Celery 實例 app，名稱為 my_task
app = Celery('my_task', broker=broker, backend=backend)  
  
# 創建了一個 Celery 任務 add，當函數被 @app.task 裝飾後，就成為可被 Celery 調度的任務 
@app.task  
def add(x, y):  
    time.sleep(5)
    return x + y