#!/bin/bash
sphinx-apidoc -f -o ask_amy_api/ ../ask_amy
make html
rm -rf ../docs/*
cp -R _build/html/* ../docs
cp CNAME ../docs
touch ../docs/.nojekyll
