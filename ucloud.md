## Quick setup for of GitHub with VS Code

Steps:
- 1) Run an instance of VS code on UCloud
  - Use limited compute for the first classes
  - Mount your own (private!) folder to the instance in which you create the following files.
- 2) Create a file called `setup_git.sh` containing the following code:


```bash
# run using 
# bash path_to_folder/setup_git.sh

git config --global user.email "yourmail@mail.com"
git config --global user.name "githubusername"
```

Make sure to fill in the correct username and email. This will set up GitHub, but you also need to:

- 3) Create a file called `git_token.txt` which contain your [personal access token](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token).

Save the files and you can now close the session. Next time you start a session you can mount your folder and run:

```
bash path_to_folder/setup_git.sh
```

to set up git. If you want to use the VS code GitHub integration you will still need to log in using the GitHub access token, which can simply be copied from the file `git_token.txt`.

## Collaborate with VS Code
In the [VS code documentation](https://docs.cloud.sdu.dk/Apps/coder.html?highlight=coder%20share#start-live-share) on UCloud there is a guide to setting up live share on UCloud.
