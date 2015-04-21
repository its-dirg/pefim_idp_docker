#!/bin/bash

apt-get update
apt-get install -y \
        libsasl2-dev \
        libldap2-dev \
        libssl-dev \
        wget \
        unzip \
	xmlsec1

# Create a directory for the pefim_idp src
mkdir /opt/pefim/src
cd /opt/pefim/src

Download and unzip pefim_idp
wget -O download.zip "https://github.com/its-dirg/pefim_idp/archive/master.zip"
unzip download.zip
rm download.zip
src_name=$(ls)
mv ${src_name} pefim_idp

# install the pefim idp
pip install git+https://github.com/HaToHo/pysaml2.git#egg=pysaml2
pip install -e /opt/pefim/src/pefim_idp/
pip install cherrypy==3.2.4
pip install python-ldap