PROYECTO DE PI : https://github.com/HX-PRomero/PI_ML_OPS
API EN DETA : https://www.youtube.com/watch?v=rLUn2rhO37s



-- DESPLIEGUE DE  BASE DE DATOS



pip install -r requirements.txt

## Run the server in local
uvicorn main:app --reload



http://localhost:8000/get_max_duration/amazon/min/2020


http://localhost:8000/get_score_count/amazon/3/2020


http://localhost:8000/get_actor/amazon/2020





## Running in GCP

gcloud components update



Enabled the listed services 

gcloud services enable apigateway.googleapis.com
gcloud services enable servicemanagement.googleapis.com
gcloud services enable servicecontrol.googleapis.com


gcloud functions deploy nodejs-http-function \
--gen2 \
--runtime=nodejs18 \
--region=us-central1 \
--source=. \
--entry-point=helloGET \
--trigger-http \
--allow-unauthenticated


## Creando el api gateway
gcloud api-gateway apis create basico --project=amplifyauth-284502

gcloud api-gateway apis describe basico --project=amplifyauth-284502

## Creating the api config of the api gateway 
gcloud api-gateway api-configs create my-config --api=basico --openapi-spec=openapi2-functions.yaml --project=amplifyauth-284502
   <!-- --backend-auth-service-account=SERVICE_ACCOUNT_EMAIL -->

gcloud api-gateway api-configs describe my-config --api=basico --project=amplifyauth-284502

## Create a new gateway inside api gateway
gcloud api-gateway gateways create my-gateway --api=basico --api-config=my-config --location=us-central1 --project=amplifyauth-284502

## Describe the api gateway 
gcloud api-gateway gateways describe my-gateway --location=us-central1 --project=amplifyauth-284502


curl https://my-gateway-6r4c2bk1.uc.gateway.dev

## Installing beta 
gcloud components install beta


## Network-endpoint-groups -- antigua version

gcloud beta compute network-endpoint-groups create prueba-neg-central-cli --region=us-central1 --network-endpoint-type=serverless --serverless-platform=apigateway.googleapis.com --serverless-resource=my-gateway

## Network-endpoint-groups -- nueva version
gcloud beta compute network-endpoint-groups create prueba-neg-central-cli --region=us-central1 --network-endpoint-type=serverless --serverless-deployment-platform=apigateway.googleapis.com --serverless-deployment-resource=my-gateway



## Create the backend service
gcloud compute backend-services create backend-service-example  --global 

## Create the url-maps
gcloud compute url-maps create api-gateway-url-map --default-service backend-service-example



## Create the rul maps path matcher
gcloud compute url-maps add-path-matcher api-gateway-url-map --path-matcher-name=my-pm2 --default-service=backend-service-example --path-rules="video=backend-service-example,/video/*=backend-service-example" --new-hosts my-hosts.com


## Nice references : 
https://googlecloudcheatsheet.withgoogle.com/
