# Git
Git is a version control system (VCS) that monitors changes to project files. It allows you to:

- View changes to files across time.
- Restore previous versions.
- Annotate versions to summarise the changes.
- Create branches for experimentation.
- Add version names to projects. 

Git is notably a _distributed_ version control system (DCVS), as opposed to _centralised_, which means that the change history is stored both locally and on a (usually remote) server. This provides additional backups should the server's version be compromised.

## A GUI vs The Command Line
Many GUI versions of Git are available. However, the command line is thought to provide the most functionality and varies the least between different clients and operating systems.

## Git Commands

Check git's version.
```bash
git --version
```

Get help
```bash
git --help
```
or 
```bash
git <command> --help
```

View the ```.git_config``` file's contents. This can also be found in the ```<C:/Users/<USER>``` user directory. 
```bash
git config --list
```

Check the working tree's status.
```bash
git status
```

See previous commit information.
```bash
git log
```

### Setting up your account
Set up a username to match your GitHub account and access its remote repositories.
```bash
git config --global user.name "<USER_NAME>"
```

Set up an email to match your GitHub account and access its remote repositories.
```bash
git config --global user.email "<USER_EMAIL>"
```

### Creating a local repository
Navigate to the folder that you want to be a repo.
```bash
git init --initial-branch=main
```
or 
```bash
git init -b main
```
The folder should now contain a ```.git``` folder that contains the directory information.

### Tracking file changes
Tell git to start tracking a file (staging).
```bash
git add <file>
```

Once staged, the changes may be committed.
```bash
git commit -m "<Message>"
```
Each commit has a unique identity as well as other metadata. This allows git to track your changes.

### Cloning a Repository
You can create a local copy of a remote repository via:
```bash
git clone <repo-url>
```
The repo URL can be obtained from the repo's GitHub page.

### Branches
Branches are duplicates of the current state of the repo. They can be used to experiment with changes and _merged_ into the main branch when deemed acceptable. Create branches via:
```bash
git checkout -b <branch-name>
```

## GitHub
GitHub is a freely available remote access repository service that enables open source project sharing.

### Pull requests
On a collaborative project, a user that makes an edit to their branch will want to merge it into another branch (e.g. main). To do this, the user submits a _pull request_. Collaborators may then review the pull request and accept/reject the merge.

### Issues & Discussions
Issues are used to track ideas, tasks and bugs associated with specific sections (lines of code) of a repository.
Discussions are used for general Q&A and are not necessarily related to code. 

### Workflows
Workflows are ways to manage the development pipeline. Examples include
- Git Flow: Slower, more structured release with clear deadlines.
- GitHub Flow: Faster, more dynamic development. Meant for continuous delivery.

### Gists 
Gists are mini repos that can be used to share single files or small sections of code. They can be either public or private. However, private gists have less protection than private repositories because the shareable URL can be viewed by anyone.

Like repositories, they benefit from version control and remote editing. They can also be embedded into websites for documentation purposes.

### Wikis
Wikis add supplementary resources and documentation to repositories. They can be created on the repo's GitHub page.

### Codespaces
Codespaces are cloud-based, containerised virtual machines that can be used for running code remotely. Each independent user is allotted 60 hours of codepace time per week. They are commonly used for testing code in a variety of environments.

### Projects
Projects are used for planning and organising project milestones.

## Preferred Git & GitHub Setup
1. Set up a GitHub account and create a repo.
2. Download and install GitHub Desktop.
3. Download the repository and ensure that it's backed up via GitHub Desktop.
4. Install Git for Windows.
5. Install VS Code. 
6. VS Code should recognise your git repos when they are navigated to.
7. You can delete GitHub Desktop if necessary.

## References
https://learn.microsoft.com/en-us/training/paths/github-foundations/

## Technobabble
- Version control system (VCS): Tracks changes to files.
- Source/Software control management (SCM): Same as VCS.
- Software configuration management (SCM): A wider term that considers all process changes. For example: build, packaging, etc (i.e. not just file changes).
- Working tree: All files and directories that fall within the scope of the version-controlled project.
- Repository (repo): Contains the data and history for the project. 
- Bare repo: A repo that is not part of a working tree. Usually a directory ending in ```.git```. It is usually used for backup/sharing.
- Commit: Accepting the changes to the files.
- Remote: A remotely held git repository.
- Continuous integration and continuous delivery (CI/CD): More emphasis on automation to speed up releases of new code.
