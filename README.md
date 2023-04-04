# sam-sel-py39-test

This project contains source code and supporting files for a serverless application that you can deploy with the SAM CLI. It includes the following files and folders.

- hello_world - Code for the application's Lambda function and Project Dockerfile.
- events - Invocation events that you can use to invoke the function.
- tests - Unit tests for the application code. 
- template.yaml - A template that defines the application's AWS resources.

The application uses several AWS resources, including Lambda functions and an API Gateway API. These resources are defined in the `template.yaml` file in this project. You can update the template to add AWS resources through the same deployment process that updates your application code.

## Deploy the sample application

To build and deploy your application for the first time, run the following in your shell:

```bash
sam build

#first time
sam deploy --guided

#following times
sam deploy --region="ap-northeast-1"
```

```bash
#Unfortunately the local image doesnt work as its a aws lambda image with python.
sam-sel-py39-test$ sam local invoke HelloWorldFunction --event events/event.json
```

The SAM CLI can also emulate your application's API. Use the `sam local start-api` to run the API locally on port 3000.

```bash
sam-sel-py39-test$ sam local start-api
sam-sel-py39-test$ curl http://localhost:3000/
```