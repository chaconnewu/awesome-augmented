<h1>
 Git and Git Flow Cheat Sheet
 <a href="https://github.com/sindresorhus/awesome">
  <img alt="Awesome" src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg"/>
 </a>
</h1>
<hr>
 <p align="center">
  <img alt="Git" height="190" src="./Img/git-logo.png" width="455">
  </img>
 </p>
 <hr>
  <h1>
   Other Available Languages:
  </h1>
  <ol>
   <li>
    <a href="https://github.com/arslanbilal/git-cheat-sheet/blob/master/other-sheets/git-cheat-sheet-ar.md">
     Arabic Git Cheat Sheet
    </a>
   </li>
   <li>
    <a href="https://github.com/arslanbilal/git-cheat-sheet/blob/master/other-sheets/git-cheat-sheet-zh.md">
     Chinese Git Cheat Sheet
    </a>
   </li>
   <li>
    <a href="https://github.com/arslanbilal/git-cheat-sheet/blob/master/other-sheets/git-cheat-sheet-hi.md">
     Hindi Git Cheat Sheet
    </a>
   </li>
   <li>
    <a href="https://github.com/arslanbilal/git-cheat-sheet/blob/master/other-sheets/git-cheat-sheet-tr.md">
     Turkish Git Cheat Sheet
    </a>
   </li>
   <li>
    <a href="https://github.com/arslanbilal/git-cheat-sheet/blob/master/other-sheets/git-cheat-sheet-es.md">
     Spanish Git Cheat Sheet
    </a>
   </li>
  </ol>
  <p>
   Git cheat sheet saves you from learning all the commands by heart.
  </p>
  <p>
   Be free to contribute, update the grammar mistakes. You are also free to add your language file.
   <hr/>
  </p>
  <h1>
   Git Cheat Sheet English
  </h1>
  <h3>
   Index
  </h3>
  <ul>
   <li>
    <a href="#setup">
     Set Up
    </a>
   </li>
   <li>
    <a href="#configuration-files">
     Configuration Files
    </a>
   </li>
   <li>
    <a href="#create">
     Create
    </a>
   </li>
   <li>
    <a href="#local-changes">
     Local Changes
    </a>
   </li>
   <li>
    <a href="#search">
     Search
    </a>
   </li>
   <li>
    <a href="#commit-history">
     Commit History
    </a>
   </li>
   <li>
    <a href="#branches--tags">
     Branches & Tags
    </a>
   </li>
   <li>
    <a href="#update--publish">
     Update & Publish
    </a>
   </li>
   <li>
    <a href="#merge--rebase">
     Merge & Rebase
    </a>
   </li>
   <li>
    <a href="#undo">
     Undo
    </a>
   </li>
   <li>
    <a href="#git-flow">
     Git Flow
    </a>
   </li>
  </ul>
  <hr>
   <h2>
    Setup
   </h2>
   <h5>
    Show current configuration:
   </h5>
   <p>
    <code>
     $ git config --list
    </code>
   </p>
   <h5>
    Show repository configuration:
   </h5>
   <p>
    <code>
     $ git config --local --list
    </code>
   </p>
   <h5>
    Show global configuration:
   </h5>
   <p>
    <code>
     $ git config --global --list
    </code>
   </p>
   <h5>
    Show system configuration:
   </h5>
   <p>
    <code>
     $ git config --system --list
    </code>
   </p>
   <h5>
    Set a name that is identifiable for credit when review version history:
   </h5>
   <p>
    <code>
     $ git config --global user.name “[firstname lastname]”
    </code>
   </p>
   <h5>
    Set an email address that will be associated with each history marker:
   </h5>
   <p>
    <code>
     $ git config --global user.email “[valid-email]”
    </code>
   </p>
   <h5>
    Set automatic command line coloring for Git for easy reviewing:
   </h5>
   <p>
    <code>
     $ git config --global color.ui auto
    </code>
   </p>
   <h5>
    Set global editor for commit
   </h5>
   <p>
    <code>
     $ git config --global core.editor vi
    </code>
   </p>
   <hr>
    <h2>
     Configuration Files
    </h2>
    <h5>
     Repository specific configuration file [--local]:
    </h5>
    <p>
     <code>
      <repo>/.git/config
     </code>
    </p>
    <h5>
     User-specific configuration file [--global]:
    </h5>
    <p>
     <code>
      ~/.gitconfig
     </code>
    </p>
    <h5>
     System-wide configuration file [--system]:
    </h5>
    <p>
     <code>
      /etc/gitconfig
     </code>
    </p>
    <hr>
     <h2>
      Create
     </h2>
     <h5>
      Clone an existing repository:
     </h5>
     <p>
      There are two ways:
     </p>
     <p>
      Via SSH
     </p>
     <p>
      <code>
       $ git clone ssh://user@domain.com/repo.git
      </code>
     </p>
     <p>
      Via HTTP
     </p>
     <p>
      <code>
       $ git clone http://domain.com/user/repo.git
      </code>
     </p>
     <h5>
      Create a new local repository:
     </h5>
     <p>
      <code>
       $ git init
      </code>
      <hr/>
     </p>
     <h2>
      Local Changes
     </h2>
     <h5>
      Changes in working directory:
     </h5>
     <p>
      <code>
       $ git status
      </code>
     </p>
     <h5>
      Changes to tracked files:
     </h5>
     <p>
      <code>
       $ git diff
      </code>
     </p>
     <h5>
      Add all current changes to the next commit:
     </h5>
     <p>
      <code>
       $ git add .
      </code>
     </p>
     <h5>
      Add some changes in <file> to the next commit:
     </h5>
     <p>
      <code>
       $ git add -p <file>
      </code>
     </p>
     <h5>
      Commit all local changes in tracked files:
     </h5>
     <p>
      <code>
       $ git commit -a
      </code>
     </p>
     <h5>
      Commit previously staged changes:
     </h5>
     <p>
      <code>
       $ git commit
      </code>
     </p>
     <h5>
      Commit with message:
     </h5>
     <p>
      <code>
       $ git commit -m 'message here'
      </code>
     </p>
     <h5>
      Commit skipping the staging area and adding message:
     </h5>
     <p>
      <code>
       $ git commit -am 'message here'
      </code>
     </p>
     <h5>
      Commit to some previous date:
     </h5>
     <p>
      <code>
       git commit --date="`date --date='n day ago'`" -am "Commit Message"
      </code>
     </p>
     <h5>
      Change last commit:
      <br/>
     </h5>
     <p>
      <em>
       <sub>
        Don't amend published commits!
       </sub>
      </em>
     </p>
     <p>
      <code>
       $ git commit -a --amend
      </code>
     </p>
     <h5>
      Change committer date of last commit:
     </h5>
     <p>
      <code>
       GIT_COMMITTER_DATE="date" git commit --amend
      </code>
     </p>
     <h5>
      Change Author date of last commit:
     </h5>
     <p>
      <code>
       git commit --amend --date="date"
      </code>
     </p>
     <h5>
      Move uncommitted changes from current branch to some other branch:
      <br/>
     </h5>
     <p>
      <code>
       git stash
