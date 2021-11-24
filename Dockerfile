# donwloading Alpine OS with python
FROM python:3.8.5

# setting current working directory 
WORKDIR /usr/app/

# copying all contents from my current dir to workdir
COPY . .

# RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements_docker.txt

# EXPOSE 5000
ENTRYPOINT python app.py

# usefull command
# after adding all files and contents run the following command to build the container image
#  < docker build -t demo-dockerflask:latest . >
#  < docker images > ; check the image with the following command
#  < docker rmi -f $(docker images -a -q) > ; delete the image if there is something worng 
# 
# Build container from image
#  < docker run -t -p 5000:5000 demo-dockerflask >
#  < docker rm -f $(docker ps -a -q) > ; delete the container if there is something worng
#
# Browse 127.0.0.1:5000 for accessing webapps

# to run a container with detach mode 
#  < docker run -d -t -p 5000:5000 demo-dockerflask > 
# to access that running detached container
#  < docker exec -it docker_id/name bash >

    # launch and access a container 
    #  <ole@T:~$ docker run -it --rm alpine /bin/ash>
    #  (inside container) / # 
    # Options used above:
    #        --/bin/ash is Ash (Almquist Shell) provided by BusyBox
    #        --rm Automatically remove the container when it exits (docker run --help)
    #        --i Interactive mode (Keep STDIN open even if not attached)
    #        --t Allocate a pseudo-TTY

# deleting all cached images and builds or containers
#  < docker system prune -a >  -> all build cacche/stopped container/networks/images
#  < docker builder prune > -> deletes all dangling docker builds

# further reference 
# https://towardsdatascience.com/how-to-dockerize-an-existing-flask-application-115408463e1c
# https://felipefaria.medium.com/running-a-simple-flask-application-inside-a-docker-container-b83bf3e07dd5
# usefull link ->  https://stackoverflow.com/questions/26504846/copy-directory-to-another-directory-using-add-command