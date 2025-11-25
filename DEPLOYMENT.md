# GitHub Actions Deployment Setup

This repository uses GitHub Actions to automatically publish to PyPI.

## Workflow

- **Develop Branch** → Publishes to [TestPyPI](https://test.pypi.org/)
- **Main Branch** → Publishes to [PyPI](https://pypi.org/)

## Setup Instructions

### 1. Create API Tokens

**TestPyPI Token:**
1. Go to https://test.pypi.org/manage/account/#api-tokens
2. Create a new API token named `funsize-engineer-github`
3. Scope: "Entire account" (for first upload)
4. Copy the token (starts with `pypi-`)

**PyPI Token:**
1. Go to https://pypi.org/manage/account/#api-tokens
2. Create a new API token named `funsize-engineer-github`
3. Scope: "Entire account" (for first upload)
4. Copy the token (starts with `pypi-`)

### 2. Add Secrets to GitHub

1. Go to your repository: https://github.com/JessicaRudd/funsize-engineer
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Add two secrets:
   - Name: `TEST_PYPI_API_TOKEN`, Value: `pypi-...` (your TestPyPI token)
   - Name: `PYPI_API_TOKEN`, Value: `pypi-...` (your PyPI token)

### 3. Create Develop Branch

```bash
git checkout -b develop
git push -u origin develop
```

### 4. Deployment Process

**To deploy to TestPyPI:**
```bash
git checkout develop
# Make your changes
git add .
git commit -m "Your changes"
git push origin develop
```

**To deploy to Production PyPI:**
```bash
git checkout main
git merge develop
git push origin main
```

Or create a Pull Request from `develop` to `main` and merge it.

## Testing the Package

**From TestPyPI:**
```bash
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ funsize-engineer
```

**From PyPI:**
```bash
pip install funsize-engineer
```

## Notes

- The workflow automatically builds and uploads the package
- No need to manually run `python setup.py sdist` or `twine upload`
- Each push to `develop` or `main` triggers a deployment
- Make sure to update the version in `setup.py` before each release
