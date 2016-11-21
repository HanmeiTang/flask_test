Build up repository.

```shell
$ git init
Initialized empty Git repository in /Users/hanmeiTang/repos/flask_ex/.git/
```

```shell
# Add remote
$ git remote add origin git@github.com:HanmeiTang/flask_test.git

# Git pull with "unrelated-histories error" ignored
$ git pull origin master --allow-unrelated-histories
From github.com:HanmeiTang/flask_test
 * branch            master     -> FETCH_HEAD
Merge made by the 'recursive' strategy.
 README.md | 2 ++
 1 file changed, 2 insertions(+)
 create mode 100644 README.md
# Git pull from specific remote
$ git push origin master
Counting objects: 16, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (13/13), done.
Writing objects: 100% (16/16), 400.23 KiB | 0 bytes/s, done.
Total 16 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), done.
To github.com:HanmeiTang/flask_test.git
   99c0271..b8cc44e  master -> master
 ```
```shell
# set tracking information for master branch
$ git branch --set-upstream-to=origin/master master
```

Generate requirement file.
```shell
$ pip freeze > requirements.txt
```
