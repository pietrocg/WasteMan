FROM python:3.9-bullseye
COPY ./requirements.txt /app/requirements.txt
WORKDIR /WasteMan
COPY . /WasteMan
RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
EXPOSE 8080
EXPOSE 3306
CMD ["python3", "app.py", "Config/config.ini"]