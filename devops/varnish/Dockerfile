# syntax=docker/dockerfile:1
FROM varnish:7.6

LABEL maintainer="Meow <lol262711@gmail.com>" \
      org.label-schema.name="hange-gallery-varnish" \
      org.label-schema.description="Hange_Gallery Varnish image." \
      org.label-schema.vendor="Meow"

COPY etc/varnish.vcl /etc/varnish/default.vcl
