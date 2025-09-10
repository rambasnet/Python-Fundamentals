FROM python:3.12-slim

RUN apt update && apt upgrade -y \
    && apt install -y \
    pandoc texlive texlive-xetex\
    && apt clean \
    && /bin/rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["/bin/bash","-i","-c","\"$@\"","--"]