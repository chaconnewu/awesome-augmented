<h2>
 git-tips
</h2>
<blockquote>
 <p>
  Collection of
  <code>
   git-tips
  </code>
  , want to add your tips? Checkout
  <a href="./contributing.md">
   contributing.md
  </a>
 </p>
</blockquote>
<p>
 <a href="http://git.io/git-tips">
  English
 </a>
 |
 <a href="https://github.com/521xueweihan/git-tips">
  中文
 </a>
</p>
<h3>
 <strong>
  Tools:
 </strong>
</h3>
<ul>
 <li>
  <a href="https://www.npmjs.com/package/git-tip">
   git-tip
  </a>
  - A handy CLI to make optimum use of these tips.
 </li>
</ul>
<p>
 P.S: All these commands are tested on
 <code>
  git version 2.7.4 (Apple Git-66)
 </code>
 .
</p>
<p>
 <!-- @doxie.inject start toc -->
 <!-- Don’t remove or change the comment above – that can break automatic updates. -->
 *
 <a href="#everyday-git-in-twenty-commands-or-so">
  Everyday Git in twenty commands or so
 </a>
 *
 <a href="#show-helpful-guides-that-come-with-git">
  Show helpful guides that come with Git
 </a>
 *
 <a href="#overwrite-pull">
  Overwrite pull
 </a>
 *
 <a href="#list-of-all-files-till-a-commit">
  List of all files till a commit
 </a>
 *
 <a href="#git-reset-first-commit">
  Git reset first commit
 </a>
 *
 <a href="#list-all-the-conflicted-files">
  List all the conflicted files
 </a>
 *
 <a href="#list-of-all-files-changed-in-a-commit">
  List of all files changed in a commit
 </a>
 *
 <a href="#unstaged-changes-since-last-commit">
  Unstaged changes since last commit
 </a>
 *
 <a href="#changes-staged-for-commit">
  Changes staged for commit
 </a>
 *
 <a href="#show-both-staged-and-unstaged-changes">
  Show both staged and unstaged changes
 </a>
 *
 <a href="#list-all-branches-that-are-already-merged-into-master">
  List all branches that are already merged into master
 </a>
 *
 <a href="#quickly-switch-to-the-previous-branch">
  Quickly switch to the previous branch
 </a>
 *
 <a href="#remove-branches-that-have-already-been-merged-with-master">
  Remove branches that have already been merged with master
 </a>
 *
 <a href="#list-all-branches-and-their-upstreams-as-well-as-last-commit-on-branch">
  List all branches and their upstreams, as well as last commit on branch
 </a>
 *
 <a href="#track-upstream-branch">
  Track upstream branch
 </a>
 *
 <a href="#delete-local-branch">
  Delete local branch
 </a>
 *
 <a href="#delete-remote-branch">
  Delete remote branch
 </a>
 *
 <a href="#delete-local-tag">
  Delete local tag
 </a>
 *
 <a href="#delete-remote-tag">
  Delete remote tag
 </a>
 *
 <a href="#undo-local-changes-with-the-last-content-in-head">
  Undo local changes with the last content in head
 </a>
 *
 <a href="#revert-undo-a-commit-by-creating-a-new-commit">
  Revert: Undo a commit by creating a new commit
 </a>
 *
 <a href="#reset-discard-commits-advised-for-private-branch">
  Reset: Discard commits, advised for private branch
 </a>
 *
 <a href="#reword-the-previous-commit-message">
  Reword the previous commit message
 </a>
 *
 <a href="#see-commit-history-for-just-the-current-branch">
  See commit history for just the current branch
 </a>
 *
 <a href="#amend-author">
  Amend author.
 </a>
 *
 <a href="#reset-author-after-author-has-been-changed-in-the-global-config">
  Reset author, after author has been changed in the global config.
 </a>
 *
 <a href="#changing-a-remotes-url">
  Changing a remote's URL
 </a>
 *
 <a href="#get-list-of-all-remote-references">
  Get list of all remote references
 </a>
 *
 <a href="#get-list-of-all-local-and-remote-branches">
  Get list of all local and remote branches
 </a>
 *
 <a href="#get-only-remote-branches">
  Get only remote branches
 </a>
 *
 <a href="#stage-parts-of-a-changed-file-instead-of-the-entire-file">
  Stage parts of a changed file, instead of the entire file
 </a>
 *
 <a href="#get-git-bash-completion">
  Get git bash completion
 </a>
 *
 <a href="#what-changed-since-two-weeks">
  What changed since two weeks?
 </a>
 *
 <a href="#see-all-commits-made-since-forking-from-master">
  See all commits made since forking from master
 </a>
 *
 <a href="#pick-commits-across-branches-using-cherry-pick">
  Pick commits across branches using cherry-pick
 </a>
 *
 <a href="#find-out-branches-containing-commit-hash">
  Find out branches containing commit-hash
 </a>
 *
 <a href="#git-aliases">
  Git Aliases
 </a>
 *
 <a href="#saving-current-state-of-tracked-files-without-commiting">
  Saving current state of tracked files without commiting
 </a>
 *
 <a href="#saving-current-state-including-untracked-files">
  Saving current state including untracked files
 </a>
 *
 <a href="#show-list-of-all-saved-stashes">
  Show list of all saved stashes
 </a>
 *
 <a href="#apply-any-stash-without-deleting-from-the-stashed-list">
  Apply any stash without deleting from the stashed list
 </a>
 *
 <a href="#apply-last-stashed-state-and-delete-it-from-stashed-list">
  Apply last stashed state and delete it from stashed list
 </a>
 *
 <a href="#delete-all-stored-stashes">
  Delete all stored stashes
 </a>
 *
 <a href="#grab-a-single-file-from-a-stash">
  Grab a single file from a stash
 </a>
 *
 <a href="#show-all-tracked-files">
  Show all tracked files
 </a>
 *
 <a href="#show-all-untracked-files">
  Show all untracked files
 </a>
 *
 <a href="#show-all-ignored-files">
  Show all ignored files
 </a>
 *
 <a href="#create-new-working-tree-from-a-repository-git-25">
  Create new working tree from a repository (git 2.5)
 </a>
 *
 <a href="#create-new-working-tree-from-head-state">
  Create new working tree from HEAD state
 </a>
 *
 <a href="#untrack-files-without-deleting">
  Untrack files without deleting
 </a>
 *
 <a href="#before-deleting-untracked-filesdirectory-do-a-dry-run-to-get-the-list-of-these-filesdirectories">
  Before deleting untracked files/directory, do a dry run to get the list of these files/directories
 </a>
 *
 <a href="#forcefully-remove-untracked-files">
  Forcefully remove untracked files
 </a>
 *
 <a href="#forcefully-remove-untracked-directory">
  Forcefully remove untracked directory
 </a>
 *
 <a href="#update-all-the-submodules">
  Update all the submodules
 </a>
 *
 <a href="#show-all-commits-in-the-current-branch-yet-to-be-merged-to-master">
  Show all commits in the current branch yet to be merged to master
 </a>
 *
 <a href="#rename-a-branch">
  Rename a branch
 </a>
 *
 <a href="#rebases-feature-to-master-and-merges-it-in-to-master">
  Rebases 'feature' to 'master' and merges it in to master
 </a>
 *
 <a href="#archive-the-master-branch">
  Archive the
  <code>
   master
  </code>
  branch
 </a>
 *
 <a href="#modify-previous-commit-without-modifying-the-commit-message">
  Modify previous commit without modifying the commit message
 </a>
 *
 <a href="#prunes-references-to-remote-branches-that-have-been-deleted-in-the-remote">
  Prunes references to remote branches that have been deleted in the remote.
 </a>
 *
 <a href="#retrieve-the-commit-hash-of-the-initial-revision">
  Retrieve the commit hash of the initial revision.
 </a>
 *
 <a href="#visualize-the-version-tree">
  Visualize the version tree.
 </a>
 *
 <a href="#deploying-git-tracked-subfolder-to-gh-pages">
  Deploying git tracked subfolder to gh-pages
 </a>
 *
 <a href="#adding-a-project-to-repo-using-subtree">
  Adding a project to repo using subtree
 </a>
 *
 <a href="#get-latest-changes-in-your-repo-for-a-linked-project-using-subtree">
  Get latest changes in your repo for a linked project using subtree
 </a>
 *
 <a href="#export-a-branch-with-history-to-a-file">
  Export a branch with history to a file.
 </a>
 *
 <a href="#import-from-a-bundle">
  Import from a bundle
 </a>
 *
 <a href="#get-the-name-of-current-branch">
  Get the name of current branch.
 </a>
 *
 <a href="#ignore-one-file-on-commit-eg-changelog">
  Ignore one file on commit (e.g. Changelog).
 </a>
 *
 <a href="#stash-changes-before-rebasing">
  Stash changes before rebasing
 </a>
 *
 <a href="#fetch-pull-request-by-id-to-a-local-branch">
  Fetch pull request by ID to a local branch
 </a>
 *
 <a href="#show-the-most-recent-tag-on-the-current-branch">
  Show the most recent tag on the current branch.
 </a>
 *
 <a href="#show-inline-word-diff">
  Show inline word diff.
 </a>
 *
 <a href="#show-changes-using-common-diff-tools">
  Show changes using common diff tools.
 </a>
 *
 <a href="#dont-consider-changes-for-tracked-file">
  Don’t consider changes for tracked file.
 </a>
 *
 <a href="#undo-assume-unchanged">
  Undo assume-unchanged.
 </a>
 *
 <a href="#clean-the-files-from-gitignore">
  Clean the files from
  <code>
   .gitignore
  </code>
  .
 </a>
 *
 <a href="#restore-deleted-file">
  Restore deleted file.
 </a>
 *
 <a href="#restore-file-to-a-specific-commit-hash">
  Restore file to a specific commit-hash
 </a>
 *
 <a href="#always-rebase-instead-of-merge-on-pull">
  Always rebase instead of merge on pull.
 </a>
 *
 <a href="#list-all-the-alias-and-configs">
  List all the alias and configs.
 </a>
 *
 <a href="#make-git-case-sensitive">
  Make git case sensitive.
 </a>
 *
 <a href="#add-custom-editors">
  Add custom editors.
 </a>
 *
 <a href="#auto-correct-typos">
  Auto correct typos.
 </a>
 *
 <a href="#check-if-the-change-was-a-part-of-a-release">
  Check if the change was a part of a release.
 </a>
 *
 <a href="#dry-run-any-command-that-supports-dry-run-flag-should-do">
  Dry run. (any command that supports dry-run flag should do.)
 </a>
 *
 <a href="#marks-your-commit-as-a-fix-of-a-previous-commit">
  Marks your commit as a fix of a previous commit.
 </a>
 *
 <a href="#squash-fixup-commits-normal-commits">
  Squash fixup commits normal commits.
 </a>
 *
 <a href="#skip-staging-area-during-commit">
  Skip staging area during commit.
 </a>
 *
 <a href="#interactive-staging">
  Interactive staging.
 </a>
 *
 <a href="#list-ignored-files">
  List ignored files.
 </a>
 *
 <a href="#status-of-ignored-files">
  Status of ignored files.
 </a>
 *
 <a href="#commits-in-branch1-that-are-not-in-branch2">
  Commits in Branch1 that are not in Branch2
 </a>
 *
 <a href="#reuse-recorded-resolution-record-and-reuse-previous-conflicts-resolutions">
  Reuse recorded resolution, record and reuse previous conflicts resolutions.
 </a>
 *
 <a href="#open-all-conflicted-files-in-an-editor">
  Open all conflicted files in an editor.
 </a>
 *
 <a href="#count-unpacked-number-of-objects-and-their-disk-consumption">
  Count unpacked number of objects and their disk consumption.
 </a>
 *
 <a href="#prune-all-unreachable-objects-from-the-object-database">
  Prune all unreachable objects from the object database.
 </a>
 *
 <a href="#instantly-browse-your-working-repository-in-gitweb">
  Instantly browse your working repository in gitweb.
 </a>
 *
 <a href="#view-the-gpg-signatures-in-the-commit-log">
  View the GPG signatures in the commit log
 </a>
 *
 <a href="#remove-entry-in-the-global-config">
  Remove entry in the global config.
 </a>
 *
 <a href="#checkout-a-new-branch-without-any-history">
  Checkout a new branch without any history
 </a>
 *
 <a href="#extract-file-from-another-branch">
  Extract file from another branch.
 </a>
 *
 <a href="#list-only-the-root-and-merge-commits">
  List only the root and merge commits.
 </a>
 *
 <a href="#change-previous-two-commits-with-an-interactive-rebase">
  Change previous two commits with an interactive rebase.
 </a>
 *
 <a href="#list-all-branch-is-wip">
  List all branch is WIP
 </a>
 *
 <a href="#find-guilty-with-binary-search">
  Find guilty with binary search
 </a>
 *
 <a href="#bypass-pre-commit-and-commit-msg-githooks">
  Bypass pre-commit and commit-msg githooks
 </a>
 *
 <a href="#list-commits-and-changes-to-a-specific-file-even-through-renaming">
  List commits and changes to a specific file (even through renaming)
 </a>
 *
 <a href="#clone-a-single-branch">
  Clone a single branch
 </a>
 *
 <a href="#create-and-switch-new-branch">
  Create and switch new branch
 </a>
 *
 <a href="#ignore-file-mode-changes-on-commits">
  Ignore file mode changes on commits
 </a>
 *
 <a href="#turn-off-git-colored-terminal-output">
  Turn off git colored terminal output
 </a>
 *
 <a href="#specific-color-settings">
  Specific color settings
 </a>
 *
 <a href="#show-all-local-branches-ordered-by-recent-commits">
  Show all local branches ordered by recent commits
 </a>
 *
 <a href="#find-lines-matching-the-pattern-regex-or-string-in-tracked-files">
  Find lines matching the pattern (regex or string) in tracked files
 </a>
 *
 <a href="#clone-a-shallow-copy-of-a-repository">
  Clone a shallow copy of a repository
 </a>
 *
 <a href="#search-commit-log-across-all-branches-for-given-text">
  Search Commit log across all branches for given text
 </a>
 *
 <a href="#get-first-commit-in-a-branch-from-master">
  Get first commit in a branch (from master)
 </a>
 *
 <a href="#unstaging-staged-file">
  Unstaging Staged file
 </a>
 *
 <a href="#force-push-to-remote-repository">
  Force push to Remote Repository
 </a>
 *
 <a href="#adding-remote-name">
  Adding Remote name
 </a>
 *
 <a href="#show-the-author-time-and-last-revision-made-to-each-line-of-a-given-file">
  Show the author, time and last revision made to each line of a given file
 </a>
 *
 <a href="#group-commits-by-authors-and-title">
  Group commits by authors and title
 </a>
 *
 <a href="#forced-push-but-still-ensure-you-dont-overwrite-others-work">
  Forced push but still ensure you don't overwrite other's work
 </a>
 *
 <a href="#show-how-many-lines-does-an-author-contribute">
  Show how many lines does an author contribute
 </a>
 *
 <a href="#revert-reverting-an-entire-merge">
  Revert: Reverting an entire merge
 </a>
 *
 <a href="#number-of-commits-in-a-branch">
  Number of commits in a branch
 </a>
 *
 <a href="#alias-git-undo">
  Alias: git undo
 </a>
