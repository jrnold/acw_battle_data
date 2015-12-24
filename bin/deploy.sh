#!/bin/bash
DATA_DIR=data
DATAPACKAGE=$DATA_DIR/datapackage.json
BUCKET=data.jrnold.me/acw_battle_data
REGION=us-east-1
TAR_FILE=

version=$(jq -r .version $DATAPACKAGE)
tarfile=acw_battle_data-$version.tar.gz
zipfile=acw_battle_data-$version.zip

tar czf $tarfile -C $DATA_DIR .
zip -j $zipfile $DATA_DIR/*

aws s3 sync --delete --region $REGION $DATA_DIR s3://$BUCKET/v$version
aws s3 sync --exclude "*" --include $tarfile --include $zipfile --region $REGION . s3://$BUCKET

