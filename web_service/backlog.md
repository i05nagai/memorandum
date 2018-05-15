---
title: Backlog
---

## Backlog

## IssueのExport
CSV, Excelにexportできる。
GitHubへのExportはできない。
columnsは以下の通り。
issueのcommentの数だけcolumnが増える。


* "ID",
* "Project ID",
* "Project Name",
* "Key ID",
* "Key",
* "Issue Type ID",
* "Issue Type",
* "Category ID",
* "Category Name",
* "Version ID",
* "Version",
* "Subject",
* "Description"
    * issue作成時のcomment
* "Status ID"
* "Status"
* "Priority ID"
* "Priority"
* "Milestone ID"
* "Milestone"
* "Resolution ID"
* "Resolution"
* "Assignee ID"
* "Assignee"
* "Create User ID"
* "Created by"
* "Created Date"
* "Parent issue key"
* "Start Date"
* "Due date"
* "Estimated Hours"
* "Actual Hours"
* "Update User ID"
* "Updated by"
* "Updated"
* "Attachment"
* "Shared File"
* "Comment1"
    * 1,2,3とissueのcommentの数だけcolumnがある
* "Comment2"
* "Comment3"



## Tips

### 課題を一括登録する
* [Home · ikikko/backlog-template-issue-gas Wiki](https://github.com/ikikko/backlog-template-issue-gas/wiki)


### migrating Backlog to github issue

```python
import csv
import github
import time


# BASE_URL is URL like
# https://xxxxxx.backlog.jp/view/
BASE_URL = 'https://xxxxxxx.backlog.jp/view/'
# path to exported backlog CSV
PATH_TO_CSV = 'backlog.txt'
# github access token
GITHUB_ACCESS_TOKEN = ''
# exported github repository
GITHUB_REPOSITORY = ''
# close issue if backlog status is close
GITHUB_CLOSE_ISSUE = True
# wait in SLEEP_SECOND to create next issue
GITHUB_ISSUE_SLEEP_SECOND = 8
# wait in SLEEP_SECOND to create next issue comment
GITHUB_ISSUE_COMMENT_SLEEP_SECOND = 5
#
# map backlog username to github username
# __default is used when the username is not found in this mapping
# github.GithubObject.NotSet means not set to GitHub issue
#
USER_MAPPING = {
    # 'backlog-username': 'github-username',
    '__default': github.GithubObject.NotSet,
}
#
# map backlog label to github label
# __default is used when the username is not found in this mapping
# github.GithubObject.NotSet means not set to GitHub issue
#
LABEL_MAPPING = {
    # 'backlog-label-name': 'github-label-name',
    # '__default': github.GithubObject.NotSet,
    '__default': 'type: backlog',
}
#
# map backlog milestone to github milestone
# __default is used when the username is not found in this mapping
# github.GithubObject.NotSet means not set to GitHub issue
#
MILESTONE_MAPPING = {
    # 'backlog-milestone-name': 'github-milestone-name',
    '__default': github.GithubObject.NotSet,
}
#
# map backlog status to github state.
# this is ignored when GITHUB_CLOSE_ISSUE is false.
# __default is used when the username is not found in this mapping
# github.GithubObject.NotSet means not set to GitHub issue
#
# Backlog status: Open/Close/In Progress/Resolved
# Github State: closed, open, all
#
STATE_MAPPING = {
    # 'backlog-status-name': 'github-state-name',
    'Closed': 'closed',
    '__default': github.GithubObject.NotSet,
}


#
# utility
#
def _do_mapping(t, mapping):
    if t in mapping:
        return mapping[t]
    return mapping['__default']


def _do_mapping_list(ts, mapping):
    return [_do_mapping(t, mapping) for t in ts]


def mapping_labels(category_names):
    mapped = [_do_mapping(t, LABEL_MAPPING) for t in category_names]
    # remove github.GithubObject.NotSet
    mapped = list(filter(lambda x: x != github.GithubObject.NotSet, mapped))

    # remove duplicate lables
    mapped = list(set(mapped))

    if len(mapped) == 0:
        return github.GithubObject.NotSet
    else:
        return mapped


def read_file(path_to_csv):
    data = []
    with open(path_to_csv, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data


#
# backlog
#
def preview(row_dict):
    keys = [
        'ID',
        'Project ID',
        'Project Name',
        'Key ID',
        'Key',
        'Issue Type ID',
        'Issue Type',
        'Category ID',
        'Category Name',
        'Version ID',
        'Version',
        'Subject',
        'Description',
        'Status ID',
        'Status',
        'Priority ID',
        'Priority',
        'Milestone ID',
        'Milestone',
        'Resolution ID',
        'Resolution',
        'Assignee ID',
        'Assignee',
        'Create User ID',
        'Created by',
        'Created Date',
        'Parent issue key',
        'Start Date',
        'Due date',
        'Estimated Hours',
        'Actual Hours',
        'Update User ID',
        'Updated by',
        'Updated',
        'Attachment',
        'Shared File'
    ]
    for key in keys:
        print('{0}: {1}'.format(key, row_dict[key]))


def get_issue_url(row_dict):
    return '{0}{1}'.format(BASE_URL, row_dict['Key'])


def normalize_text(text):
    # normalize backlog text
    return text.replace('\\\\n', '\n')


def category_name_to_list(category_name):
    return category_name.split(',')


def supplement_for_body(bi):
    keys = [
        'Created by',
        'Created Date',
        'Parent issue key',
        'Start Date',
        'Updated by',
        'Updated'
    ]
    supp = []
    for key in keys:
        supp.append('* {0}: {1}'.format(key, bi[key]))
    return '\n'.join(supp)


#
# github
#
def get_repository(g, repository_name, repository_type='private'):
    repos = g.get_user().get_repos(type=repository_type)
    for _repo in repos:
        if _repo.name == repository_name:
            repo = _repo
            break

    if repo is None:
        msg = 'repository {0} does not exist'.format(repository_name)
        raise ValueError(msg)
    return repo


def get_issues(g, repository_name, repository_type='private'):
    repo = get_repository(g, repository_name, repository_type)
    return repo.get_issues()


def create_issue_from_repo(
        repo,
        title,
        body,
        assignee=github.GithubObject.NotSet,
        milestone=github.GithubObject.NotSet,
        labels=[],
        assignees=[]):
    print('create issue: {0}'.format(title))
    return repo.create_issue(title, body, assignee, milestone, labels, assignees)


def create_issue(
        g,
        repository_name,
        repository_type,
        title,
        body,
        assignee=github.GithubObject.NotSet,
        milestone=github.GithubObject.NotSet,
        labels=[],
        assignees=[]):
    repo = get_repository(g, repository_name, repository_type)
    return create_issue_from_repo(
        repo, title, body, assignee, milestone, labels, assignees)


def close_issue(issue):
    issue.edit(state='closed')
    print('issue closed')


def github_auth():
    return github.Github(GITHUB_ACCESS_TOKEN)


def create_issue_comment(issue, body):
    print('create issue comment with {0}'.format(body))
    return issue.create_comment(body)


#
# miscs
#
def _issue_comments_from_backlog_to_github(bi):
    # find num of comments
    nums = []
    for key in bi.keys():
        if key is not None and 'Comment' in key:
            num = int(key.replace('Comment', ''))
            nums.append(num)
    sorted(nums)
    # get comments
    comments = []
    for num in nums:
        comment = normalize_text(bi['Comment{0}'.format(num)])
        # remove empty comment
        if len(comment) > 0:
            comments.append(comment)
    return comments


def _issue_from_backlog_to_github(bi):
    title = bi['Subject']
    backlog_url = get_issue_url(bi)
    body_supplement = supplement_for_body(bi)
    body = "{0}\\\\n### Backlog information\\\\n{1}\\\\n{2}".format(
        bi['Description'], backlog_url, body_supplement)
    body = normalize_text(body)
    assignee = _do_mapping(bi['Assignee'], USER_MAPPING)
    milestone = _do_mapping(bi['Milestone'], MILESTONE_MAPPING)
    labels = mapping_labels(bi['Category Name'])
    assignees = github.GithubObject.NotSet

    comments = _issue_comments_from_backlog_to_github(bi)
    state = _do_mapping(bi['Status'], STATE_MAPPING)
    return {
        'title': title,
        'body': body,
        'assignee': assignee,
        'milestone': milestone,
        'labels': labels,
        'assignees': assignees,
        'state': state,
        'comments': comments,
    }


def _create_issue_from_gi(repo, gi):
    title = gi['title']
    body = gi['body']
    assignee = gi['assignee']
    milestone = gi['milestone']
    labels = gi['labels']
    assignees = gi['assignees']
    # issue
    issue = create_issue_from_repo(
        repo, title, body, assignee, milestone, labels, assignees)
    # issue comments
    migrate_issue_comments(issue, gi['comments'])

    if GITHUB_CLOSE_ISSUE and gi['state'] == 'closed':
        close_issue(issue)


def migrate_issue_comments(issue, gi_comments):
    for comment in gi_comments:
        create_issue_comment(issue, comment)
        time.sleep(GITHUB_ISSUE_COMMENT_SLEEP_SECOND)


def migrate_issue_comments_from_issue_num(repo, issue_num, gi_comments):
    issue = repo.get_issue(issue_num)
    migrate_issue_comments(issue, gi_comments)


def migrate_issues(repo, bis):
    for i, bi in enumerate(bis):
        preview(bi)
        gi = _issue_from_backlog_to_github(bi)
        _create_issue_from_gi(repo, gi)
        print('')
        print('')
        time.sleep(GITHUB_ISSUE_SLEEP_SECOND)


def main():
    data = read_file(PATH_TO_CSV)

    g = github_auth()
    repo = get_repository(g, GITHUB_REPOSITORY, 'private')

    # migrate bulk of issues
    migrate_issues(repo, data[30:50])

    # create issue comments from part of comments
    # this snippet is useful for creating issue fails
    #
    # gi = _issue_from_backlog_to_github(data[14])
    # print(gi['comments'][1])
    # migrate_issue_comments_from_issue_num(repo, 150, gi['comments'][1:])


if __name__ == '__main__':
    main()
```

## Reference
