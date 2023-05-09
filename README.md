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
1. Скачаиваем архив с GitHub и разархивируем его в home 
2. Скачиваем csv файлы с гугл диска по ссылке: https://drive.google.com/drive/folders/18oo2jku32MjNNKX1X3WQzZU3OKvjoAgy?usp=sharing и затем переносим эти файлы в папку csvfiles  
3. Поднимаем docker-compose (cd hive; sudo docker-compose up)  
4. Переходим в dbeaver и устанавливаем коннект с базой Postgres (host:localhost; database:postgres; username:savelovba; password:123)  
5. Переходим в vscode, открываем папку python_scripts
6. Далее по очереди запускам скрипты  
1 скрипт - создание таблиц в БД  
2 скрипт - заполнение таблиц в БД  
3 скрипт - очистка данных (from stg to dds)  
4 скрипт - формирование витрины для гипотезы 1 (dm)   
5 скрипт - формирование витрины для гипотезы 2 (dm)  
6 скрипт - формирование витрины для гипотезы 3 (dm)  
7. Для визуализации витрин с помощью Grafana необходимо в браузере перейти по адресу http://localhost:3111 и установить соединение с базой Postgres (host:localhost; database:postgres; username:savelovba; password:123)  
