**Objective**:
Design, deploy, and manage a containerized microservice application using Kubernetes, following best practices for scalability, security, and observability.

 **Part 1: Application Setup**
**Task**:

Containerize a simple web application (e.g., Node.js, Python Flask, or Java Spring Boot).
Create a Dockerfile and push the image to Docker Hub or a private registry.

**Deliverables**:

Dockerfile
Image URL
Source code repo (GitHub/GitLab)

**Part 2: Kubernetes Deployment**
Task:

Create Kubernetes manifests for:
Deployment (3 replicas)
Service (LoadBalancer)
ConfigMap (for environment variables)
Secret (for sensitive data like DB passwords)
Init Container to wait for DB readiness
Sidecar Container for logging or proxy
Add readiness and liveness probes to the deployment
Resilience & Scheduling with Pod Distruption


**Deliverables**:

deployment.yaml
service.yaml
configmap.yaml
secret.yaml

**Part 3: Security Best Practices**
Task:

Use a non-root user in the Dockerfile.
Add resource limits and requests in the deployment.
Enable RBAC and create a service account for the pod.
Deliverables:

Updated Dockerfile
rbac.yaml
Updated deployment.yaml with security context

**Part 4: Monitoring & Logging**
Task:

Integrate Prometheus and Grafana for monitoring.

**Deliverables**:

Monitoring setup instructions
Sample Grafana dashboard screenshot
Logging configuration


**Basic Flow**:

Code is dockerized Flask app and then connects to Postgres using secrets/config → deployed in Kubernetes with 2 replicas, probes, logging sidecar, init container, RBAC, and exposed using NodePort. DB is deployed separately, app waits for DB before boot. Logs are tailed by a sidecar. PDB ensures HA.
