#!/bin/bash
NODE_IP=$(minikube ip)
NODE_PORT=$(kubectl get service my-service -o jsonpath='{.spec.ports[0].nodePort}')
while true; do
  ab -n 10000 -c 100 http://$NODE_IP:$NODE_PORT/docs
done