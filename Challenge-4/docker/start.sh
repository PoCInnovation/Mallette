#!/bin/bash
/usr/sbin/service mysql start
/usr/sbin/apache2ctl -D FOREGROUND
