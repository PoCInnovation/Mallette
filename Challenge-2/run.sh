sudo docker build -t challenge02_img .
sudo docker run -d -P --cap-add=SYS_PTRACE --name challenge02_cont challenge02_img
