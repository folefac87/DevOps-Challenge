# Instruction for running the setup

-  To build image for the api_microservice application, run the following command in the same directory as the Dockerfile:
docker build -t my-api-image .
- This will build a Docker image with the tag my-api-image. 

To build image for the jobs_microservice application, run the following command in the same directory as the Dockerfile:
docker build -t myapp-image .

- In the pulumi folder, run: pulumi up

To access the application externally, run the following command: 
kubectl port-forward service/api-service 5000:80

kubectl port-forward service/jobs-service 5001:80
