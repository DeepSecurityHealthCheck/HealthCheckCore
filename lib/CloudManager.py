import boto3
import requests
import os, sys
import datetime

class  CloudManager():

    def __init__(self):
        self.remote_sqs = os.environ.get('SQS_URL', None)
        self.remote_bucket = os.environ.get('DATA_PACK_BUCKET', None)
        self.report_bucket = os.environ.get('REPORTS_BUCKET', None)
        self.keys_bucket   = os.environ.get('KEYS_BUCKET', None)
        self.sqs_client = boto3.client('sqs')
        self.bucket_client = boto3.client('s3')
        self.EXPIRE_DAYS  = 45
    
    def pull_sqs(self):
        try:
            response = self.sqs_client.receive_message(QueueUrl = self.remote_sqs, WaitTimeSeconds=20)
            messages = response.get('Messages', None)
        except Exception as e:
            print('Error request AWS Service {}'.format(e))
            sys.exit(-1)

        return messages
    

    def pull_s3_object(self, bucket, key):
        try:
            response = self.bucket_client.get_object(Bucket=bucket, Key=key)
            body = response.get('Body', None)
            if body != None:
                body = body.read()
            
            return body
        except Exception as e:
            print('Error on running AWS S3 service {}'.format(e))
            sys.exit(-1)

    # def pull_datapack(self, data_pack_id):
    #     try:
    #         response = self.bucket_client.get_object(Bucket=self.remote_bucket, Key=data_pack_id)

    #         body = response.get('Body', None)
    #         if body != None:
    #             body = body.read()

    #         return body
    #     # except NoSuchKey:
    #     #     print("Ghost data request data pack, removing from queue...")

    #     except Exception as e:
    #         print('Error on request AWS Service(S3 Data Pack) {}'.format(e))
    #         sys.exit(-1)

    # def pull_private_key(self):
    #     try:
    #         response = self.bucket_client.get_object(Bucket=self.keys_bucket, Key='PRIVATE_key.pem')
    #         body = response.get('Body', None)
            
    #         if body != None:
    #             body = body.read()
            
    #         return body
    #     except Exception as e:
    #         print('Error on request AWS Service(S3 Keys) {}'.format(e))
    #         sys.exit(-1)

    # def pull_private_key_password(self):
    #     try:
    #         response = self.bucket_client.get_object(Bucket=self.keys_bucket, Key='PRIVATE_key_password')
    #         body = response.get('Body', None)
            
    #         if body != None:
    #             body = body.read()
            
    #         return body
    #     except Exception as e:
    #         print('Error on request AWS Service(S3 Keys) {}'.format(e))
    #         sys.exit(-1)

    def write_new_report(self, report_path, generation_id):
        try:
            with open(report_path, 'rb') as report:
                report_data = report.read()
                expiration_time = ((datetime.datetime.now() + datetime.timedelta(days=self.EXPIRE_DAYS))).strftime("%a, %d %b %Y %H:%M:%S GMT")
                print('Saving {} in bucket {}'.format(report_path, self.report_bucket))
                res = self.bucket_client.put_object(Body=report_data, Bucket=self.report_bucket, Key=generation_id, Expires=expiration_time)
        except Exception as e:
            print('Error on request AWS Service {}'.format(e))
            sys.exit(-1)
    
    def remove_message(self, sqs_message):
        receipt_handle = sqs_message['ReceiptHandle']
        sqs_client = boto3.client('sqs')
        res = sqs_client.delete_message(QueueUrl=self.remote_sqs, ReceiptHandle = receipt_handle)