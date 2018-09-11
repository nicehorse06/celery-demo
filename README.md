## 啟動一般的Celery Worker

```
celery -A celery_app worker --loglevel=info
```

執行 python client.py 觸及 tasks


## 啟動定時的 Celery Worker

```
celery -B -A celery_app worker --loglevel=info
```


### 參考資料

* [Celery - Distributed Task Queue](http://puremonkey2010.blogspot.com/2018/01/python-celery-distributed-task-queue.html)