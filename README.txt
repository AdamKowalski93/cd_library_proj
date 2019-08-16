README:


1. Start minikube:
minikube start

2. Set docker env:
eval $(minikube docker-env)

3. Build image:
docker build -t linux:alpine .

4. Run in minikube:
kubectl apply -f app.yaml










===========================================

#kubectl run hello-foo --image=linux:alpine --image-pull-policy=Never
# Check that it's running
#kubectl get pods


# export DOCKER_TLS_VERIFY="1"
# export DOCKER_HOST="tcp://192.168.99.100:2376"
# export DOCKER_CERT_PATH="/Users/pb/.minikube/certs"
# export DOCKER_API_VERSION="1.35"
# Run this command to configure your shell:
# eval $(minikube docker-env)