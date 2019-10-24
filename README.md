# Project Title

Cornell Chatbot, IT@Cornell

## Getting Started

This voice/text chatbot made for use by the Cornell community to quickly answer questions about the university without the need to search through multiple web data sources. Natural language processing enabled by custom voice/text interpretation applications with Amazon/AWS.Respond the users-side acoustic queries, I adopt services with Lambda, API Gateway.
Make use of Serverless Application Model (SAM) of AWS CloudFormation to initialize the server-side templated infrastructure.


### coding style tests

You can now create YAML-formatted templates to describe your AWS resources and properties in AWS CloudFormation. Now, you have the option to use either YAML-formatted templates or JSON-formatted templates to model and describe your AWS infrastructure. YAML-formatted CloudFormation templates follow the same anatomy as existing JSON-formatted templates and support all the same features.

```
  ### BUILD SECTION - DO NOT ALTER ###

  BuildBucket:
    Type: 'AWS::S3::Bucket'
    Properties:
      Tags:
        - Key: 'Application'
          Value: !Sub '${Application}'
        - Key: 'Environment'
          Value: !Sub '${Environment}'

  BuildRole:
    Type: 'AWS::IAM::Role'
    Properties:
      RoleName: !Sub '${Application}-${Environment}-build'
      AssumeRolePolicyDocument:
        Version: '2012-10-17'
        Statement:
          - Effect: 'Allow'
            Action: 'sts:AssumeRole'
            Principal:
              Service: !Sub 'codebuild.${AWS::URLSuffix}'
      ManagedPolicyArns:
        - !Sub 'arn:${AWS::Partition}:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole'
        - !Sub 'arn:${AWS::Partition}:iam::aws:policy/AWSLambdaFullAccess'
        - !Sub 'arn:${AWS::Partition}:iam::aws:policy/AmazonAPIGatewayAdministrator'
        - !Sub 'arn:${AWS::Partition}:iam::aws:policy/AWSCodeBuildAdminAccess'
        - !Sub 'arn:${AWS::Partition}:iam::aws:policy/IAMFullAccess'
        - !Sub 'arn:${AWS::Partition}:iam::aws:policy/AWSCloudFormationReadOnlyAccess'
      Policies:
        - PolicyName: 'build-permissions'
          PolicyDocument:
            Version: '2012-10-17'
            Statement:
              - Effect: 'Allow'
                Action:
                  - 'cloudformation:*'
                Resource:
                  - !Sub 'arn:${AWS::Partition}:cloudformation:${AWS::Region}:${AWS::AccountId}:stack/${AWS::StackName}/*'
                  - !Sub 'arn:${AWS::Partition}:cloudformation:${AWS::Region}:aws:transform/Serverless-2016-10-31'


```

## Deployment
Need Amazon Account to enable the Amazon Web Services

## Built With

* [YAML](https://yaml.org/) - Handle APIs Gateway and AWS post-requests
* [Python](https://www.python.org/download/releases/3.0/) - APIs to answer the questioon
* [Swift](https://developer.apple.com/swift/) - Used to generate front-end interface

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 



This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
