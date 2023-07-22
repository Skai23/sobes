## Overview
Simple http server was return timestamp and hostname. 
Additionally there are two endpoints for checking health and metrics in Prometheus format

## How build image
```
git clone https://github.com/Skai23/sobes.git
cd sobes/server
docker build --tag python-http-server:latest .
docker push python-http-server:latest
```
## deploy to microk8s

Start [microk8s](https://github.com/canonical/microk8s) cluster and enshure that microk8s cluster enable modules ingress and repositiry. Enable if nessesary
```
microk8s start
microk8s enable ingress
microk8s enable repository
```
push docker image to local registry
```
docker tag python-http-server:latest localhost:32000/python-http-server:latest
docker push localhost:32000/python-http-server:latest

apply manifests to microk8s cluster
```
cd sobes/k8s
kubectl apply -f deploy.yaml -f service.yaml -f ingress.yaml
```
Done! Try curl http://py-server.localhost

## Handlers
request from / returns simple format timestamp and hostname

request from /health returns health check

request from /metrics returns prometheus format metrics

All another requests returns 404 response Not found