</p>
<p>
 <!-- Don’t remove or change the comment below – that can break automatic updates. More info at <a href="http://npm.im/doxie.inject">http://npm.im/doxie.inject</a>. -->
 <!-- @doxie.inject end toc -->
</p>
<p>
 <!-- @doxie.inject start -->
 <!-- Don’t remove or change the comment above – that can break automatic updates. -->
</p>
<h2>
 Everyday Git in twenty commands or so
</h2>
<p>
 <code>
  sh
git help everyday
 </code>
</p>
<h2>
 Show helpful guides that come with Git
</h2>
<p>
 <code>
  sh
git help -g
 </code>
</p>
<h2>
 Overwrite pull
</h2>
<p>
 <code>
  sh
git fetch --all && git reset --hard origin/master
 </code>
</p>
<h2>
 List of all files till a commit
</h2>
<p>
 <code>
  sh
git ls-tree --name-only -r <commit-ish>
 </code>
</p>
<h2>
 Git reset first commit
</h2>
<p>
 <code>
  sh
git update-ref -d HEAD
 </code>
</p>
<h2>
 List all the conflicted files
</h2>
<p>
 <code>
  sh
git diff --name-only --diff-filter=U
 </code>
</p>
<h2>
 List of all files changed in a commit
</h2>
<p>
 <code>
  sh
