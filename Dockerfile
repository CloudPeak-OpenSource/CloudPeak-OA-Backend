FROM python:3.12

WORKDIR /app

COPY . .

RUN pip install poetry -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN poetry lock
RUN poetry export >> requirements.txt
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "4891" ]
EXPOSE 4891
