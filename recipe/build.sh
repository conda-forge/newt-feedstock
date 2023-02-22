#!/bin/bash

set -ex

autoconf

./configure \
  --prefix=$PREFIX \
  --without-python \
  --without-tcl

make
make install

cp $RECIPE_DIR/setup.py .
$PYTHON -m pip install . --no-deps -vv