git diff-tree --no-commit-id --name-only -r <commit-ish>
 </code>
</p>
<h2>
 Unstaged changes since last commit
</h2>
<p>
 <code>
  sh
git diff
 </code>
</p>
<h2>
 Changes staged for commit
</h2>
<p>
 <code>
  sh
git diff --cached
 </code>
</p>
<p>
 <strong>
  Alternatives:
 </strong>
 <code>
  sh
git diff --staged
 </code>
</p>
<h2>
 Show both staged and unstaged changes
</h2>
<p>
 <code>
  sh
git diff HEAD
 </code>
</p>
<h2>
 List all branches that are already merged into master
</h2>
<p>
 <code>
  sh
git branch --merged master
 </code>
</p>
<h2>
 Quickly switch to the previous branch
</h2>
<p>
 <code>
  sh
git checkout -
 </code>
</p>
<h2>
 Remove branches that have already been merged with master
</h2>
<p>
 <code>
  sh
git branch --merged master | grep -v '^\*' | xargs -n 1 git branch -d
 </code>
</p>
<p>
 <strong>
  Alternatives:
 </strong>
 <code>
  sh
git branch --merged master | grep -v '^\*\|  master' | xargs -n 1 git branch -d # will not delete master if master is not checked out
 </code>
</p>
<h2>
 List all branches and their upstreams, as well as last commit on branch
