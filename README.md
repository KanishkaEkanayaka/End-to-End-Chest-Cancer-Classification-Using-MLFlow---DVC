# End-to-End-Chest-Cancer-Classification-Using-MLFlow---DVC

## basic pre-requisits
Create template
create setup.py
create and install requirements
create utility functions

## workflow
1.update config.yaml
2.update secrets.yaml [potional]
3.update params.yaml
4.update the entity
5.update the configuration manager in src/config
6.update the components
7.update the pipeline
8.update main.py
9.update dvc.yaml

## DagsHub

```bash

save all the required credentials in environment variables
os.environ["MLFLOW_TRACKING_URI"] = ""
os.environ["MLFLOW_TRACKING_USERNAME"] = ""
os.environ["MLFLOW_TRACKING_PASSWORD"] = ""

or use export keyword

export MLFLOW_TRACKING_URI = your tracking uri
export MLFLOW_TRACKING_USERNAME = your tracking user name
export MLFLOW_TRACKING_PASSWORD = your tracking password

```

## DVC

First create the dvc.yaml file.

Then execute the following commands

```bash

dvc init # initialize dvc
dvc repro # to run dvc.yaml file
dvc dag # to see the pipeline visually on cmd

```

## Final model
After figuring out the best model parameters then train the model with those parameters.
then store that finally trained model in another folder outside the artifacts folder because we are not pushing artifacts folder into the github

## Docker Image Creation

 - First Create Docker file
 - Then inside github/workflows create main.yaml file to write all the CICD commands which need to do CICD in github action

## AWS-CICD-Deployment-with-Github-Actions
1. Login to AWS console.
2. Create IAM user for deployment

### with specific access

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws


### Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

### Policy to place when creating IAM:

        1. AmazonEC2ContainerRegistryFullAccess

        2. AmazonEC2FullAccess

3. Create ECR repo to store/save docker image
    - Save the URI: 566373416292.dkr.ecr.us-east-1.amazonaws.com/chicken
4. Create EC2 machine (Ubuntu)
5. Open EC2 and Install docker in EC2 Machine:

        ### optinal

        sudo apt-get update -y

        sudo apt-get upgrade

        ### required

        curl -fsSL https://get.docker.com -o get-docker.sh

        sudo sh get-docker.sh

        sudo usermod -aG docker ubuntu

        newgrp docker

6. Configure EC2 as self-hosted runner:
setting>actions>runner>new self hosted runner> choose os> then run command one by one

7. Setup github secrets:

        AWS_ACCESS_KEY_ID=

        AWS_SECRET_ACCESS_KEY=

        AWS_REGION = us-east-1

        AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

        ECR_REPOSITORY_NAME = simple-app