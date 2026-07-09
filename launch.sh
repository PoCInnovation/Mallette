#!/bin/sh

docker kill chall01
docker kill chall02
docker kill chall03
docker kill chall04

docker rm chall01
docker rm chall02
docker rm chall03
docker rm chall04

docker run --name chall01 -d -p 8000:8000 chal01_cont python manage.py runserver 0.0.0.0:8000
docker run --name chall02 -d --cap-add=SYS_PTRACE -p 2222:22 chal02_cont bash -c "/usr/sbin/sshd -D"
docker run --name chall03 -d -p 2020:22 chal03_cont bash -c "/usr/sbin/sshd -D"
docker run --name chall04 -d -p 8080:8080 chal04_cont bash -c "yes 1"

