# big_data_project
# Установка Docker:
sudo apt update  
sudo apt install apt-transport-https ca-certificates curl software-properties-common  
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -  
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"  
sudo apt update  
sudo apt install docker-ce  
sudo systemctl status docker  

# Установка Docker-compose:
sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose  
sudo chmod +x /usr/local/bin/docker-compose  
docker-compose --version  

# Настройка и подключение:
1. Скачаиваем архив с GitHub и закидываем в папку  
2. Скачиваем csv файлы с гугл диска по ссылке: https://drive.google.com/drive/folders/18oo2jku32MjNNKX1X3WQzZU3OKvjoAgy?usp=sharing и затем переносим эти файлы в папку csvfiles  
3.