</h2>
<p>
 <code>
  sh
git branch -vv
 </code>
</p>
<h2>
 Track upstream branch
</h2>
<p>
 <code>
  sh
git branch -u origin/mybranch
 </code>
</p>
<h2>
 Delete local branch
</h2>
<p>
 <code>
  sh
git branch -d <local_branchname>
 </code>
</p>
<h2>
 Delete remote branch
</h2>
<p>
 <code>
  sh
git push origin --delete <remote_branchname>
 </code>
</p>
<p>
 <strong>
  Alternatives:
 </strong>
 <code>
  sh
git push origin :<remote_branchname>
 </code>
</p>
<h2>
 Delete local tag
</h2>
<p>
 <code>
  sh
git tag -d <tag-name>
 </code>
</p>
<h2>
 Delete remote tag
</h2>
<p>
 <code>
  sh
git push origin :refs/tags/<tag-name>
 </code>
</p>
<h2>
 Undo local changes with the last content in head
</h2>
<p>
 <code>
  sh
git checkout -- <file_name>
 </code>
</p>
<h2>
 Revert: Undo a commit by creating a new commit
</h2>
<p>
 <code>
  sh
git revert <commit-ish>
 </code>
</p>
<h2>
 Reset: Discard commits, advised for private branch
</h2>
<p>
 <code>
  sh
git reset <commit-ish>
 </code>
</p>
<h2>
 Reword the previous commit message
</h2>
<p>
 <code>
  sh
git commit -v --amend
 </code>
</p>
<h2>
 See commit history for just the current branch
</h2>
<p>
 <code>
  sh
git cherry -v master
 </code>
</p>
<h2>
 Amend author.
</h2>
<p>
 <code>
  sh
git commit --amend --author='Author Name <email@address.com>'
 </code>
</p>
<h2>
 Reset author, after author has been changed in the global config.
</h2>
<p>
 <code>
  sh
git commit --amend --reset-author --no-edit
 </code>
