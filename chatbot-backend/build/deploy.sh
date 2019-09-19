#!/bin/bash

aws cloudformation deploy \
    --stack-name $APPLICATION-$ENVIRONMENT \
    --template-file $CODEBUILD_SRC_DIR/build/build/deployment.yml \
    --s3-bucket $BUILD_BUCKET \
    --capabilities CAPABILITY_IAM CAPABILITY_NAMED_IAM \
    --parameter-overrides \
        "Application=$APPLICATION" \
        "Environment=$ENVIRONMENT" \
        "BitBucketRepo=$BITBUCKET_REPO" \
    --tags \
        "Application=$APPLICATION" \
        "Environment=$ENVIRONMENT" \
