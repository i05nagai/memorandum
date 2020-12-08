---
title: bitbucket
---

## bitbucket

## API


#### BASE_URL/pull-requests/{pr_id}/comments?{query}

Response

```
{
  "isLastPage": true,
  "limit": 25,
  "size": 1,
  "start": 0,
  "values": [
    {
      "anchor": {
        "diffType": "EFFECTIVE",
        "fromHash": "<hash>",
        "orphaned": false,
        "path": "path/to/file",
        "toHash": "<hash>"
      },
      "author": {
        "active": true,
        "displayName": "<name>",
        "emailAddress": "<email>",
        "id": <id>,
        "links": {
          "self": [
            {
              "href": "<link-to-user>"
            }
          ]
        },
        "name": "<name>",
        "slug": "<name>",
        "type": "NORMAL"
      },
      "comments": [],
      "createdDate": 1597747461555,
      "id": <id>,
      "permittedOperations": {
        "deletable": true,
        "editable": true,
        "transitionable": true
      },
      "properties": {
        "repositoryId": <id>
      },
      "pullRequest": {
        "author": {
          "approved": false,
          "role": "AUTHOR",
          "status": "UNAPPROVED",
          "user": {
            "active": true,
            "displayName": "<name>",
            "emailAddress": "<address>",
            "id": 23181,
            "links": {
              "self": [
                {
                  "href": "<link-to-user>"
                }
              ]
            },
            "name": "<name>",
            "slug": "<name>",
            "type": "NORMAL"
          }
        },
        "closed": false,
        "createdDate": 1597744474293,
        "fromRef": {
          "displayId": "<branch-name>",
          "id": "<branch-id>",
          "latestCommit": "<commit>",
          "repository": {
            "forkable": true,
            "id": <id>,
            "links": {
              "clone": [
                {
                  "href": "<link-to-repo>",
                  "name": "http"
                },
                {
                  "href": "<link-to-repo>",
                  "name": "ssh"
                }
              ],
              "self": [
                {
                  "href": "<link_to-repo>"
                }
              ]
            },
            "name": "<name-repo>",
            "project": {
              "description": "<description>",
              "id": <id>,
              "key": "<key>",
              "links": {
                "self": [
                  {
                    "href": "<link-to-project>"
                  }
                ]
              },
              "name": "<name>",
              "public": false,
              "type": "NORMAL"
            },
            "public": false,
            "scmId": "git",
            "slug": "<name>",
            "state": "AVAILABLE",
            "statusMessage": "Available"
          }
        },
        "id": <id>,
        "links": {
          "self": [
            {
              "href": "<link-to-pr>"
            }
          ]
        },
        "locked": false,
        "open": true,
        "participants": [],
        "reviewers": [],
        "state": "OPEN",
        "title": "<title>",
        "toRef": {
          "displayId": "<branch-name>",
          "id": "<branch-id>",
          "latestCommit": "<commit>",
          "repository": {
            "forkable": true,
            "id": <id>,
            "links": {
              "clone": [
                {
                  "href": "<repo-url>",
                  "name": "http"
                },
                {
                  "href": "<repo-git-url>",
                  "name": "ssh"
                }
              ],
              "self": [
                {
                  "href": "<repo-url>"
                }
              ]
            },
            "name": "<name>",
            "project": {
              "description": "<description>",
              "id": <id>,
              "key": "<key>",
              "links": {
                "self": [
                  {
                    "href": "<link-to-url>"
                  }
                ]
              },
              "name": "<FLUSS>",
              "public": false,
              "type": "NORMAL"
            },
            "public": false,
            "scmId": "git",
            "slug": "<name>",
            "state": "AVAILABLE",
            "statusMessage": "Available"
          }
        },
        "updatedDate": 1597744474293,
        "version": 0
      },
      "severity": "NORMAL",
      "state": "OPEN",
      "tasks": [
        {
          "anchor": {
            "author": {
              "active": true,
              "displayName": "<name>",
              "emailAddress": "<email>",
              "id": 23181,
              "links": {
                "self": [
                  {
                    "href": "<link>"
                  }
                ]
              },
              "name": "<name>",
              "slug": "<name>",
              "type": "NORMAL"
            },
            "createdDate": 1597747461555,
            "id": <id>,
            "permittedOperations": {
              "deletable": true,
              "editable": true,
              "transitionable": true
            },
            "properties": {
              "repositoryId": <id>
            },
            "severity": "NORMAL",
            "state": "OPEN",
            "text": "<comment-text>",
            "type": "COMMENT",
            "updatedDate": 1597747461555,
            "version": 0
          },
          "author": {
            "active": true,
            "displayName": "<name>",
            "emailAddress": "<email>",
            "id": <id>,
            "links": {
              "self": [
                {
                  "href": "<link>"
                }
              ]
            },
            "name": "<name>",
            "slug": "<name>",
            "type": "NORMAL"
          },
          "createdDate": 1597747461000,
          "id": <id>,
          "permittedOperations": {
            "deletable": true,
            "editable": true,
            "transitionable": true
          },
          "state": "OPEN",
          "text": "<text-task>"
        }
      ],
      "text": "<text-comment>",
      "updatedDate": 1597747461555,
      "version": 0
    }
  ]
}
```

## Reference
- [REST API](https://developer.atlassian.com/server/bitbucket/reference/rest-api/)
