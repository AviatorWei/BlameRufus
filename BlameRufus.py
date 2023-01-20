import argparse
import git
from datetime import datetime, timezone, timedelta

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Arg parse for BlameRufus')
    parser.add_argument('--git_dir', type=str, default=".", help='git repo to analyze, default for current')

    args = parser.parse_args()

    repo = git.Repo(args.git_dir)

    to_blame = "Rufus"
    week = timedelta(days=7)
    msg = f"active branch: {repo.active_branch}\n" \
        + f"local changes: {len(list(repo.index.diff(None))) > 0}\n" \
        + f"recent commit: {datetime.now(timezone.utc) - repo.active_branch.commit.authored_datetime <= week}\n" \
        + f"blame {to_blame}: {repo.active_branch.commit.author.name == to_blame}"
    print(msg)
