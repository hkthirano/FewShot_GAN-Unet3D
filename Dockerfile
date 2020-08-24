# docker build -t hirano:cd9.0cn7u16_ssh .
# docker run --gpus all -itd -P --shm-size 8G -v /data1/hirano/for_okita:/root/for_okita -v /data1/TsuyoshiData:/root/TsuyoshiData -v /data1/BRATS:/root/BRATS --name fewshotgan_for_okita hirano:cd9.0cn7u16_ssh /bin/bash


# どのイメージを基にするか
FROM nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04

# 作成したユーザの情報
LABEL maintainter="hoge"

# sshサーバをインストールします
RUN apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/sshd
# rootのパスワードをhogeに設定します。
RUN echo 'root:hoge' | chpasswd
# sshのrootでのアクセスを許可します
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# おまじない
# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]

# cudaのpathを通す
RUN echo 'export PATH=/usr/local/cuda/bin:${PATH}' >> ~/.bashrc
RUN echo 'export LD_LIBRARY_PATH=/usr/local/cuda/lib64:${LD_LIBRARY_PATH}' >> ~/.bashrc
