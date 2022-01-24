# Migration Hub Hands-On Extra
このレポジトリはMigration HubのRefactor Spacesのハンズオンの延長戦として試したコード一式です。

# 前提条件
このレポジトリで紹介しているlambda関数は以下のレポジトリのハンズオンを行ったあとに試すことを想定しています。

https://github.com/harunobukameda/AWS-Migration-Hub-Refactor-Spaces

# ローカルでの実行
ローカルでテストする用にDockerを用意しています。

以下のコマンドを実行するとLambdaのランタイムの実行環境とDynamo DBのローカル環境が構築されます。

lambdaのコードを変更するたびにこのコマンドを毎回実行する必要があります。

```
docker-compose up -d --build
```
