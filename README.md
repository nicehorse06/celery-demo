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

* [Asynchronous Tasks in Python - Getting Started With Celery](https://www.youtube.com/watch?v=fg-JfZBetpM)
	* 簡易的介紹celery，broker為rabbit mq
* [用 Celery 結合 Redis 或 RabbitMQ = 馬上開始使用 Task Queue (1)](https://www.andretw.com/2013/07/using-celery-right-now-and-more-best-practices-1.html)
* [celery有什么难理解的?](https://shangliuyan.github.io/2015/07/04/celery%E6%9C%89%E4%BB%80%E4%B9%88%E9%9A%BE%E7%90%86%E8%A7%A3%E7%9A%84/)
* [First steps with Django](https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html)
* [Example Django project using Celery](https://github.com/celery/celery/tree/master/examples/django/)
* [How to use the @shared_task decorator for class based tasks](https://stackoverflow.com/questions/21233089/how-to-use-the-shared-task-decorator-for-class-based-tasks)
