import os
import boto3

def handler(event,context):
    sns_topic = os.environ['TOPIC_ARN']
    message = "Don't forget all the delicious cheese you have in the fridge #noServerNovember"
    sns = boto3.client('sns')
    sns.publish(TopicArn=sns_topic,Message=message)
