---
title: disown
---

## disown
To delete/remove jobs or to tell the shell not to send a HUP signal use disown command. 
Remove jobs from the table of active job.

## CLI

```
disown jobID
disown jobID1 jobID2 ... jobIDN
disown [options] jobID1 jobID2 ... jobIDN
```

## Usage
Check jobs

```
jobs -l
```

How do I remove all jobs?

```
disown -a
```

How do I remove only running jobs?

```
disown -r
```

## Reference
* [Linux / Unix: disown Command Examples - nixCraft](https://www.cyberciti.biz/faq/unix-linux-disown-command-examples-usage-syntax/)
