#### deploy stack
aws cloudformation deploy --template-file lambda.yaml  --stack-name my-new-stack-2 --capabilities CAPABILITY_NAMED_IAM

#### publish
aws sns publish --topic-arn "arn:aws:sns:us-east-1:434842609133:ledivan-devops" --message '{ "Key": "BOB", "Value": "BOB" }'
