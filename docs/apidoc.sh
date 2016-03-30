#!/bin/bash
rm source/proj*
sphinx-apidoc -f -e -P -M -o source/ ../proj/
