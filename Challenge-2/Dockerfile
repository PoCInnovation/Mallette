FROM ubuntu:14.04

RUN apt-get update && apt-get install -y openssh-server gdb gcc build-essential unzip vim sudo git
RUN mkdir /var/run/sshd
RUN echo 'root:P0CP0CP0C' | chpasswd
RUN echo 'pass \
pass \
ch2 \
42 \
69 \
21 \
1337 \
Y' | adduser ch2

RUN echo 'ch2:ch2' | chpasswd

RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
RUN wget http://onniquedesmeres.fr/Mallette/Challenge-2/archive.zip
RUN unzip archive.zip ; rm archive.zip
RUN mv POC.ascii /home/ch2/.POC.ascii ; echo "cat /home/ch2/.POC.ascii" >> /home/ch2/.bashrc
RUN make re -C step1/ ; mv step1/step1 /home/ch2/bin ; rm -rf step1
RUN mkdir /ch2 ; make re -C step2/ ; mv step2/step2 /ch2/step2 ; rm -rf step2
RUN chmod ou-wr /ch2 /etc /bin /root /proc /dev
RUN git clone https://github.com/longld/peda.git ~/.peda
RUN echo “source ~/.peda/peda.py” >> ~/.gdbinit
