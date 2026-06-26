# Prod_ML

1-docker build -t flight-classifier.
2-docker run -p 8501:8501 flight-classifier
FROM -> Start with a machine
ENV -> Configure machine
WORKDIR -> Move into project folder
RUN -> Install stuff
COPY -> Bring in files
EXPOSE -> Declare network port
CMD -> Start application
