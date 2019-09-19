#!/bin/bash

mkdir -p $CODEBUILD_SRC_DIR/build/build
cp -LR $CODEBUILD_SRC_DIR/lambdas $CODEBUILD_SRC_DIR/build/build/

echo "Building Lambdas..."
for dir in $CODEBUILD_SRC_DIR/build/build/lambdas/*
do
    pip3 install -r $dir/requirements.txt -t $dir > /dev/null
done

aws cloudformation package \
    --template-file $CODEBUILD_SRC_DIR/template.yml \
    --s3-bucket $BUILD_BUCKET \
    --output-template-file $CODEBUILD_SRC_DIR/build/build/deployment.yml \
