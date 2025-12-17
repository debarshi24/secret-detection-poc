# Secret Detection POC Architecture

```
┌─────────────┐    ┌──────────────────┐    ┌─────────────────────┐    ┌─────────────────┐
│  Developer  │    │     GitHub       │    │   AWS CodePipeline  │    │  AWS CodeBuild  │
│             │───▶│                  │───▶│                     │───▶│                 │
│ 1. git push │    │ 2. Webhook       │    │ 3. Triggers Build   │    │ 4. TruffleHog   │
│             │    │    Trigger       │    │    Pipeline         │    │    Scan         │
└─────────────┘    └──────────────────┘    └─────────────────────┘    └─────────────────┘
                                                     │                          │
                                                     │                          │
                                                     ▼                          ▼
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                              AWS CloudWatch Logs                                       │
│                                                                                         │
│  ✅ SUCCESS: No secrets found - Build passes                                           │
│  ❌ FAILURE: Secrets detected - Build fails                                            │
│                                                                                         │
└─────────────────────────────────────────────────────────────────────────────────────────┘
                                           │
                                           ▼
                              ┌─────────────────────┐
                              │      S3 Bucket      │
                              │                     │
                              │ 5. Scan Reports     │
                              │    & Artifacts      │
                              └─────────────────────┘
```

## Flow Description

1. **Developer Push**: Code committed to GitHub repository
2. **Webhook Trigger**: GitHub webhook automatically triggers CodePipeline
3. **Pipeline Start**: CodePipeline orchestrates the build process
4. **Secret Scan**: CodeBuild runs TruffleHog to scan for hardcoded secrets
5. **Result Logging**: Scan results logged to CloudWatch and artifacts stored in S3

## Key Components

- **GitHub**: Source code repository with webhook integration
- **CodePipeline**: CI/CD orchestration (2-stage: Source + Build)
- **CodeBuild**: Executes TruffleHog secret scanner
- **CloudWatch**: Centralized logging and monitoring
- **S3**: Artifact storage for pipeline outputs

## Security Decision Points

```
Code Push → Secret Scan → Decision
                            │
                    ┌───────┴───────┐
                    ▼               ▼
              ✅ No Secrets    ❌ Secrets Found
                    │               │
                    ▼               ▼
              Build Passes    Build Fails
              Deploy Ready    Block Deploy
```