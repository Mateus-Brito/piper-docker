FROM bash:alpine3.15

RUN apk add wget git git-lfs
RUN adduser -D dev
COPY . /docker
RUN chmod +x /docker/download.sh
ENTRYPOINT ["/docker/download.sh"]
