FROM gradle:4.8.1

USER root

WORKDIR /home/gradle/project

COPY src/reviews/ ./

ENV SERVICE_VERSION=v1

RUN gradle clean build

CMD ["/bin/bash"]
