FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install --no-cache -r requirements.txt
EXPOSE 5000
CMD [ "python", "main.py" ]