FROM python:slim

WORKDIR /usr/src/QueryTicket/

COPY requirements/requirements.txt ./

COPY QueryTicket/ ./

# RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install --no-cache-dir -i https://mirrors.huaweicloud.com/repository/pypi/simple -r requirements.txt

EXPOSE 80 

CMD [ "gunicorn", "-b", "0.0.0.0:80", "main:app"]