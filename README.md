## Overview
Simple http server was return timestamp and hostname. 
Additionally there are two endpoints for checking health and metrics in Prometheus format

## How build image
```
git clone https://github.com/Skai23/sobes.git
cd sobes/server
docker build --tag python-http-server:latest
docker push python-http-server:latest
```
## deploy to k8s
```
git clone https://github.com/Skai23/sobes.git
cd sobes/k8s
#change ingress host your-domain.com in ingress.yaml
vi ingress.yaml
kubectl apply -f ./*
```

## Handlers
request from / returns simple format timestamp and hostname

request from /health returns health check

request from /metrics returns prometheus format metrics

All another requests returns 404 response Not found
