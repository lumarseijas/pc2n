#comando para Crear un cluster de Kubernetes en GKE con 3 nodos sin autoescalado
#aplicar los archivos de configuracion: kubectl apply -f microservicio.yaml
#verificar despliegues y servicios:
# kubectl get pods
# kubectl get services

from subprocess import call
#FALTA LO DE LOS 3 NODOS
call(
    "gcloud container clusters create pc2 "
    "--num-nodes=3 "
    "--enable-autoscaling=false "
    "--region=us-central1 "
    "--machine-type=e2-medium",
    shell=True
)

call("kubectl apply -f productpage.yaml", shell=True)
call("kubectl apply -f details.yaml", shell=True)
call("kubectl apply -f ratings.yaml", shell=True)
call("kubectl apply -f reviews-svc.yaml", shell=True)
call("kubectl apply -f reviews-v1-deployment.yaml", shell=True)
call("kubectl apply -f reviews-v2-deployment.yaml", shell=True)
call("kubectl apply -f reviews-v3-deployment.yaml", shell=True)

call("kubectl get pods", shell=True)
call("kubectl get services", shell=True)