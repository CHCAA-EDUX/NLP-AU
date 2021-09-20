## Quick setup for of GitHub with VS Code

Steps:
- 1) Run an instance of VS code on UCloud
  - Mount your own (private!) folder to the instance in which you create the following files.
- 2) Create a file called `setup_git.sh` containing the following code:


```bash
# run using 
# bash path_to_folder/setup_git.sh

curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo gpg --dearmor -o /usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
#sudo apt update
sudo apt install gh

git config --global user.email "yourmail@mail.com"
git config --global user.name "Your Name (UCloud)"

gh auth login --with-token < git_token.txt
# assumes the git_token.txt contains a valid github token if you don't have one creat it following this guide
# https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token
```

Make sure to fill in the correct username and email. User name does not have to be your GitHub username. This will set up GitHub, but you also need to:

- 3) Create a file called `git_token.txt` which contain your [personal access token](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token).

Save the files and you can now close the session. Next time you start a session you can mount your folder and run:

```
bash path_to_folder/setup_git.sh
```

to set up git. If you want to use the VS code github integration you will still need to log in using the GitHub access token, which can simply be copied from the file `git_token.txt`.