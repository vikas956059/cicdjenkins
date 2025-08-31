FROM python:3.9-alpine
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80
ENV PORT=80
CMD ["python", "app.py"]
