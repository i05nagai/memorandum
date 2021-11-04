---
title: Slack
---

## slack


## Register workspace

* Workspace
    * sub domain of `slack.com`
    * i.e. `<workspace-name>.slack.com`
* User
    * register for each workspaces

### 個人用

1. [slack](https://slack.com/)から`Create new team`
2. メールアドレス、user name, team nameをいれてる。
    * 個人用なのでusernameとteamnameは同じで良い。


## Slack bot
- [Building and deploying a Slack app with Python, Bolt, and AWS Amplify](https://www.xiegerts.com/post/slack-app-bolt-python-amplify/)
- [Slack \| Bolt for Python](https://slack.dev/bolt-python/concepts#event-listening)
- [Verifying requests from Slack \| Slack](https://api.slack.com/authentication/verifying-requests-from-slack)
- [Workflow Builder: Steps from apps \| Slack](https://api.slack.com/workflows/steps)

Slack bot can be implemeneted with Lambda + API Gateway (public) + Bolt app.


## Tips

### RSS
* [Add RSS feeds to Slack – Slack Help Center](https://get.slack.help/hc/en-us/articles/218688467-Add-RSS-feeds-to-Slack)

In the channel which you want to subscribe the RSS in,

```
/feed subscribe http://url
```

See all RSSs,

```
/feed list
```

Remove subscribed RSS

```
/feed remove [id]
```

```
/feed help
```


## Reference
* [slack解説](http://creive.me/archives/7161/)
