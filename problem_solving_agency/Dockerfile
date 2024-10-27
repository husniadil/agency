FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENV OPENAI_API_KEY=${OPENAI_API_KEY}

ENV GRADIO_SERVER_PORT=7860

ENV GRADIO_SERVER_ADDRESS=0.0.0.0

ENV RUN_GRADIO=true

CMD ["bash", "-c", "python agency.py"]
