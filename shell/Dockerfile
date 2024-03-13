FROM alpine:latest
RUN apk update && apk add bash
WORKDIR /app
COPY app.sh .
RUN chmod +x app.sh
CMD ["bash", "app.sh"]