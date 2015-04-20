#!/bin/bash
#
# To debug your container:
#
#   DOCKERARGS="--entrypoint /bin/bash" bash -x ./run.sh
#

image=itsdirg/pefim_idp
name=pefim_idp

# Check if running on mac
if [ $(uname) = "Darwin" ]; then
    # Check so the boot2docker vm is running
    if [ $(boot2docker status) != "running" ]; then
        boot2docker start
    fi
    $(boot2docker shellinit)
else
    # if running on linux
    if [ $(id -u) -ne 0 ]; then
        sudo="sudo"
    fi
fi

${sudo} docker run --rm=true \
    --name ${name} \
    -v $PWD/etc:/opt/pefim/etc \
    -p 8088:8088 \
    $DOCKERARGS \
    -i -t \
    ${image}
