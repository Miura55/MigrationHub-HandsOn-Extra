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
## テーブルの作成
`http://localhost:28001/`でdynamodb-adminを起動して `Create Table`をクリックで新規テーブルを作成します。

![admin](https://i.gyazo.com/09049412b6485e60d8e983b6a8fa0a56.png)

以下の内容でテーブルの設定を行います。

- テーブル名: `unishop`
- ハッシュ名: `uuid`

![create table](https://i.gyazo.com/35cf162937dc13ac03a77b1f7a3ad894.png)

## リクエスト
curlコマンドなどで以下のAPIを試すことができます。

本来はメソッドを指定する必要がありますが、ローカルでは関数の入出力をテストしているだけなので任意のメソッドで実行すれば動作します。
### AddUnicornFromBasket
url: `http://localhost:20080/2015-03-31/functions/function/invocations`

リクエストパラメータ

```json
{
  "uuid": "4b3fc86b-81d0-4614-920e-8184063acf2d",
  "unicorns": [
    {
      "uuid": "16c3e7c0-bba4-11e9-afec-41e09d726297"
    }
  ]
}
```

### RemoveUnicornFromBasket
url: `http://localhost:10080/2015-03-31/functions/function/invocations`

リクエストパラメータ

```json
{
  "uuid": "4b3fc86b-81d0-4614-920e-8184063acf2d",
  "unicorns": [
    {
      "uuid": "16c3e7c0-bba4-11e9-afec-41e09d726297"
    }
  ]
}
```

### GetUnicornFromBasket
url: `http://localhost:30080/2015-03-31/functions/function/invocations`

リクエストパラメータ

```json
{
  "uuid": "4b3fc86b-81d0-4614-920e-8184063acf2d"
}
```
