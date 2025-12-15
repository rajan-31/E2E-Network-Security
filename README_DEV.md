Start
- minikube
    - `minikube start`
- local runner
    - `cd actions-runner`
    - `./run.sh`
- start ELK
    - `cd temp`
    - `docker compose up -d`
- .
    - `export POD_NAME=$(kubectl get pods --namespace kube-logging -l "app.kubernetes.io/name=fluent-bit,app.kubernetes.io/instance=fluent-bit" -o jsonpath="{.items[0].metadata.name}")`
    - `kubectl --namespace kube-logging port-forward $POD_NAME 2020:2020`
- start metricbeat service

Helpful Commands

```bash
watch "kubectl get deployments; kubectl get pods; kubectl get hpa; kubectl top pods;"
watch -n 3 -d 'echo "--- DEPLOYMENTS ---"; kubectl get deployments; echo "\n--- PODS ---"; kubectl get pods; echo "\n--- HPAS ---"; kubectl get hpa;  echo "\n--- SVC ---"; kubectl get svc;  echo "\n--- Ingress ---"; kubectl get ingress; echo "\n--- TOP PODS ---"; kubectl top pods';

watch -n 1 \
'\
echo "===================== DEPLOYMENTS ====================="; \
kubectl get deployments; \
echo "\n======================== PODS ========================"; \
kubectl get pods; \
echo "\n"; \
kubectl get pods --namespace=kube-logging; \
echo "\n======================== HPA ========================="; \
kubectl get hpa;  \
echo "\n======================== SVC ========================="; \
kubectl get svc; \
echo "\n"; \
kubectl get svc --namespace=kube-logging; \
echo "\n====================== Ingress ======================="; \
kubectl get ingress;'

kubectl delete deployment my-app; kubectl delete service my-service; kubectl delete hpa my-app-hpa;

kubectl delete deployment backend-deployment frontend-deployment; kubectl delete service backend-service frontend-service; kubectl delete ingress frontend-backend-ingress; kubectl delete hpa backend-hpa frontend-hpa;

helm uninstall fluent-bit --namespace kube-logging
kubectl delete namespace kube-logging
```

Links

- http://192.168.49.2.nip.io/login