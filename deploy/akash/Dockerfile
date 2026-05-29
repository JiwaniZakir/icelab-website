# ICE Lab Hermes content agent — extends official Hermes image with gh + content CLI deps.
FROM ghcr.io/nousresearch/hermes-agent:latest

USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
    gh git \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir bibtexparser \
    google-cloud-pubsub google-api-python-client google-auth

COPY deploy/akash/entrypoint.sh /opt/ice-lab/entrypoint.sh
RUN chmod +x /opt/ice-lab/entrypoint.sh

ENV MESSAGING_CWD=/data/icelab-website
ENV HERMES_HOME=/opt/data

WORKDIR /data/icelab-website

ENTRYPOINT ["/opt/ice-lab/entrypoint.sh"]
CMD ["gateway", "run"]
