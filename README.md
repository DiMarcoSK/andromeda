# Andromeda

**Andromeda** is a simple pipeline runner. It aims to automate tasks and processes in continuous integration/continuous delivery (CI/CD) environments. If you are tired of
commiting changes in new branches only to test the pipeline (Or if you want to insta approve your GMUD) this tool is for you.

## Requirements
- Go (v1.16+)
- Kubernets (To run tasks in pods)

## Customization
You can configure the pipeline by editing the `.gitlab-ci.yml` or `name-of-the-workflow.yml` file, defining the stages like `build`, `test`, and `deploy`. Andromeda will handle the execution of each stage in the correct order.
