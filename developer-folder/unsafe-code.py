#!/usr/bin/env python3
"""
Unsafe code example - contains hardcoded secrets!
"""

import boto3

def get_aws_client():
    """BAD PRACTICE: Hardcoded credentials."""
    # This will trigger the secret scanner
    aws_access_key = "AKIAIOSFODNN7EXAMPLE"
    aws_secret_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEYYYYY"
    
    return boto3.client(
        's3',
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key
    )

def main():
    """Main function with hardcoded API key."""
    api_key = "sk-1234567890abcdef1234567890abcdef"
    print(f"Using API key: {api_key}")
    
    client = get_aws_client()
    print("AWS client created")

if __name__ == "__main__":
    main()