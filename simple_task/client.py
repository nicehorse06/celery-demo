# -*- coding: utf-8 -*-  
  
from celery_app import add  
  
# 异步任务  
result = add.delay(2, 8)  

result.ready()   # 使用 ready() 判断任务是否执行完毕   成功回傳True
result.get()	# 得到結果
  
print 'hello world'  