# UPDATE-DESCRIPTION-USING-README

GitHub Action to update repository's description using README.

## README Format

Description must be the only content in the first header.

## Usage

``` yml
name: Update repository descriptoin
uses: rtvu/update-description-using-readme@v1.0.0
with:
  repository: ${{ github.repository }}
  token: ${{ secrets.REPOSITORY_PAT }}
```

## Inputs

| Name | Description | Default |
| --- | --- | --- |
| `repository` | (**required**) GitHub repository as `<owner>/<name>`. | |
| `readme` | Path to repository's README. | `README.md` |
| `update` | Boolean to update repository's description. | `true` |
| `token` | (**required**) GitHub personal access token. | |

## Outputs

| Name | Description |
| --- | --- |
| `description` | README's description of repository. |
