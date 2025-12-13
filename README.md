Start
- minikube
    - `minikube start --driver=docker`
- local runner
    - `cd actions-runner`
    - `./run.sh`

Helpful Commands

```bash
watch "kubectl get deployments; kubectl get pods; kubectl get hpa; kubectl top pods;"
watch -n 3 -d 'echo "--- DEPLOYMENTS ---"; kubectl get deployments; echo "\n--- PODS ---"; kubectl get pods; echo "\n--- HPAS ---"; kubectl get hpa;  echo "\n--- SVC ---"; kubectl get svc;  echo "\n--- Ingress ---"; kubectl get ingress; echo "\n--- TOP PODS ---"; kubectl top pods';

kubectl delete deployment my-app; kubectl delete service my-service; kubectl delete hpa my-app-hpa;
kubectl delete deployment backend-deployment frontend-deployment; kubectl delete service backend-service frontend-service; kubectl delete ingress frontend-backend-ingress; kubectl delete hpa backend-hpa frontend-hpa;
```

Links

- http://192.168.49.2.nip.io/login