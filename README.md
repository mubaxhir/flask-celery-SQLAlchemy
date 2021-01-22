# flask-celery-SQLAlchemy-rabbitmqServer

install rabbitmq server using link: 
https://www.rsupernova.com/how-to-install-and-manage-rabbitmq-on-ubuntu-20-04/


***$ sudo apt-get install rabbitmq-server
$sudo rabbitmqctl set_user_tags myuser administrator
$ sudo rabbitmqctl set_permissions -p / myuser ".*" ".*" ".*"
$ sudo rabbitmqctl list_permissions
$sudo rabbitmq-plugins enable rabbitmq_management
$sudo rabbitmqctl add_vhost myvhost
$ sudo service rabbitmq-server restart
$ celery -A celery_example.celery worker -l INFO
***

Thank you very much
