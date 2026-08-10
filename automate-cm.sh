#!/bin/bash

if  kubectl get deploy | grep -q "nginx" ; then
  echo "you need to delete the original nginx deployment first"
  exit 1
fi

   
kubectl delete cm webpage || true

kubectl create configmap webpage --from-file=Frontend/index.html --from-file=Frontend/qualifications.html --from-file=Frontend/styles.css --from-file=Frontend/images/Dan_Jackson_Thomas.jpg --dry-run=client -o yaml > ConfigMaps/frontend-index-config.yml

kubectl apply -f ConfigMaps/frontend-index-config.yml

kubectl apply -f frontend.yml
