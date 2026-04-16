FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p reports/allure-results

ENV ENV=qa

CMD behave -D env=$ENV -f allure_behave.formatter -o reports/allure-results