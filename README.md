Start
- minikube
    - `minikube start --driver=docker`
- local runner
    - `cd actions-runner`
    - `./run.sh`
- start ELK
    - `cd temp`
    - `docker compose up -d`
- start metricbeat

Helpful Commands

```bash
watch "kubectl get deployments; kubectl get pods; kubectl get hpa; kubectl top pods;"
watch -n 3 -d 'echo "--- DEPLOYMENTS ---"; kubectl get deployments; echo "\n--- PODS ---"; kubectl get pods; echo "\n--- HPAS ---"; kubectl get hpa;  echo "\n--- SVC ---"; kubectl get svc;  echo "\n--- Ingress ---"; kubectl get ingress; echo "\n--- TOP PODS ---"; kubectl top pods';

watch -n 3 -d \
'echo "--- DEPLOYMENTS ---"; \
kubectl get deployments --namespace=default; \
kubectl get deployments --namespace=kube-logging; \
echo "\n--- PODS ---"; \
kubectl get pods --namespace=default; \
kubectl get pods --namespace=kube-logging; \
echo "\n--- HPAS ---"; \
kubectl get hpa --namespace=default;  \
kubectl get hpa --namespace=kube-logging;  \
echo "\n--- SVC ---"; \
kubectl get svc --namespace=default; \
kubectl get svc --namespace=kube-logging; \
echo "\n--- Ingress ---"; \
kubectl get ingress --namespace=default; \
kubectl get ingress --namespace=kube-logging; \
echo "\n--- TOP PODS ---"; \
kubectl top pods --namespace=default; \
kubectl top pods --namespace=kube-logging;'

kubectl delete deployment my-app; kubectl delete service my-service; kubectl delete hpa my-app-hpa;
kubectl delete deployment backend-deployment frontend-deployment; kubectl delete service backend-service frontend-service; kubectl delete ingress frontend-backend-ingress; kubectl delete hpa backend-hpa frontend-hpa;
```

Links

- http://192.168.49.2.nip.io/login