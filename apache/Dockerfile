FROM httpd:latest
COPY ./httpd.conf /usr/local/apache2/conf/httpd.conf
COPY ./httpd-ssl.conf /usr/local/apache2/conf/extra/httpd-ssl.conf
COPY ./server.crt /usr/local/apache2/conf/server.crt
COPY ./server.csr /usr/local/apache2/conf/server.csr
COPY ./server.key /usr/local/apache2/conf/server.key
