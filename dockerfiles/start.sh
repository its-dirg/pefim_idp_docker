#!/bin/bash

/opt/pefim/tools/make_metadata.py /opt/pefim/etc/idp_config.py > /opt/pefim/etc/idp.xml

cd /opt/pefim/etc
pefim_idp idp_config
