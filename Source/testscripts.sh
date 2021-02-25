# #!/bin/bash
# set -eu
# # Switch into every git repo directory under a path,
# # pull the latest changes and switch back to
# # the parent directory to repeat the process
# reposPath=""
# for repoDir in $(ls -d ${reposPath}/*/) do
# cd ${repoDir}
# git commit -m "This shell has worked"
# cd ../
# done

#!/bin/bash
set -eu

echo "Starting Tests"

if python3 -m unittest discover .;
then

git add testscripts.shell
git commit -m "{$1}"
echo "All tests passed"
fi
