# Setup Instructions

## Prerequisites
- AWS CLI configured
- GitHub repository
- GitHub personal access token

## Step-by-Step Implementation

### 1. Create GitHub Repository
```bash
# Create new repo or use existing one
# Ensure you have admin access for webhook creation
```

### 2. Deploy AWS Infrastructure
```bash
aws cloudformation create-stack \
  --stack-name secret-detection-poc \
  --template-body file://cloudformation-template.yml \
  --parameters ParameterKey=GitHubOwner,ParameterValue=YOUR_USERNAME \
               ParameterKey=GitHubRepo,ParameterValue=YOUR_REPO \
               ParameterKey=GitHubToken,ParameterValue=YOUR_TOKEN \
  --capabilities CAPABILITY_IAM \
  --region us-east-1
```

### 3. Add buildspec.yml to Repository
```bash
# Copy buildspec.yml to your repository root
git add buildspec.yml
git commit -m "Add secret scanning buildspec"
git push origin main
```

### 4. Test the Pipeline

**Test 1: Safe Code (Should Pass)**
```bash
cp demo-files/safe-code.py app.py
git add app.py
git commit -m "Add safe application code"
git push origin main
# Check CodePipeline - should succeed
```

**Test 2: Unsafe Code (Should Fail)**
```bash
cp demo-files/unsafe-code.py app.py
git add app.py
git commit -m "Add application with secrets"
git push origin main
# Check CodePipeline - should fail with secret detection
```

**Test 3: Fix Code (Should Pass)**
```bash
cp demo-files/safe-code.py app.py
git add app.py
git commit -m "Remove hardcoded secrets"
git push origin main
# Check CodePipeline - should succeed again
```

### 5. Monitor Results
- View pipeline: AWS Console → CodePipeline
- Check logs: AWS Console → CloudWatch → Log Groups
- Review artifacts: S3 bucket created by CloudFormation

## Verification Checklist

- [ ] CloudFormation stack deployed successfully
- [ ] CodePipeline created and connected to GitHub
- [ ] First build triggered automatically
- [ ] Safe code passes the pipeline
- [ ] Unsafe code fails the pipeline
- [ ] CloudWatch logs show scan results
- [ ] S3 artifacts bucket contains scan reports

## Troubleshooting

**Pipeline not triggering**: Check GitHub webhook in repository settings
**Build failing**: Verify buildspec.yml is in repository root
**Permission errors**: Ensure IAM roles have correct policies
**GitHub connection**: Verify personal access token has repo permissions