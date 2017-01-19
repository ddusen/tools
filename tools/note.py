
读取日志文件:
①. cd  /var/log/sync
②. tail syncservice.log -F


启动爬虫:
①. sudo su crawler
②. cd
③. ls   >>> crawler ENV
④. source ENV/bin/activate
⑤. cd crawler/common/
⑥. python manage.py runserver 0.0.0.0:8888

数据库端口映射