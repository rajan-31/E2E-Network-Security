Start
- minikube
- local runner

Commands

```bash
watch "kubectl get deployments; kubectl get pods; kubectl get hpa; kubectl top pods;"
watch -n 1 -d 'echo "--- DEPLOYMENTS ---"; kubectl get deployments; echo "\n--- PODS ---"; kubectl get pods; echo "\n--- HPAS ---"; kubectl get hpa; echo "\n--- TOP PODS ---"; kubectl top pods'

kubectl delete deployment my-app; kubectl delete service my-service; kubectl delete hpa my-app-hpa;
```