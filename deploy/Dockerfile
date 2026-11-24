FROM ubuntu:22.04
RUN openssl genrsa -out /etc/ssl/app.key 1024
RUN ssh-keygen -t dsa -f /root/.ssh/id_dsa -N ""