</p>
<h2>
 Changing a remote's URL
</h2>
<p>
 <code>
  sh
git remote set-url origin <URL>
 </code>
</p>
<h2>
 Get list of all remote references
</h2>
<p>
 <code>
  sh
git remote
 </code>
</p>
<p>
 <strong>
  Alternatives:
 </strong>
 <code>
  sh
git remote show
 </code>
</p>
<h2>
 Get list of all local and remote branches
</h2>
<p>
 <code>
  sh
git branch -a
 </code>
</p>
<h2>
 Get only remote branches
</h2>
<p>
 <code>
  sh
git branch -r
 </code>
</p>
<h2>
 Stage parts of a changed file, instead of the entire file
</h2>
<p>
 <code>
  sh
git add -p
 </code>
</p>
<h2>
 Get git bash completion
</h2>
<p>
 <code>
  sh
curl http://git.io/vfhol > ~/.git-completion.bash && echo '[ -f ~/.git-completion.bash ] && . ~/.git-completion.bash' >> ~/.bashrc
 </code>
</p>
<h2>
 What changed since two weeks?
</h2>
<p>
 <code>
  sh
git log --no-merges --raw --since='2 weeks ago'
 </code>
</p>
<p>
 <strong>
  Alternatives:
 </strong>
 <code>
  sh
git whatchanged --since='2 weeks ago'
 </code>
</p>
<h2>
 See all commits made since forking from master
</h2>
<p>
 <code>
  sh
git log --no-merges --stat --reverse master..
 </code>
</p>
<h2>
 Pick commits across branches using cherry-pick
</h2>
<p>
 <code>
  sh
git checkout <branch-name> && git cherry-pick <commit-ish>
 </code>
</p>
<h2>
 Find out branches containing commit-hash
</h2>
<p>
 <code>
  sh
git branch -a --contains <commit-ish>
 </code>
</p>
<p>
 <strong>
  Alternatives:
 </strong>
 <code>
  sh
git branch --contains <commit-ish>
 </code>
</p>
<h2>
 Git Aliases
</h2>
<p>
 <code>
  sh
git config --global alias.<handle> <command> 
git config --global alias.st status
 </code>
</p>
<h2>
 Saving current state of tracked files without commiting
</h2>
<p>
 <code>
  sh
git stash
 </code>
</p>
<p>
 <strong>
  Alternatives:
 </strong>
 <code>
  sh
git stash save
 </code>
</p>
<h2>
 Saving current state including untracked files
</h2>
<p>
 <code>
  sh
git stash save -u
 </code>
</p>
<p>
 <strong>
  Alternatives:
 </strong>
 <code>
  sh
git stash save --include-untracked
 </code>
</p>
<h2>
 Show list of all saved stashes
</h2>
<p>
 <code>
  sh
git stash list
 </code>
</p>
<h2>
 Apply any stash without deleting from the stashed list
</h2>
<p>
 <code>
  sh
git stash apply <stash@{n}>
 </code>
</p>
<h2>
 Apply last stashed state and delete it from stashed list
</h2>
<p>
 <code>
  sh
git stash pop
 </code>
</p>
<p>
 <strong>
  Alternatives:
 </strong>
 <code>
  sh
git stash apply stash@{0} && git stash drop stash@{0}
 </code>
</p>
<h2>
 Delete all stored stashes
</h2>
<p>
 <code>
  sh
git stash clear
 </code>
</p>
<p>
 <strong>
  Alternatives:
 </strong>
 <code>
  sh
git stash drop <stash@{n}>
 </code>
</p>
<h2>
 Grab a single file from a stash
</h2>
<p>
 <code>
  sh
git checkout <stash@{n}> -- <file_path>
 </code>
</p>
<p>
 <strong>
  Alternatives:
 </strong>
 <code>
  sh
git checkout stash@{0} -- <file_path>
 </code>
</p>
<h2>
 Show all tracked files
</h2>
<p>
 <code>
  sh
git ls-files -t
 </code>
</p>
<h2>
 Show all untracked files
</h2>
<p>
 <code>
  sh
git ls-files --others
 </code>
</p>
<h2>
 Show all ignored files
</h2>
<p>
 <code>
  sh
git ls-files --others -i --exclude-standard
 </code>
</p>
<h2>
 Create new working tree from a repository (git 2.5)
</h2>
<p>
 <code>
  sh
git worktree add -b <branch-name> <path> <start-point>
 </code>
</p>
<h2>
 Create new working tree from HEAD state
</h2>
<p>
 <code>
  sh
git worktree add --detach <path> HEAD
 </code>
</p>
<h2>
 Untrack files without deleting
</h2>
<p>
 <code>
  sh
git rm --cached <file_path>
 </code>
</p>
<p>
 <strong>
  Alternatives:
 </strong>
 <code>
  sh
git rm --cached -r <directory_path>
 </code>
</p>
<h2>
 Before deleting untracked files/directory, do a dry run to get the list of these files/directories
</h2>
<p>
 <code>
  sh
git clean -n
 </code>