git checkout branch2
git stash pop
      </code>
     </p>
     <h5>
      Restore stashed changes back to current branch:
     </h5>
     <p>
      <code>
       git stash apply
      </code>
     </p>
     <h5>
      Remove the last set of stashed changes:
     </h5>
     <p>
      <code>
       git stash drop
      </code>
     </p>
     <hr>
      <h2>
       Search
      </h2>
      <h5>
       A text search on all files in the directory:
      </h5>
      <p>
       <code>
        $ git grep "Hello"
       </code>
      </p>
      <h5>
       In any version of a text search:
      </h5>
      <p>
       <code>
        $ git grep "Hello" v2.5
       </code>
      </p>
      <hr>
       <h3>
        Commit History
       </h3>
       <h5>
        Show all commits, starting with newest (it'll show the hash, author information, date of commit and title of the commit):
       </h5>
       <p>
        <code>
         $ git log
        </code>
       </p>
       <h5>
        Show all the commits(it'll show just the commit hash and the commit message):
       </h5>
       <p>
        <code>
         $ git log --oneline
        </code>
       </p>
       <h5>
        Show all commits of a specific user:
       </h5>
       <p>
        <code>
         $ git log --author="username"
        </code>
       </p>
       <h5>
        Show changes over time for a specific file:
       </h5>
       <p>
        <code>
         $ git log -p <file>
        </code>
       </p>
       <h5>
        Display commits that are present only in remote/branch in right side
       </h5>
       <p>
        <code>
         $ git log --oneline <origin/master>..<remote/master> --left-right
        </code>
       </p>
       <h5>
        Who changed, what and when in <file>:
       </h5>
       <p>
        <code>
         $ git blame <file>
        </code>
       </p>
       <h5>
        Show Reference log:
       </h5>
       <p>
        <code>
         $ git reflog show
        </code>
       </p>
       <h5>
        Delete Reference log:
       </h5>
       <p>
        <code>
         $ git reflog delete
        </code>
        <hr/>
       </p>
       <h2>
        Branches & Tags
       </h2>
       <h5>
        List all local branches:
       </h5>
       <p>
        <code>
         $ git branch
        </code>
       </p>
       <h5>
        List all remote branches:
       </h5>
       <p>
        <code>
         $ git branch -r
        </code>
       </p>
       <h5>
        Switch HEAD branch:
       </h5>
       <p>
        <code>
         $ git checkout <branch>
        </code>
       </p>
       <h5>
        Create and switch new branch:
       </h5>
       <p>
        <code>
         $ git checkout -b <branch>
        </code>
       </p>
       <h5>
        Create a new branch based on your current HEAD:
       </h5>
       <p>
        <code>
         $ git branch <new-branch>
        </code>
       </p>
       <h5>
        Create a new tracking branch based on a remote branch:
       </h5>
       <p>
        <code>
         $ git branch --track <new-branch> <remote-branch>
        </code>
       </p>
       <h5>
        Delete a local branch:
       </h5>
       <p>
        <code>
         $ git branch -d <branch>
        </code>
       </p>
       <h5>
        Force delete a local branch:
       </h5>
       <p>
        <em>
         <sub>
          You will lose unmerged changes!
         </sub>
        </em>
       </p>
       <p>
        <code>
         $ git branch -D <branch>
        </code>
       </p>
       <h5>
        Mark the current commit with a tag:
       </h5>
       <p>
        <code>
         $ git tag <tag-name>
        </code>
       </p>
       <h5>
        Mark the current commit with a tag that includes a message:
       </h5>
       <p>
        <code>
         $ git tag -a <tag-name>
        </code>
        <hr/>
       </p>
       <h2>
        Update & Publish
       </h2>
       <h5>
        List all current configured remotes:
       </h5>
       <p>
        <code>
         $ git remote -v
        </code>
       </p>
       <h5>
        Show information about a remote:
       </h5>
       <p>
        <code>
         $ git remote show <remote>
        </code>
       </p>
       <h5>
        Add new remote repository, named <remote>:
       </h5>
       <p>
        <code>
         $ git remote add <remote> <url>
        </code>
       </p>
       <h5>
        Download all changes from <remote>, but don't integrate into HEAD:
       </h5>
       <p>
        <code>
         $ git fetch <remote>
        </code>
       </p>
       <h5>
        Download changes and directly merge/integrate into HEAD:
       </h5>
       <p>
        <code>
         $ git remote pull <remote> <url>
        </code>
       </p>
       <h5>
        Get all changes from HEAD to local repository:
       </h5>
       <p>
        <code>
         $ git pull origin master
        </code>
       </p>
       <h5>
        Get all changes from HEAD to local repository without a merge:
       </h5>
       <p>
        <code>
         git pull --rebase <remote> <branch>
        </code>
       </p>
       <h5>
        Publish local changes on a remote:
       </h5>
       <p>
        <code>
         $ git push remote <remote> <branch>
        </code>
       </p>
       <h5>
        Delete a branch on the remote:
       </h5>
       <p>
        <code>
         $ git push <remote> :<branch> (since Git v1.5.0)
or
git push <remote> --delete <branch> (since Git v1.7.0)
        </code>
       </p>
       <h5>
        Publish your tags:
       </h5>
       <p>
        <code>
         $ git push --tags
        </code>
        <hr/>
       </p>
       <h2>
        Merge & Rebase
       </h2>
       <h5>
        Merge
        <branch>
         into your current HEAD:
        </branch>
       </h5>
       <p>
        <code>
         $ git merge <branch>
        </code>
       </p>
       <h5>
        Rebase your current HEAD onto <branch>:
        <br/>
       </h5>
       <p>
        <em>
         <sub>
          Don't rebase published commit!
         </sub>
        </em>
       </p>
       <p>
        <code>
         $ git rebase <branch>
        </code>
       </p>
       <h5>
        Abort a rebase:
       </h5>
       <p>
        <code>
         $ git rebase --abort
        </code>
       </p>
       <h5>
        Continue a rebase after resolving conflicts:
       </h5>
       <p>
        <code>
         $ git rebase --continue
        </code>
       </p>
       <h5>
        Use your configured merge tool to solve conflicts:
       </h5>
       <p>
        <code>
         $ git mergetool
        </code>
       </p>
       <h5>
        Use your editor to manually solve conflicts and (after resolving) mark file as resolved:
       </h5>
       <p>
        <code>
         $ git add <resolved-file>
        </code>
       </p>
       <p>
        <code>
         $ git rm <resolved-file>
        </code>
       </p>
       <h5>
        Squashing commits:
       </h5>
       <p>
        <code>
         $ git rebase -i <commit-just-before-first>
        </code>
       </p>
       <p>
        Now replace this,
       </p>
       <p>
        <code>
         pick <commit_id>
pick <commit_id2>
pick <commit_id3>
        </code>
       </p>
       <p>
        to this,
       </p>
       <p>
        <code>
         pick <commit_id>
squash <commit_id2>
squash <commit_id3>
        </code>
        <hr/>
       </p>
       <h2>
        Undo
       </h2>
       <h5>
        Discard all local changes in your working directory:
       </h5>
       <p>
        <code>
         $ git reset --hard HEAD
        </code>
       </p>
       <h5>
        Get all the files out of the staging area(i.e. undo the last
        <code>
         git add
        </code>
        ):
       </h5>
       <p>
        <code>
         $ git reset HEAD
        </code>
       </p>
       <h5>
        Discard local changes in a specific file:
       </h5>
       <p>
        <code>
         $ git checkout HEAD <file>
        </code>
       </p>
       <h5>
        Revert a commit (by producing a new commit with contrary changes):
       </h5>
       <p>
        <code>
         $ git revert <commit>
        </code>
       </p>
       <h5>
        Reset your HEAD pointer to a previous commit and discard all changes since then:
       </h5>
       <p>
        <code>
         $ git reset --hard <commit>
        </code>
       </p>
       <h5>
        Reset your HEAD pointer to a remote branch current state.
       </h5>
       <p>
        <code>
         git reset --hard <remote/branch> e.g., upstream/master, origin/my-feature
        </code>
       </p>
       <h5>
        Reset your HEAD pointer to a previous commit and preserve all changes as unstaged changes:
       </h5>
       <p>
        <code>
         $ git reset <commit>
        </code>
       </p>
       <h5>
        Reset your HEAD pointer to a previous commit and preserve uncommitted local changes:
       </h5>
       <p>
        <code>
         $ git reset --keep <commit>
        </code>
       </p>
       <h5>
        Remove files that were accidentally committed before they were added to .gitignore
       </h5>
       <p>
        <code>
         $ git rm -r --cached .
$ git add .
$ git commit -m "remove xyz file"
        </code>
        <hr/>
       </p>
       <h2>
        Git-Flow
       </h2>
       <h3>
        Index
       </h3>
       <ul>
        <li>
         <a href="#setup">
          Setup
         </a>
        </li>
        <li>
         <a href="#getting-started">
          Getting Started
         </a>
        </li>
        <li>
         <a href="#features">
          Features
         </a>
        </li>
        <li>
         <a href="#make-a-release">
          Make a Release
         </a>
        </li>
        <li>
         <a href="#hotfixes">
          Hotfixes
         </a>
        </li>
        <li>
         <a href="#commands">
          Commands
         </a>
         <hr/>
        </li>
       </ul>
       <h3>
        Setup
       </h3>
       <h6>
        You need a working git installation as prerequisite. Git flow works on OSX, Linux and Windows.
       </h6>
       <h5>
        OSX Homebrew:
       </h5>
       <p>
        <code>
         $ brew install git-flow
        </code>
       </p>
       <h5>
        OSX Macports:
       </h5>
       <p>
        <code>
         $ port install git-flow
        </code>
       </p>
       <h5>
        Linux (Debian-based):
       </h5>
       <p>
        <code>
         $ apt-get install git-flow
        </code>
       </p>
       <h5>
        Windows (Cygwin):
       </h5>
       <h6>
        You need wget and util-linux to install git-flow.
       </h6>
       <p>
        <code>
         $ wget -q -O - --no-check-certificate https://github.com/nvie/gitflow/raw/develop/contrib/gitflow-installer.sh | bash
        </code>
        <hr/>
       </p>
       <h3>
        Getting Started
       </h3>
       <h6>
        Git flow needs to be initialized in order to customize your project setup. Start using git-flow by initializing it inside an existing git repository:
       </h6>
       <h5>
        Initialize:
       </h5>
       <h6>
        You'll have to answer a few questions regarding the naming conventions for your branches. It's recommended to use the default values.
       </h6>
       <p>
        <code>
         git flow init
        </code>
        <hr/>
       </p>
       <h3>
        Features
       </h3>
       <h6>
        Develop new features for upcoming releases. Typically exist in developers repos only.
       </h6>
       <h5>
        Start a new feature:
       </h5>
       <h6>
        This action creates a new feature branch based on 'develop' and switches to it.
       </h6>
       <p>
        <code>
         git flow feature start MYFEATURE
        </code>
       </p>
       <h5>
        Finish up a feature:
       </h5>
       <h6>
        Finish the development of a feature. This action performs the following:
       </h6>
       <h6>
        1)Merged MYFEATURE into 'develop'.
       </h6>
       <h6>
        2)Removes the feature branch.
       </h6>
       <h6>
        3)Switches back to 'develop' branch
       </h6>
       <p>
        <code>
         git flow feature finish MYFEATURE
        </code>
       </p>
       <h5>
        Publish a feature:
       </h5>
       <h6>
        Are you developing a feature in collaboration? Publish a feature to the remote server so it can be used by other users.
       </h6>
       <p>
        <code>
         git flow feature publish MYFEATURE
        </code>
       </p>
       <h5>
        Getting a published feature:
       </h5>
       <h6>
        Get a feature published by another user.
       </h6>
       <p>
        <code>
         git flow feature pull origin MYFEATURE
        </code>
       </p>
       <h5>
        Tracking a origin feature:
       </h5>
       <h6>
        You can track a feature on origin by using
       </h6>
       <p>
        <code>
         git flow feature track MYFEATURE
        </code>
        <hr/>
       </p>
       <h3>
        Make a Release
       </h3>
       <h6>
        Support preparation of a new production release. Allow for minor bug fixes and preparing meta-data for a release
       </h6>
       <h5>
        Start a release:
       </h5>
       <h6>
        To start a release, use the git flow release command. It creates a release branch created from the 'develop' branch. You can optionally supply a [BASE] commit sha-1 hash to start the release from. The commit must be on the 'develop' branch.
       </h6>
       <p>
        <code>
         git flow release start RELEASE [BASE]
        </code>
       </p>
       <h6>
        It's wise to publish the release branch after creating it to allow release commits by other developers. Do it similar to feature publishing with the command:
       </h6>
       <p>
        <code>
         git flow release publish RELEASE
        </code>
       </p>
       <h6>
        (You can track a remote release with the:
        <code>
         git flow release track RELEASE
        </code>
        command)
       </h6>
       <h5>
        Finish up a release:
       </h5>
       <h6>
        Finishing a release is one of the big steps in git branching. It performs several actions:
       </h6>
       <h6>
        1)Merges the release branch back into 'master'
       </h6>
       <h6>
        2)Tags the release with its name
       </h6>
       <h6>
        3)Back-merges the release into 'develop'
       </h6>
       <h6>
        4)Removes the release branch
       </h6>
       <p>
        <code>
         git flow release finish RELEASE
        </code>
       </p>
       <h6>
        Don't forget to push your tags with
        <code>
         git push --tags
        </code>
       </h6>
       <hr>
        <h3>
         Hotfixes
        </h3>
        <h6>
         Hotfixes arise from the necessity to act immediately upon an undesired state of a live production version. May be branched off from the corresponding tag on the master branch that marks the production version.
        </h6>
        <h5>
         Git flow hotfix start:
        </h5>
        <h6>
         Like the other git flow commands, a hotfix is started with
        </h6>
        <p>
         <code>
          $ git flow hotfix start VERSION [BASENAME]
         </code>
        </p>
        <h6>
         The version argument hereby marks the new hotfix release name. Optionally you can specify a basename to start from.
        </h6>
        <h5>
         Finish a hotfix:
        </h5>
        <h6>
         By finishing a hotfix it gets merged back into develop and master. Additionally the master merge is tagged with the hotfix version
        </h6>
        <p>
         <code>
          git flow hotfix finish VERSION
         </code>
         <hr/>
        </p>
        <h3>
         Commands
        </h3>
        <p align="center">
         <img alt="Git" height="270" src="./Img/git-flow-commands.png" width="460">
         </img>
        </p>
        <hr>
         <h3>
          Git flow schema
         </h3>
         <p align="center">
          <img alt="Git" src="Img/git-flow-commands-without-flow.png">
          </img>
         </p>
         <hr>
         </hr>
        </hr>
       </hr>
      </hr>
     </hr>
    </hr>
   </hr>
  </hr>
 </hr>
</hr>