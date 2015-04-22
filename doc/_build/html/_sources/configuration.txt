.. _configuration:

***************
PEFIM idp setup
***************

Setting up PEFIM idp docker container

Docker volume structure
=======================

To run a PEFIM idp using the docker image, you need to bind a volume to **/opt/pefim/etc** in the container.
This volume will act as the working directory of the PEFIM idp and contain all necessary files to the idp.

The start.sh script
-------------------

In the volume root, a file named **start.sh** must exist. This file is the starting point of the application and is
responsible of starting the PEFIM idp.

An example of a start script::

    #!/bin/bash

    make_metadata.py idp_config.py > idp.xml
    pefim_idp idp_config

This creates a metadata file of the config file idp_config.py and starts the PEFIM idp.
