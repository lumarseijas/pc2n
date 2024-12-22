#comando para Crear un cluster de Kubernetes en GKE con 3 nodos sin autoescalado
#aplicar los archivos de configuracion: kubectl apply -f microservicio.yaml
#verificar despliegues y servicios:
# kubectl get pods
# kubectl get services

from subprocess import call

#call("minikube start --nodes 3",shell=True)
# Iniciamos un clúster de Kubernetes con 3 nodos
call("minikube start --driver=docker -p pc2 --nodes 3", shell=True)

# Cambiamos al perfil que acabamos de crear
call("minikube profile pc2", shell=True)

call("minikube kubectl apply -- -f productpage.yaml", shell=True)
call("minikube kubectl apply -- -f details.yaml", shell=True)
call("minikube kubectl apply -- -f ratings.yaml", shell=True)
call("minikube kubectl apply -- -f reviews-svc.yaml", shell=True)
call("minikube kubectl apply  -- -f reviews-v1-deployment.yaml", shell=True)
call("minikube kubectl apply -- -f reviews-v2-deployment.yaml", shell=True)
call("minikube kubectl apply -- -f reviews-v3-deployment.yaml", shell=True)

call("minikube kubectl get pods", shell=True)
call("minikube kubectl get services", shell=True)
call("minikube service productpage", shell=True)
