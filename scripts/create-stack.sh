#!/bin/sh
aws cloudformation create-stack \
    --stack-name ecs-fastapi \
    --template-body file://template.yml \
    --capabilities CAPABILITY_AUTO_EXPAND CAPABILITY_NAMED_IAM
