#!/usr/bin/env python3
"""PreToolUse hook: block direct changes to the main branch.

All changes must go through a pull request. This hook denies:
  * Edit / Write / NotebookEdit while the checked-out branch is main/master
  * git commit/merge/rebase/reset/cherry-pick/revert/am/pull while on main/master
  * git push that targets main/master (explicitly, or implicitly from main)

Exit code 2 with a message on stderr tells Claude Code to block the call.
"""
import json
import re
import subprocess
import sys

PROTECTED = ("main", "master")
MUTATING_GIT = r"(commit|merge|rebase|reset|cherry-pick|revert|am|pull)"


def current_branch(cwd):
    try:
        out = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            cwd=cwd or None, capture_output=True, text=True, timeout=10,
        )
        return out.stdout.strip() if out.returncode == 0 else None
    except (OSError, subprocess.SubprocessError):
        return None


def block(reason):
    print(
        f"BLOCKED: {reason}\n"
        "Changes to main must go through a pull request. Create a branch "
        "(git switch -c <name>), commit there, push it, and open a PR.",
        file=sys.stderr,
    )
    sys.exit(2)


def pushes_to_protected(cmd, on_protected):
    """True if a `git push` segment in cmd would update a protected branch."""
    names = "|".join(PROTECTED)
    for seg in re.split(r"&&|\|\||;|\|", cmd):
        if not re.search(r"\bgit\b.*\bpush\b", seg):
            continue
        # Explicit target: `main`, `HEAD:main`, `+main`, `refs/heads/main`
        if re.search(rf"(?:^|[\s:+])(?:refs/heads/)?(?:{names})(?:\s|$)", seg):
            return True
        # Bare push (no refspec) from a protected branch
        if on_protected:
            return True
    return False


def main():
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError:
        sys.exit(0)

    tool = data.get("tool_name", "")
    branch = current_branch(data.get("cwd"))
    on_protected = branch in PROTECTED

    if tool in ("Edit", "Write", "NotebookEdit", "MultiEdit"):
        if on_protected:
            block(f"cannot modify files while on '{branch}'.")
    elif tool == "Bash":
        cmd = (data.get("tool_input") or {}).get("command", "")
        if pushes_to_protected(cmd, on_protected):
            block("git push to main is not allowed.")
        if on_protected and re.search(rf"\bgit\b(\s+-\S+(\s+\S+)?)*\s+{MUTATING_GIT}\b", cmd):
            block(f"cannot run this git command while on '{branch}'.")
    sys.exit(0)


if __name__ == "__main__":
    main()
