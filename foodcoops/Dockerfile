FROM python:2-slim
ARG ODOO_VERSION=9.0

#######################
# System dependencies #
#######################
RUN apt update && \
        apt install -y libjpeg-dev zlib1g-dev libxml2-dev libxslt1-dev libxmlsec1-dev libsasl2-dev python-dev libldap2-dev libssl-dev libpq-dev python-psycopg2 python-passlib nodejs npm postgresql-client-11 git && \
        apt-get clean && rm -rf /var/lib/apt/lists/ && \
        npm install -g less

RUN adduser app
USER app
WORKDIR /home/app

############################
# Application dependencies #
############################
# - install Odoo
# - install Odoo dependencies
# - Reinstall psycopg2 due to bug with GLIBC
#   (see https://github.com/psycopg/psycopg2-wheels/issues/2)
# - FoodCoops dependencies
#   - XlsxWriter needed by the 'report_xlsx' module
#   - pysftp needed by the 'auto_backup' module
RUN git clone -b "$ODOO_VERSION" --single-branch --depth 1 https://github.com/odoo/odoo.git /home/app/odoo && \
        pip install --user -r odoo/requirements.txt && \
        pip install --user psycopg2 --upgrade && \
        pip install --user XlsxWriter pysftp && \
        rm -rf /home/app/.cache/pip
# - copy repo code
ADD . /home/app/
# Basic configuration of Odoo
RUN mkdir -p /home/app/.local/share/Odoo/ && mv odoo.conf /home/app/.local/share/Odoo/odoo.conf

VOLUME ["/home/app/.local/share/Odoo"]
EXPOSE 8069
CMD ./odoo/odoo.py --addons-path=odoo/addons,extra_addons,intercoop_addons,louve_addons \
        --without-demo=all \
        --config=/home/app/.local/share/Odoo/odoo.conf