</p>
<h2>
 Forcefully remove untracked files
</h2>
<p>
 <code>
  sh
git clean -f
 </code>
</p>
<h2>
 Forcefully remove untracked directory
</h2>
<p>
 <code>
  sh
git clean -f -d
 </code>
</p>
<p>
 <strong>
  Alternatives:
 </strong>
 <code>
  sh
git clean -df
 </code>
</p>
<h2>
 Update all the submodules
</h2>
<p>
 <code>
  sh
git submodule foreach git pull
 </code>
</p>
<p>
 <strong>
  Alternatives:
 </strong>
 <code>
  sh
git submodule update --init --recursive
 </code>
</p>
<p>
 <code>
  sh
git submodule update --remote
 </code>
</p>
<h2>
 Show all commits in the current branch yet to be merged to master
</h2>
<p>
 <code>
  sh
git cherry -v master
 </code>
</p>
<p>
 <strong>
  Alternatives:
 </strong>
 <code>
  sh
git cherry -v master <branch-to-be-merged>
 </code>
</p>
<h2>
 Rename a branch
</h2>
<p>
 <code>
  sh
git branch -m <new-branch-name>
 </code>
</p>
<p>
 <strong>
  Alternatives:
 </strong>
 <code>
  sh
git branch -m [<old-branch-name>] <new-branch-name>
 </code>
</p>
<h2>
 Rebases 'feature' to 'master' and merges it in to master
</h2>
<p>
 <code>
  sh
git rebase master feature && git checkout master && git merge -
 </code>
</p>
<h2>
 Archive the
 <code>
  master
 </code>
 branch
</h2>
<p>
 <code>
  sh
git archive master --format=zip --output=master.zip
 </code>
</p>
<h2>
 Modify previous commit without modifying the commit message
</h2>
<p>
 <code>
  sh
git add --all && git commit --amend --no-edit
 </code>
</p>
<h2>
 Prunes references to remote branches that have been deleted in the remote.
</h2>
<p>
 <code>
  sh
git fetch -p
 </code>
</p>
<p>
 <strong>
  Alternatives:
 </strong>
 <code>
  sh
git remote prune origin
 </code>
</p>
<h2>
 Retrieve the commit hash of the initial revision.
</h2>
<p>
 <code>
  sh
 git rev-list --reverse HEAD | head -1
 </code>
</p>
<p>
 <strong>
  Alternatives:
 </strong>
 <code>
  sh
git rev-list --max-parents=0 HEAD
 </code>
</p>
<p>
 <code>
  sh
git log --pretty=oneline | tail -1 | cut -c 1-40
 </code>
</p>
<p>
 <code>
  sh
git log --pretty=oneline --reverse | head -1 | cut -c 1-40
 </code>
</p>
<h2>
 Visualize the version tree.
</h2>
<p>
 <code>
  sh
git log --pretty=oneline --graph --decorate --all
 </code>
</p>
<p>
 <strong>
  Alternatives:
 </strong>
 <code>
  sh
gitk --all
 </code>
</p>
<h2>
 Deploying git tracked subfolder to gh-pages
</h2>
<p>
 <code>
  sh
git subtree push --prefix subfolder_name origin gh-pages
 </code>
</p>
<h2>
 Adding a project to repo using subtree
</h2>
<p>
 <code>
  sh
git subtree add --prefix=<directory_name>/<project_name> --squash git@github.com:<username>/<project_name>.git master
 </code>
</p>
<h2>
 Get latest changes in your repo for a linked project using subtree
</h2>
<p>
 <code>
  sh
git subtree pull --prefix=<directory_name>/<project_name> --squash git@github.com:<username>/<project_name>.git master
 </code>
</p>
<h2>
 Export a branch with history to a file.
</h2>
<p>
 <code>
  sh
git bundle create <file> <branch-name>
 </code>
</p>
<h2>
 Import from a bundle
</h2>
<p>
 <code>
  sh
git clone repo.bundle <repo-dir> -b <branch-name>
 </code>
</p>
<h2>
 Get the name of current branch.
</h2>
<p>
 <code>
  sh
git rev-parse --abbrev-ref HEAD
 </code>
</p>
<h2>
 Ignore one file on commit (e.g. Changelog).
</h2>
<p>
 <code>
  sh
git update-index --assume-unchanged Changelog; git commit -a; git update-index --no-assume-unchanged Changelog
 </code>
</p>
<h2>
 Stash changes before rebasing
</h2>
<p>
 <code>
  sh
git rebase --autostash
 </code>
</p>
<h2>
 Fetch pull request by ID to a local branch
</h2>
<p>
 <code>
  sh
git fetch origin pull/<id>/head:<branch-name>
 </code>
</p>
<p>
 <strong>
  Alternatives:
 </strong>
 <code>
  sh
git pull origin pull/<id>/head:<branch-name>
 </code>
</p>
<h2>
 Show the most recent tag on the current branch.
</h2>
<p>
 <code>
  sh
git describe --tags --abbrev=0
 </code>
</p>
<h2>
 Show inline word diff.
</h2>
<p>
 <code>
  sh
