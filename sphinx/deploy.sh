#!/bin/bash

make html
rm -rf ../docs/*
cp -R _build/html/* ../docs
touch ../docs/.nojekyll
