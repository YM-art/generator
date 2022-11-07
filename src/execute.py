import logging
import subprocess
from typing import Sequence, Dict
from pathlib import Path
import os

logger = logging.getLogger("execute")
# logger.setLevel(logging.info)
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)


class ExecuteCMDException:
    pass


def execute_cmd(
    *popenargs,
    capture_output=True,
    shell=False,
    timeout=None,
    check=False,
    encoding="utf-8",
    **kwargs,
):
    kwargs["capture_output"] = capture_output
    kwargs["shell"] = shell
    kwargs["timeout"] = timeout
    kwargs["check"] = check
    if encoding:
        kwargs["encoding"] = encoding

    # if isinstance(popenargs, Sequence):
    #     if isinstance(popenargs[0], str):
    #         cmd_text = popenargs[0]
    #     elif isinstance(popenargs[0], Sequence):
    #         cmd_text = " ".join(popenargs[0])
    #     elif isinstance(popenargs[0], Path):
    #         cmd_text = popenargs[0].name
    #         kwargs["cwd"] = popenargs[0].parent
    #     else:
    #         raise ValueError(f"参数遇到未知情况：{popenargs}")
    # else:
    #     raise ValueError(f"参数遇到未知情况：{popenargs}")

    # print(f"开始执行{popenargs}")

    try:
        logger.info(f"开始执行{popenargs}")
        _res = subprocess.run(*popenargs, **kwargs)
    except Exception as e:
        error_msg = f"执行命令出错：{os.getcwd()} - {popenargs}\n{str(e)}"
        logger.error(error_msg)
        raise ExecuteCMDException(error_msg)
    else:
        if _res.returncode == 0:
            output = f"{_res.stdout}\n{_res.stderr}"
            logger.info(output)
            return _res
        else:
            error_output = f"{_res.stdout}\n{_res.stderr}"
            error_msg = f"执行命令出错：{os.getcwd()} - {popenargs}\n{error_output}"
            logger.error(error_msg)
            raise ExecuteCMDException(error_msg)


