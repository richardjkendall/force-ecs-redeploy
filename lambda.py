import boto3
import os

client = boto3.client("ecs")

def update(cluster, service):
  """
  Update a service with the latest version of a docker image
  """
  try:
    response = client.update_service(
      cluster=cluster,
      service=service,
      forceNewDeployment=True
    )
    print("Request to update service submitted")
  except Exception as e:
    if "ClusterNotFoundException" == e.__class__.__name__:
      print("The cluster '{c}' was not found".format(c = cluster))
    if "ServiceNotFoundException" == e.__class__.__name__:
      print("The service '{s}' was not found".format(s = service))

def handler(*args, **kwargs):
  """
  Lambda handler
  """
  # get clutser/service details from environment
  cluster = os.getenv("CLUSTER")
  service = os.getenv("SERVICE")
  if cluster == None:
    print("CLUSTER not found in the environment")
    exit(-1)
  if service == None:
    print("SERVICE not found in the environment")
    exit(-1)
  print("Cluster = {c}, Service = {s}".format(c = cluster, s = service))
  update(
    cluster = cluster,
    service = service
  )

if __name__ == "__main__":
  print("Running handler...")
  handler()