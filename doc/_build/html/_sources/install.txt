.. _install:

*******************
Quick install guide
*******************

Install Docker
==============

To install docker on your specific OS, follow the instruction on the docker page: http://docs.docker.com/installation/

Install PEFIM idp using docker
==============================

Download the PEFIM docker project from: https://github.com/its-dirg/pefim_idp_docker

All files necessary to build the PEFIM idp image are located in the dockerfiles directory. To build the image run the script::

    dockerfiles/build.sh

If you want to test the PEFIM idp, you can use the example idp setup in the example directory.
Replace the metadata in **example/etc/metadata** with your metadata or change the metadata configuration in **example/etc/idp_config.py**.

To start the idp run the script::

    example/run.sh
