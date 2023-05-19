import pulumi
from pulumi_kubernetes.apps.v1 import Deployment
from pulumi_kubernetes.core.v1 import Service
from pulumi_kubernetes.helm.v3 import Chart, ChartOpts

api_deployment = Deployment(
    "api-deployment",
    spec={
        "selector": {"matchLabels": {"app": "api"}},
        "template": {
            "metadata": {"labels": {"app": "api"}},
            "spec": {
                "containers": [
                    {
                        "name": "api",
                        "image": "martins87/my-api",
                        "env": [{"name": "JOBS_SERVICE", "value": "os.environ['JOBS_SERVICE']"}],
                        "ports": [{"name": "http", "containerPort": 5000}],
                    }
                ]
            },
        },
    },
)

api_service = Service(
    "api-service",
    metadata={"name": "api-service"},
    spec={
        "selector": {"app": "api"},
        "ports": [{"name": "http", "port": 80, "targetPort": 5000}],
        "type": "ClusterIP",
    },
)

jobs_deployment = Deployment(
    "jobs-deployment",
    spec={
        "selector": {"matchLabels": {"app": "jobs"}},
        "template": {
            "metadata": {"labels": {"app": "jobs"}},
            "spec": {
                "containers": [
                    {
                        "name": "jobs",
                        "image": "martins87/myapp",
                        "ports": [{"name": "http", "containerPort": 5001}],
                    }
                ]
            },
        },
    },
)

jobs_service = Service(
    "jobs-service",
    metadata={"name": "jobs-service"},
    spec={
        "selector": {"app": "jobs"},
        "ports": [{"name": "http", "port": 80, "targetPort": 5001}],
        "type": "ClusterIP",
    },
)
