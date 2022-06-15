ARG base_image=alpine:3.16.0

FROM $base_image AS core


ARG image_version=0.0
ARG agent_version=0.0
ARG version_file=VERSION
ARG agent_bin=newrelic-infra

RUN apk add --no-cache --upgrade \
    ca-certificates=20191127-r5 
