FROM python:3-slim

RUN set -ex \
    && pip install transifex-client \
    && rm -rf ~/.cache \
    && apt-get update \
    && apt-get install -y --no-install-recommends git make \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ADD entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