git diff --word-diff
 </code>
</p>
<h2>
 Show changes using common diff tools.
</h2>
<p>
 <code>
  sh
git difftool -t <commit1> <commit2> <path>
 </code>
</p>
<h2>
 Don’t consider changes for tracked file.
</h2>
<p>
 <code>
  sh
git update-index --assume-unchanged <file_name>
 </code>
</p>
<h2>
 Undo assume-unchanged.
</h2>
<p>
 <code>
  sh
git update-index --no-assume-unchanged <file_name>
 </code>
</p>
<h2>
 Clean the files from
 <code>
  .gitignore
 </code>
 .
</h2>
<p>
 <code>
  sh
git clean -X -f
 </code>
</p>
<h2>
 Restore deleted file.
</h2>
<p>
 <code>
  sh
git checkout <deleting_commit>^ -- <file_path>
 </code>
</p>
<h2>
 Restore file to a specific commit-hash
</h2>
<p>
 <code>
  sh
git checkout <commit-ish> -- <file_path>
 </code>
</p>
<h2>
 Always rebase instead of merge on pull.
</h2>
<p>
 <code>
  sh
git config --global pull.rebase true
 </code>
</p>
<h2>
 List all the alias and configs.
</h2>
<p>
 <code>
  sh
git config --list
 </code>
</p>
<h2>
 Make git case sensitive.
</h2>
<p>
 <code>
  sh
git config --global core.ignorecase false
 </code>
</p>
<h2>
 Add custom editors.
</h2>
<p>
 <code>
  sh
git config --global core.editor '$EDITOR'
 </code>
</p>
<h2>
 Auto correct typos.
</h2>
<p>
 <code>
  sh
git config --global help.autocorrect 1
 </code>
</p>
<h2>
 Check if the change was a part of a release.
</h2>
<p>
 <code>
  sh
git name-rev --name-only <SHA-1>
 </code>
</p>
<h2>
 Dry run. (any command that supports dry-run flag should do.)
</h2>
<p>
 <code>
  sh
git clean -fd --dry-run
 </code>
</p>
<h2>
 Marks your commit as a fix of a previous commit.
</h2>
<p>
 <code>
  sh
git commit --fixup <SHA-1>
 </code>
</p>
<h2>
 Squash fixup commits normal commits.
</h2>
<p>
 <code>
  sh
git rebase -i --autosquash
 </code>
</p>
<h2>
 Skip staging area during commit.
</h2>
<p>
 <code>
  sh
git commit --only <file_path>
 </code>
</p>
<h2>
 Interactive staging.
</h2>
<p>
 <code>
  sh
git add -i
 </code>
</p>
<h2>
 List ignored files.
</h2>
<p>
 <code>
  sh
git check-ignore *
 </code>
</p>
<h2>
 Status of ignored files.
</h2>
<p>
 <code>
  sh
git status --ignored
 </code>
</p>
<h2>
 Commits in Branch1 that are not in Branch2
</h2>
<p>
 <code>
  sh
git log Branch1 ^Branch2
 </code>
</p>
<h2>
 Reuse recorded resolution, record and reuse previous conflicts resolutions.
</h2>
<p>
 <code>
  sh
git config --global rerere.enabled 1
 </code>
</p>
<h2>
 Open all conflicted files in an editor.
</h2>
<p>
 <code>
  sh
git diff --name-only | uniq | xargs $EDITOR
 </code>
</p>
<h2>
 Count unpacked number of objects and their disk consumption.
</h2>
<p>
 <code>
  sh
git count-objects --human-readable
 </code>
</p>
<h2>
 Prune all unreachable objects from the object database.
</h2>
<p>
 <code>
  sh
git gc --prune=now --aggressive
 </code>
</p>
<h2>
 Instantly browse your working repository in gitweb.
</h2>
<p>
 <code>
  sh
git instaweb [--local] [--httpd=<httpd>] [--port=<port>] [--browser=<browser>]
 </code>
</p>
<h2>
 View the GPG signatures in the commit log
</h2>
<p>
 <code>
  sh
git log --show-signature
 </code>
</p>
<h2>
 Remove entry in the global config.
</h2>
<p>
 <code>
  sh
git config --global --unset <entry-name>
 </code>
</p>
<h2>
 Checkout a new branch without any history
</h2>
<p>
 <code>
  sh
git checkout --orphan <branch_name>
 </code>
</p>
<h2>
 Extract file from another branch.
</h2>
<p>
 <code>
  sh
git show <branch_name>:<file_name>
 </code>
</p>
<h2>
 List only the root and merge commits.
</h2>
<p>
 <code>
  sh
git log --first-parent
 </code>
</p>
<h2>
 Change previous two commits with an interactive rebase.
</h2>
<p>
 <code>
  sh
git rebase --interactive HEAD~2
 </code>
</p>
<h2>
 List all branch is WIP
</h2>
<p>
 <code>
  sh
git checkout master && git branch --no-merged
 </code>
</p>
<h2>
 Find guilty with binary search
