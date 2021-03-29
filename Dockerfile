FROM centos:latest
RUN yum install net-tools -y
Run yum install python3 -y
RUN pip3 install joblib
RUN pip3 install colorama
RUN pip3 install Flask
COPY Menu_App   Flask_App
EXPOSE 3000 8081
ENTRYPOINT ["python3" , "Flask_App/app.py"]
