FROM debian:jessie

RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install mysql-server mysql-client
RUN service mysql start &&/usr/bin/mysqladmin -u root password password46387463248database
RUN apt-get -y install apache2 apache2-doc && service apache2 start
RUN apt-get -y install php5 php5-mysql libapache2-mod-php5 && update-rc.d -f apache2 enable &&service apache2 restart
ADD website/* /var/www/html/
ADD 000-default.conf /etc/apache2/sites-enabled/
RUN service mysql start && echo "create database app;use app;create table users( username varchar(30) NOT NULL, password varchar(32) NOT NULL, perm enum('user', 'admin') DEFAULT 'user');insert into users (username, password, perm) values('admin', '90decd40332624c7e4b223f82ba034fa', 'admin')" | mysql -u root -ppassword46387463248database
RUN service apache2 start
ADD start.sh /
CMD ./start.sh
#CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
RUN rm /var/www/html/index.html