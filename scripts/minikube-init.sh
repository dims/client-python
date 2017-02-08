#!/bin/bash

# Copyright 2017 The Kubernetes Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

set -x

function clean_exit(){
    local error_code="$?"
    local spawned=$(jobs -p)
    if [ -n "$spawned" ]; then
        kill $(jobs -p)
    fi
    return $error_code
}

trap "clean_exit" EXIT

# Switch off SE-Linux
setenforce 0

# Debug libvirt
dpkg -l | grep virt
sudo ifconfig -a

# Download and install docker-machine-kvm
sudo curl -L https://github.com/dims/dims.github.io/raw/master/bin/docker-machine-driver-kvm -o /usr/local/bin/docker-machine-driver-kvm
sudo chmod +x /usr/local/bin/docker-machine-driver-kvm

# Get the latest stable version of kubernetes
export K8S_VERSION=$(curl -sS https://storage.googleapis.com/kubernetes-release/release/stable.txt)
echo "K8S_VERSION : ${K8S_VERSION}"

echo "Download Kubernetes CLI"
wget -O kubectl "http://storage.googleapis.com/kubernetes-release/release/${K8S_VERSION}/bin/linux/amd64/kubectl"
sudo chmod +x kubectl
sudo mv kubectl /usr/local/bin/

# Install minikube
curl -Lo minikube https://storage.googleapis.com/minikube/releases/v0.16.0/minikube-linux-amd64
sudo chmod +x minikube
sudo mv minikube /usr/local/bin/

# Debug info
sudo cat /etc/group | grep libvir
virsh -c qemu:///system list
env
export HOME=${HOME:-"${TRAVIS_BUILD_DIR}"}
env | grep HOME
virsh nodeinfo
virsh capabilities

# Start minikube with kvm driver
minikube --v=9 --alsologtostderr start --vm-driver=kvm --iso-url=https://storage.googleapis.com/minikube/iso/minikube-v1.0.6.iso

virsh list
virsh dumpxml minikube

sudo cat /etc/apt/sources.list | grep -v "^#" | grep -v "^$" | grep -v deb-src | sort
sudo dpkg -l | grep software-properties-common

kubectl get nodes

echo "Dump Kubernetes Objects..."
kubectl get componentstatuses
kubectl get configmaps
kubectl get daemonsets
kubectl get deployments
kubectl get events
kubectl get endpoints
kubectl get horizontalpodautoscalers
kubectl get ingress
kubectl get jobs
kubectl get limitranges
kubectl get nodes
kubectl get namespaces
kubectl get pods
kubectl get persistentvolumes
kubectl get persistentvolumeclaims
kubectl get quota
kubectl get resourcequotas
kubectl get replicasets
kubectl get replicationcontrollers
kubectl get secrets
kubectl get serviceaccounts
kubectl get services

# Try starting something
kubectl run hello-minikube --image=gcr.io/google_containers/echoserver:1.4 --port=8080
kubectl get pods

echo "Running tests..."
set -x -e
# Yield execution to venv command
$*