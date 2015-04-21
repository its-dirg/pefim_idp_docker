#!/bin/bash

make_metadata.py idp_config.py > idp.xml
pefim_idp idp_config