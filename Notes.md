Build up repository.
$ git init
Initialized empty Git repository in /Users/hanmeiTang/repos/flask_ex/.git/
$ git s
On branch master

Initial commit

nothing to commit (create/copy files and use "git add" to track)
$ git remote add origin git@github.com:HanmeiTang/flask_test.git
$ git pull origin master --allow-unrelated-histories
From github.com:HanmeiTang/flask_test
 * branch            master     -> FETCH_HEAD
Merge made by the 'recursive' strategy.
 README.md | 2 ++
 1 file changed, 2 insertions(+)
 create mode 100644 README.md

