# Publishing the ToolkitAPI Python SDK

## Goal

Keep the source code in the private GitLab monorepo while making the package installable publicly with:

pip install toolkitapi

## Recommended setup

- Source repository: private GitLab monorepo
- Package registry: public PyPI
- Release phase: beta
- Current package version: 2.0.0b1

## One-time setup

### 1. Add GitLab CI/CD variables

In GitLab, open:

Settings → CI/CD → Variables

Add these masked variables:

- PYPI_API_TOKEN
- TEST_PYPI_API_TOKEN

Generate the tokens from:
- https://pypi.org/manage/account/token/
- https://test.pypi.org/manage/account/token/

If the project does not exist yet on PyPI, an account-scoped token is fine for the first publish.

### 2. Push the pipeline changes

Commit the SDK publishing updates and push them to your GitLab repository.

## Publish flow

### Test publish first

1. Push your changes to the main branch.
2. Open the GitLab pipeline for that commit.
3. Run the manual job named:
   - publish-python-sdk-testpypi

### Public beta release

After the TestPyPI release looks good, run:

- publish-python-sdk-pypi

You can also publish from a release tag such as:

python-sdk-v2.0.0b1

## After publish

Users can install with:

pip install toolkitapi

## Notes

- A beta version keeps expectations clear while you continue making changes.
- PyPI can be public even when the GitLab source repository is private.
- When ready for stable, bump the version from 2.0.0b1 to something like 2.0.0 and publish again.
