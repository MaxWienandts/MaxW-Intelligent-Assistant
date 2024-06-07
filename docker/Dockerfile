# To buid: docker image build -t streamlit_llama2 .
# To run: docker run -p 8501:8501 streamlit_llama2
# https://docs.streamlit.io/deploy/tutorials/docker
# Streamlit app at: http://localhost:8501/

FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY *.gguf /app/
COPY *.py /app/
COPY *.pkl /app/

# The EXPOSE instruction informs Docker that the container listens on the specified network ports at runtime. Your container needs to listen to Streamlit’s (default) port 8501
EXPOSE 8501

# The HEALTHCHECK instruction tells Docker how to test a container to check that it is still working. Your container needs to listen to Streamlit’s (default) port 8501
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "streamlit_llama2.py", "--server.port=8501", "--server.address=0.0.0.0"]



