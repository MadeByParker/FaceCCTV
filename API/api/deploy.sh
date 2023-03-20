#!/bin/sh

# variables
aws_region="eu-west-2"
aws_account_id="976227762508"
aws_ecr_name="facecctv.api"

# prebuild
echo "authenticating the docker command line interface to the AWS ECR registry..."
aws ecr get-login-password --region $aws_region | docker login --username AWS --password-stdin $aws_account_id.dkr.ecr.$aws_region.amazonaws.com

# build

echo "building the docker image..."

docker build -f app/Dockerfile -t $aws_account_id.dkr.ecr.$aws_region.amazonaws.com/$aws_ecr_name:dev ./app/

# push
echo "Pushing the docker image to the AWS ECR registry..."
docker push $aws_account_id.dkr.ecr.$aws_region.amazonaws.com/$aws_ecr_name:dev

echo "Done!"