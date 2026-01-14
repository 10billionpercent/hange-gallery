# syntax=docker/dockerfile:1
FROM varnish:7.6

LABEL maintainer="Lol262711 <lol262711@gmail.com>" \
      org.label-schema.name="hange-gallery-varnish" \
      org.label-schema.description="hange-gallery Varnish image." \
      org.label-schema.vendor="Lol262711"

COPY etc/varnish.vcl /etc/varnish/default.vcl
