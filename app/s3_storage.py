from contextlib import asynccontextmanager
from aiobotocore.session import get_session


class S3Client:
    def __init__(
            self,
            access_key: str,
            secret_key: str,
            endpoint_url: str,
            bucket_name: str
            ):
        self.config = {
            "aws_access_key_id": access_key,
            "aws_secret_access_key": secret_key,
            "endpoint_url": endpoint_url
        }
        self.bucket_name = bucket_name
        self.session = get_session()

    # creating connection
    @asynccontextmanager
    async def get_client(self):
        async with self.session.create_client("s3", **self.config) as client:
            yield client

        
    # function for upload file in s3 storage
    async def upload_file(
                  self, 
                  file,
                  object_name: str
                ):
        async with self.get_client() as client:
            await client.put_object(
                    Bucket = self.bucket_name,
                    Key = object_name,
                    Body = file
                )


s3_client = S3Client(
    access_key = "9eb6923e90064c81bd89eb5f75d3344a",
    secret_key = "13d44ceb1088470596671e934b6bbdda",
    endpoint_url = "https://s3.storage.selcloud.ru",
    bucket_name = "mems_bucket"
)