# 🔐 AWS Secret Detection POC

Automated secret detection pipeline using AWS CodePipeline and CodeBuild with TruffleHog scanner.

## Architecture

```
GitHub → CodePipeline → CodeBuild (TruffleHog) → CloudWatch Logs
   ↓           ↓            ↓                        ↓
 Push      Triggers     Scans Code              Log Results
                         Fails if               
                       secrets found
```

## Components

- **GitHub**: Source repository with webhook trigger
- **CodePipeline**: Orchestrates the CI/CD workflow  
- **CodeBuild**: Runs TruffleHog secret scanner
- **CloudWatch**: Stores build logs and results
- **S3**: Stores pipeline artifacts

## Quick Setup

### 1. Deploy Infrastructure
```bash
aws cloudformation create-stack \
  --stack-name secret-detection-poc \
  --template-body file://cloudformation-template.yml \
  --parameters ParameterKey=GitHubOwner,ParameterValue=your-username \
               ParameterKey=GitHubRepo,ParameterValue=your-repo \
               ParameterKey=GitHubToken,ParameterValue=your-token \
  --capabilities CAPABILITY_IAM
```

### 2. Add buildspec.yml to your repository
Copy `buildspec.yml` to your GitHub repository root.

### 3. Test the Pipeline

**Fail Test**: Push `demo-files/unsafe-code.py` to trigger failure
**Pass Test**: Push `demo-files/safe-code.py` to see success

## Files

- `buildspec.yml` - CodeBuild configuration with TruffleHog scanner
- `cloudformation-template.yml` - Complete AWS infrastructure
- `iam-policy.json` - Minimal CodeBuild permissions
- `demo-files/` - Test files for demonstration

## Security Features

✅ **Automatic Detection**: Scans on every push  
✅ **Build Failure**: Stops deployment if secrets found  
✅ **Least Privilege**: Minimal IAM permissions  
✅ **Audit Trail**: All scans logged in CloudWatch  
✅ **No Secrets**: Uses environment variables and IAM roles  

## Cost Optimization

- Uses `BUILD_GENERAL1_SMALL` compute type
- Minimal S3 storage for artifacts
- Pay-per-use CodeBuild pricing
- Estimated cost: <$5/month for typical usage

## Demo Flow

1. **Initial State**: Repository with safe code → ✅ Build passes
2. **Add Secret**: Commit file with hardcoded key → ❌ Build fails  
3. **Remove Secret**: Fix the code → ✅ Build passes again

Pipeline automatically blocks any deployment containing secrets!