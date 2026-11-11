FROM python:3.12-slim 

RUN mkdir /app 
WORKDIR /app 
COPY . /app
RUN python3 -m venv .venv && . .venv/bin/activate && python3 -m pip install flask

# CMD ["tail", "-f", "/dev/null"]
CMD [".venv/bin/python", "-m", "server"]

