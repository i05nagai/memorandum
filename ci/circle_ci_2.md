---
title: Circle CI 2.0
---

## Circle CI 2.0

## Environment variableso
* built-in environment variables
    * [Using Environment Variables - CircleCI](https://circleci.com/docs/2.0/env-vars/#circleci-built-in-environment-variables)
    * `CIRCLE_SHA1`
        * buildしているgit commitのSHA1
    * `CIRCLE_TAG`
        * gittag
    * `CIRCLE_WORKING_DIRECTORY`

## Configuration
* [Configuration Reference - CircleCI](https://circleci.com/docs/2.0/configuration-reference/)
`.circleci/config.yml`

* `workflows`
    * jobsの実行順序を記載する
* `jobs`
    * jobsの定義をかく
* `steps`
    * actions in job
    * collections of executable commands

```yaml
version: 2
jobs:
  one:
    docker:
      - image: circleci/ruby:2.4.1
    steps:
      - checkout
      - run: echo "A first hello"
      - run: mkdir -p my_workspace
      - run: echo "Trying out workspaces" > my_workspace/echo-output
      - persist_to_workspace:
          # Must be an absolute path, or relative path from working_directory
          root: my_workspace
          # Must be relative path from root
          paths:
            - echo-output      
  two:
    docker:
      - image: circleci/ruby:2.4.1
    steps:
      - checkout
      - run: echo "A more familiar hi"  
      - attach_workspace:
          # Must be absolute path or relative path from working_directory
          at: my_workspace

      - run: |
          if [[ $(cat my_workspace/echo-output) == "Trying out workspaces" ]]; then
            echo "It worked!";
          else
            echo "Nope!"; exit 1
          fi
workflows:
  version: 2
  one_and_two:
    jobs:
      - one
      - two:
          requires:
            - one
```

## Steps
* `checkout`
    * source codeのcheckout
* `run:`
    * execute commands

```yaml
    steps:
      - checkout # Special step to checkout your source code
      - run: # Run step to execute commands, see
      # circleci.com/docs/2.0/configuration-reference/#run
          name: Running tests
          command: make test # executable command run in
          # non-login shell with /bin/bash -eo pipefail option
          # by default.
```

## Job
* [Jobs and Steps - CircleCI](https://circleci.com/docs/2.0/jobs-steps/)

* `docker/machine/macos`
    * jobを実行する環境
    * dockerはdocker image
    * docker環境で docker commandを使う場合は、`steps`で`- setup_remote_docker`を指定する

```yaml
jobs:
  <job-name>:
    docker:
      - image: <image-name>
        environment:
          KEY: VALUE
    steps:
      - setup_remote_docker
  <job-name>:
    machine:
  <job-name>:
    macos:
      xcode:
```

```yaml
version: 2
jobs:
  build:
    docker:
      - image: circleci/<language>:<version TAG>
    steps:
      - checkout
      - run: <command>
  test:
    docker:
      - image: circleci/<language>:<version TAG>
    steps:
      - checkout
      - run: <command>
workflows:
  version: 2
  build_and_test:
    jobs:
      - build
      - test
```

## Workflow
* [Orchestrating Workflows - CircleCI](https://circleci.com/docs/2.0/workflows/)

jobのつながりを記述する。
`triggers`で日付で実行を制御できる。


```yaml
workflows:
  version: 2
  <workflow-name>:
    jobs:
      - <job-name>
    triggers:
      - schedule:
          cron: "0 0 * * *"
          filters:
            branches:
              only:
                - master
                - beta
```


```yaml
workflows:
  version: 2
  commit:
    jobs:
      - build
      - test
      - test1:
          requires:
            - build
      - test2:
          requires:
            - test1
      - deploy:
          requires:
            - test2
      - deploy
  nightly:
    triggers:
      - schedule:
          cron: "0 0 * * *"
          filters:
            branches:
              only:
                - master
                - beta
    jobs:
      - coverage
```


## Reference
* [2.0 Docs - CircleCI](https://circleci.com/docs/2.0/)
