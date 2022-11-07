import map_version_repo
import os
from _init_ import Editions
from execute import execute_cmd
import platform
from log import logger
from pathlib import Path


class npmException:
    pass


def build_repo():
    system_platform = platform.system()
    for repo_name, repo in map_version_repo.repositories.items():
        if repo_name in (
            "bot-script",
            "loader",
            "service",
            "gui-extend1"
        ):
            logger.info(f"开始编译{repo_name}")
            # if system_platform == "Windows":
            #     build_cmd = "build.bat"
            # elif system_platform == "Linux":
            #     build_cmd = "bash build.sh -r"
            if repo["build_dir"] is not None:
                if system_platform == "Linux":
                    os.chdir(Editions["root_dir"] / repo["build_dir"])
                    execute_cmd(["bash", "build.sh", "-r"])

                else:   # Windows
                    pass

        if repo_name == "rpc1":
            logger.info(f"开始编译{repo_name}")
            if repo["build_dir"] is not None:
                if system_platform == "Linux":
                    os.chdir(Editions["root_dir"] / repo["build_dir"])
                    execute_cmd(["bash", "build.sh", "-r"])

                    src_path = Editions["root_dir"] / repo["build_dir"] / "output/UiBot.Rpc.DotNet.dll"
                    # if src_path.exists():
                    #     logger.info(f"{repo_name} build succeed")
                    dst_path = Editions["root_dir"] / "laiye-libs/rpc/UiBot.Rpc.DotNet.dll"
                    execute_cmd(["cp", src_path, dst_path])

                else:
                    pass

        if repo_name == "deputy":
            logger.info(f"开始编译{repo_name}")
            if repo["build_dir"] is not None:
                if system_platform == "Linux":
                    os.chdir(Editions["root_dir"] / repo["build_dir"])
                    execute_cmd(["bash", "build-all.sh", "-r"])

                    dst_path = Editions["root_dir"] / "laiye-libs/deputy/netcoreapp2.1"
                    execute_cmd("cp ./Output/netcoreapp2.1/linux-x64/Deputy*.dll " + str(dst_path), shell=True)
                else:
                    pass

        if repo_name in (
            "extend",
            "browser-extension"
        ):
            logger.info(f"开始编译{repo_name}")
            if repo["build_dir"] is not None:
                if system_platform == "Linux":
                    os.chdir(Editions["root_dir"] / repo["build_dir"])
                    execute_cmd(["bash", "build.sh"])

        if repo_name in (
            "gui",
            "gui-creator",
            "gui-worker",
            "gui-browser",
            "rpc2",
            "uibot-antd",
            # "gui-uibotd"
        ):
            logger.info(f"开始编译{repo_name}")
            if repo["build_dir"] is not None:
                if system_platform == "Linux":
                    os.chdir(Editions["root_dir"] / repo["build_dir"])
                    for run_count in range(2):
                        res = execute_cmd(["npm", "i"])
                        if "npm ERR" in res.stdout:
                            if run_count == 0:
                                logger.info(f"{repo_name} npm i 错误，重试")
                            else:
                                raise npmException(f"{repo_name} npm i 错误")
                        else:
                            break

                    # if repo_name == "gui-uibotd":
                    #   execute_cmd(["npm", "run", "build"])

                else:
                    pass

    os.chdir(Editions["root_dir"] / "gui")
    execute_cmd(["npm", "run", "build", "creator", "--", "--output-dir=$PWD/output-creator"])
    execute_cmd(["npm", "run", "build", "worker", "--", "--output-dir=$PWD/output-worker"])
    # execute_cmd(["npm", "run", "build", "browser", "--", "--output-dir=$PWD/output-browser"])
