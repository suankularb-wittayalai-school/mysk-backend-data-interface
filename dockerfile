FROM python:3.9

ARG B_PORT=5000
ARG B_HOST=0.0.0.0

ENV PORT=$B_PORT
ENV HOST=$B_HOST
# 
WORKDIR /code

# 
COPY ./requirements.txt ./requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

# 
COPY . .

# 
CMD ["python", "src/app.py"]

EXPOSE $B_PORT