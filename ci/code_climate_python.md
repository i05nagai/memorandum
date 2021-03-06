---
title: Code Climate Python
---

## Code Climate Python


## Circle CI 2.0
* [CircleCI Test Coverage](https://docs.codeclimate.com/docs/circle-ci-test-coverage-example#section-circleci-20)

```yaml
version: 2.0
jobs:
  build:
    environment:
      CC_TEST_REPORTER_ID: YOUR_REPO_CC_TEST_REPORTER_ID
    docker:
      - image: circleci/php:7.1.9-browsers
    working_directory: ~/repo
    steps:
      - checkout
      - run:
          name: Setup dependencies
          command: |
            sudo composer self-update
            composer install -n --prefer-dist
      - run:
          name: Setup Code Climate test-reporter
          command: |
            curl -L https://codeclimate.com/downloads/test-reporter/test-reporter-latest-linux-amd64 > ./cc-test-reporter
            chmod +x ./cc-test-reporter
      - run:
          name: Run tests
          command: |
            sudo docker-php-ext-enable xdebug
            ./cc-test-reporter before-build
            sudo vendor/bin/phpunit --coverage-clover clover.xml
            ./cc-test-reporter after-build --coverage-input-type clover --exit-code $?
```

## Reference
* [Configuring Test Coverage](https://docs.codeclimate.com/v1.0/docs/configuring-test-coverage)
