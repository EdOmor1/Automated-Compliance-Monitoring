# Automated-Compliance-Monitoring

# Overview
The Automated Compliance Monitoring project aims to automate compliance monitoring within AWS environments using various AWS services like AWS Config, AWS CloudTrail, Amazon GuardDuty, and AWS Security Hub. It leverages AWS Lambda for custom compliance checks and Amazon SNS for notifications.

# Components

# AWS CloudFormation Templates
config_rule.yaml: Defines AWS Config rules to monitor and enforce compliance configurations.
cloudtrail.yaml: Sets up AWS CloudTrail for logging API activity.
guardduty.yaml: Configures Amazon GuardDuty for continuous security monitoring.
securityhub.yaml: Sets up AWS Security Hub for comprehensive security insights.

# Lambda Function
compliance_check.py: Custom Lambda function to perform compliance checks on AWS resources. It can be triggered by AWS Config rules or scheduled events.

# Notifications
sns_topic.yaml: Defines an SNS topic to send notifications for compliance events and findings.

# Usage
Deploy CloudFormation templates in the cloudformation/ directory to set up AWS services.
Deploy the Lambda function compliance_check.py to your AWS account.
Configure AWS Config rules to trigger the Lambda function for custom compliance checks.
Subscribe to the SNS topic defined in sns_topic.yaml to receive notifications.
Monitor compliance events and findings through AWS Config, CloudTrail, GuardDuty, and Security Hub dashboards.

# Prerequisites
AWS CLI installed and configured with appropriate IAM permissions.
Basic knowledge of AWS services such as CloudFormation, Lambda, AWS Config, CloudTrail, GuardDuty, and Security Hub.

# Contributing
Contributions are welcome! Please feel free to submit issues, pull requests, or suggestions.

