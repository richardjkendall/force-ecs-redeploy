# force-ecs-redeploy

Lambda function which triggers a re-deployment of an ECS service pulling the latest version of any container images which make up the tasks which are part of the service.

The code expects the following environment variables to be set

| Variable | Purpose |
| ---      | ---     |
| CLUSTER  | Name of the ECS cluster where the service is running |
| SERVICE  | Name of the service to trigger a redeployment for |

## IAM permissions

The script needs the following permissions in order to trigger the update of the service `ecs:UpdateService`.

## Example

You can see this being used as part of the following terraform module: https://github.com/richardjkendall/tf-modules/tree/master/modules/simple-cf-stats
