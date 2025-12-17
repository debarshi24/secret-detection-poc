#!/usr/bin/env python3
"""
Safe code example - no secrets here!
"""

import os
import boto3

def get_aws_client():
    """Get AWS client using environment variables or IAM role."""
    # Good practice: Use environment variables or IAM roles
    access_key = os.environ.get('AWS_ACCESS_KEY_ID')
    secret_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
    
    return boto3.client('s3')

def main():
    """Main function."""
    print("This is safe code with no hardcoded secrets!")
    client = get_aws_client()
    print("AWS client created successfully")

if __name__ == "__main__":
    main()