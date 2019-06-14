## 需求安裝

```
pip -r requirements.txt
```


## 啟動一般的Celery Worker，

```
celery -A celery_app worker --loglevel=info

python client.py
```

## 啟動定時的 Celery Worker

```
celery -B -A celery_app worker --loglevel=info
```

### todo
* [django-celery-tutorial](https://github.com/twtrubiks/django-celery-tutorial)
* [docker-django-celery-tutorial](https://github.com/twtrubiks/docker-django-celery-tutorial)
### 參考資料

* [Celery - Distributed Task Queue](http://puremonkey2010.blogspot.com/2018/01/python-celery-distributed-task-queue.html)
* [Using Celery on Heroku](https://devcenter.heroku.com/articles/celery-heroku#celery-and-django)