from typing import Union
from pathlib import Path
import time
import os
from execute import execute_cmd
from log import logger


def pull_repo(
    repo_name: str,
    repo_url: str,
    repo_path: Union[str, Path],
    include_sub_repo: str,
    rename: str,
    branch: str,
):
    """拉取代码"""
    start_time = time.perf_counter()
    repo_path = Path(repo_path)
    os.chdir(repo_path)
    repo_path_in = repo_path / rename

    if not repo_path_in.exists():
        logger.info(f"开始拉取{repo_name}")
        if include_sub_repo:
            execute_cmd(["git", "clone", "--recursive", repo_url, rename])
        else:
            execute_cmd(["git", "clone", repo_url, rename])
    else:
        logger.info(f"{repo_name}目录已存在")
        os.chdir(repo_path_in)
        _git = repo_path_in / ".git"
        if not _git.exists():
            execute_cmd(["git", "init"])
            execute_cmd(["git", "remote", "add", "origin", repo_url])
        execute_cmd(["git", "checkout", "."])
        execute_cmd(["git", "clean", '-df'])
        execute_cmd(["git", "pull", "origin", "master"])

    logger.info(f"切换到 {branch}")
    os.chdir(repo_path_in)
    execute_cmd(["git", "checkout", branch])
