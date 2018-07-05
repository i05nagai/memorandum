---
title: Vim tag
---

## Vim tag


* `Ctrl+]`
    * the keyword on which the cursor is standing is used as the tag
    * If the cursor is not on a keyword, the first keyword to the right of the cursor is used.
    * Jump to the definition of the keyword under the cursor.
    * Same as ":tag {ident}", where {ident} is the keyword under or after cursor.
* `Ctrl+t`
    * back
* `:tags`
    * show tag stack
* `:[count]ta[g][!] {ident}`
    * Jump to the definition of {ident}, using the information in the tags file(s).
    * Put {ident} in the tag stack. 
    * {ident} can be a regexp pattern,
    * When there are several matching tags for {ident}, jump to the [count] one.
    * When [count] is omitted the first one is jumped to.
* `g<LeftMouse>`
* `<C-LeftMouse>`
* `{Visual}CTRL-]`
    * Same as ":tag {ident}", where {ident} is the text that is highlighted.

:ts[elect][!] [ident]	List the tags that match [ident], using the
			information in the tags file(s).
			When [ident] is not given, the last tag name from the
			tag stack is used.
			See |tag-!| for [!].
			With a '>' in the first column is indicated which is
			the current position in the list (if there is one).
			[ident] can be a regexp pattern, see |tag-regexp|.
			See |tag-priority| for the priorities used in the
			listing.  {not in Vi}
:sts[elect][!] [ident]	Does ":tselect[!] [ident]" and splits the window for
			the selected tag.  {not in Vi}

							*g]*
g]			Like CTRL-], but use ":tselect" instead of ":tag".
			{not in Vi}

							*v_g]*
{Visual}g]		Same as "g]", but use the highlighted text as the
			identifier.  {not in Vi}

							*:tj* *:tjump*
:tj[ump][!] [ident]	Like ":tselect", but jump to the tag directly when
			there is only one match.  {not in Vi}

							*:stj* *:stjump*
:stj[ump][!] [ident]	Does ":tjump[!] [ident]" and splits the window for the
			selected tag.  {not in Vi}

							*g_CTRL-]*
g CTRL-]		Like CTRL-], but use ":tjump" instead of ":tag".
			{not in Vi}

							*v_g_CTRL-]*
{Visual}g CTRL-]	Same as "g CTRL-]", but use the highlighted text as
			the identifier.  {not in Vi}

							*:tn* *:tnext*
:[count]tn[ext][!]	Jump to [count] next matching tag (default 1).  See
			|tag-!| for [!].  {not in Vi}

							*:tp* *:tprevious*
:[count]tp[revious][!]	Jump to [count] previous matching tag (default 1).
			See |tag-!| for [!].  {not in Vi}

							*:tN* *:tNext*
:[count]tN[ext][!]	Same as ":tprevious".  {not in Vi}

							*:tr* *:trewind*
:[count]tr[ewind][!]	Jump to first matching tag.  If [count] is given, jump
			to [count]th matching tag.  See |tag-!| for [!].  {not
			in Vi}

							*:tf* *:tfirst*
:[count]tf[irst][!]	Same as ":trewind".  {not in Vi}

							*:tl* *:tlast*
:tl[ast][!]		Jump to last matching tag.  See |tag-!| for [!].  {not
			in Vi}

							*:lt* *:ltag*
:lt[ag][!] [ident]	Jump to tag [ident] and add the matching tags to a new
			location list for the current window.  [ident] can be
			a regexp pattern, see |tag-regexp|.  When [ident] is
			not given, the last tag name from the tag stack is
			used.  The search pattern to locate the tag line is
			prefixed with "\V" to escape all the special
			characters (very nomagic). The location list showing
			the matching tags is independent of the tag stack.
			See |tag-!| for [!].
			{not in Vi}

## Configuration

## Reference
