# Python behave nginx TEST

参考にさせて頂きました。
- [BDD(振る舞い型駆動開発)ツールであるbehaveを使ってサーバテストはできないものか](https://www.ainoniwa.net/pelican/2016/1126a.html)

## Feauture
  - Docker nginx
  - Variable steps
  - table scenario


## ex.docker command
`docker run --name hogehoge -d -p 80:80 nginx`

`docker run --name hogehogesssh -d -p 22:22 nginx`