</h2>
<p>
 ```sh
git bisect start                    # Search start 
git bisect bad                      # Set point to bad commit 
git bisect good v2.6.13-rc2         # Set point to good commit|tag 
git bisect bad                      # Say current state is bad 
git bisect good                     # Say current state is good 
git bisect reset                    # Finish search
</p>
<p>
 ```
</p>
<h2>
 Bypass pre-commit and commit-msg githooks
</h2>
<p>
 <code>
  sh
git commit --no-verify
 </code>
</p>
<h2>
 List commits and changes to a specific file (even through renaming)
</h2>
<p>
 <code>
  sh
git log --follow -p -- <file_path>
 </code>
</p>
<h2>
 Clone a single branch
</h2>
<p>
 <code>
  sh
git clone -b <branch-name> --single-branch https://github.com/user/repo.git
 </code>
</p>
<h2>
 Create and switch new branch
</h2>
<p>
 <code>
  sh
git checkout -b <branch-name>
 </code>
</p>
<p>
 <strong>
  Alternatives:
 </strong>
 <code>
  sh
git branch <branch-name> && git checkout <branch-name>
 </code>
</p>
<h2>
 Ignore file mode changes on commits
</h2>
<p>
 <code>
  sh
git config core.fileMode false
 </code>
</p>
<h2>
 Turn off git colored terminal output
</h2>
<p>
 <code>
  sh
git config --global color.ui false
 </code>
</p>
<h2>
 Specific color settings
</h2>
<p>
 <code>
  sh
git config --global <specific command e.g branch, diff> <true, false or always>
 </code>
</p>
<h2>
 Show all local branches ordered by recent commits
</h2>
<p>
 <code>
  sh
git for-each-ref --sort=-committerdate --format='%(refname:short)' refs/heads/
 </code>
</p>
<h2>
 Find lines matching the pattern (regex or string) in tracked files
</h2>
<p>
 <code>
  sh
git grep --heading --line-number 'foo bar'
 </code>
</p>
<h2>
 Clone a shallow copy of a repository
</h2>
<p>
 <code>
  sh
git clone https://github.com/user/repo.git --depth 1
 </code>
</p>
<h2>
 Search Commit log across all branches for given text
</h2>
<p>
 <code>
  sh
git log --all --grep='<given-text>'
 </code>
</p>
<h2>
 Get first commit in a branch (from master)
</h2>
<p>
 <code>
  sh
git log master..<branch-name> --oneline | tail -1
 </code>
</p>
<h2>
 Unstaging Staged file
</h2>
<p>
 <code>
  sh
git reset HEAD <file-name>
 </code>
</p>
<h2>
 Force push to Remote Repository
</h2>
<p>
 <code>
  sh
git push -f <remote-name> <branch-name>
 </code>
</p>
<h2>
 Adding Remote name
</h2>
<p>
 <code>
  sh
git remote add <remote-nickname> <remote-url>
 </code>
</p>
<h2>
 Show the author, time and last revision made to each line of a given file
</h2>
<p>
 <code>
  sh
git blame <file-name>
 </code>
</p>
<h2>
 Group commits by authors and title
</h2>
<p>
 <code>
  sh
git shortlog
 </code>
</p>
<h2>
 Forced push but still ensure you don't overwrite other's work
</h2>
<p>
 <code>
  sh
git push --force-with-lease <remote-name> <branch-name>
 </code>
</p>
<h2>
 Show how many lines does an author contribute
</h2>
<p>
 <code>
  sh
git log --author='_Your_Name_Here_' --pretty=tformat: --numstat | gawk '{ add += <!-- @doxie.inject start -->; subs += <!-- @doxie.inject end -->; loc += <!-- @doxie.inject start --> - <!-- @doxie.inject end --> } END { printf "added lines: %s removed lines: %s total lines: %s
", add, subs, loc }' -
 </code>
</p>
<p>
 <strong>
  Alternatives:
 </strong>
 <code>
  sh
git log --author='_Your_Name_Here_' --pretty=tformat: --numstat | awk '{ add += <!-- @doxie.inject start -->; subs += <!-- @doxie.inject end -->; loc += <!-- @doxie.inject start --> - <!-- @doxie.inject end --> } END { printf "added lines: %s, removed lines: %s, total lines: %s
", add, subs, loc }' - # on Mac OSX
 </code>
</p>
<h2>
 Revert: Reverting an entire merge
</h2>
<p>
 <code>
  sh
git revert -m 1 <commit-ish>
 </code>
</p>
<h2>
 Number of commits in a branch
</h2>
<p>
 <code>
  sh
git rev-list --count <branch-name>
 </code>
</p>
<h2>
 Alias: git undo
</h2>
<p>
 <code>
  sh
git config --global alias.undo '!f() { git reset --hard $(git rev-parse --abbrev-ref HEAD)@{${1-1}}; }; f'
 </code>
</p>
<p>
 <!-- Don’t remove or change the comment below – that can break automatic updates. More info at <a href="http://npm.im/doxie.inject">http://npm.im/doxie.inject</a>. -->
 <!-- @doxie.inject end -->
</p>
