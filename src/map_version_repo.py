"""记录版本与库之间的映射关系，打包时从此取数
库版本字段信息解释如下：
{
    "bot-script": # 库名称
    {
        "sequence_number": 0, # 拉取仓库，编译的顺序
        "repo_url": "https://git.laiye.com/laiye-rpa-client/bot-script.git",
        "repo_path": "", # 在此路径下拉取仓库，省略根目录，若直接在根目录拉取则为空
        "include_sub_repo": "--recursive", # 是否包含子库,包含为TRUE，不包含为FALSE
        "rename": "bot-script", 仓库文件夹名称
        "branch_type": "branch", # 类型: 分支 或 tag 或 commit ID
        "branch": "master", 分支 或 tag 或 commit ID 名称
        "build_dir": "bot-script" # 在此路径下编译，省略根目录
    }
}
"""

repositories = {
    "bot-script": {
        "sequence_number": 0,
        "repo_url": "https://git.laiye.com/laiye-rpa-client/bot-script.git",
        "repo_path": "",
        "include_sub_repo": True,
        "rename": "bot-script",
        "branch_type": "branch",
        "branch": "master",
        "build_dir": "bot-script"
    },
    "deputy": {
        "sequence_number": 1,
        "repo_url": "https://git.laiye.com/laiye-rpa-client/deputy.git",
        "repo_path": "",
        "include_sub_repo": False,
        "rename": "deputy",
        "branch_type": "branch",
        "branch": "master",
        "build_dir": "deputy",
    },
    "gui-extend1": {
        "sequence_number": 2,
        "repo_url": "https://git.laiye.com/laiye-rpa-client/gui-extend.git",
        "repo_path": "",
        "include_sub_repo": False,
        "rename": "gui-extend",
        "branch_type": "branch",
        "branch": "master",
        "build_dir": "gui-extend"
    },
    "rpc1": {
        "sequence_number": 3,
        "repo_url": "https://git.laiye.com/laiye-rpa-client/rpc.git",
        "repo_path": "",
        "include_sub_repo": False,
        "rename": "rpc",
        "branch_type": "branch",
        "branch": "master",
        "build_dir": "rpc/dotnet/rpc"
    },
    "loader": {
        "sequence_number": 4,
        "repo_url": "https://git.laiye.com/laiye-rpa-client/loader.git",
        "repo_path": "",
        "include_sub_repo": False,
        "rename": "loader",
        "branch_type": "branch",
        "branch": "master",
        "build_dir": "loader"
    },
    "browser-extension": {
        "sequence_number": 5,
        "repo_url": "https://git.laiye.com/laiye-rpa-client/browser-extension.git",
        "repo_path": "",
        "include_sub_repo": False,
        "rename": "browser-extension",
        "branch_type": "branch",
        "branch": "master",
        "build_dir": "browser-extension"
    },
    "extend": {
        "sequence_number": 6,
        "repo_url": "https://git.laiye.com/laiye-rpa-client/extend.git",
        "repo_path": "",
        "include_sub_repo": False,
        "rename": "extend",
        "branch_type": "branch",
        "branch": "master",
        "build_dir": "extend"
    },
    "service": {
        "sequence_number": 7,
        "repo_url": "https://git.laiye.com/laiye-rpa-client/service.git",
        "repo_path": "",
        "include_sub_repo": False,
        "rename": "service",
        "branch_type": "branch",
        "branch": "master",
        "build_dir": "service"
    },
    "debian-stuff": {
        "sequence_number": 8,
        "repo_url": "https://git.laiye.com/laiye-rpa-client/debian-stuff.git",
        "repo_path": "",
        "include_sub_repo": False,
        "branch_type": "branch",
        "branch": "master",
        "rename": "debian-stuff"
    },
    "gui": {
        "sequence_number": 9,
        "repo_url": "https://git.laiye.com/laiye-rpa-client/gui.git",
        "repo_path": "",
        "include_sub_repo": False,
        "rename": "gui",
        "branch_type": "branch",
        "branch": "master",
        "build_dir": "gui"
    },
    "rpc2": {
        "sequence_number": 10,
        "repo_url": "https://git.laiye.com/laiye-rpa-client/rpc.git",
        "repo_path": "gui",
        "include_sub_repo": False,
        "rename": "rpc",
        "branch_type": "branch",
        "branch": "master",
        "build_dir": "gui/rpc/javascript"
    },
    "gui-extend2": {
        "sequence_number": 11,
        "repo_url": "https://git.laiye.com/laiye-rpa-client/gui-extend.git",
        "repo_path": "gui",
        "include_sub_repo": False,
        "rename": "extend",
        "branch_type": "branch",
        "branch": "master",
        "build_dir": ""
    },
    "gui-creator": {
        "sequence_number": 12,
        "repo_url": "https://git.laiye.com/laiye-rpa-client/gui-creator.git",
        "repo_path": "gui",
        "include_sub_repo": False,
        "rename": "creator",
        "branch_type": "branch",
        "branch": "master",
        "build_dir": "gui/creator"
    },
    "gui-worker": {
        "sequence_number": 13,
        "repo_url": "https://git.laiye.com/laiye-rpa-client/gui-worker.git",
        "repo_path": "gui",
        "include_sub_repo": False,
        "rename": "worker",
        "branch_type": "branch",
        "branch": "master",
        "build_dir": "gui/worker"
    },
    "gui-browser": {
        "sequence_number": 14,
        "repo_url": "https://git.laiye.com/laiye-rpa-client/gui-browser.git",
        "repo_path": "gui",
        "include_sub_repo": False,
        "rename": "browser",
        "branch_type": "branch",
        "branch": "master",
        "build_dir": "gui/browser"
    },
    "uibot-antd": {
        "sequence_number": 15,
        "repo_url": "https://git.laiye.com/laiye-rpa-client/uibot-antd.git",
        "repo_path": "gui",
        "include_sub_repo": False,
        "rename": "third-party/uibot-antd",
        "branch_type": "branch",
        "branch": "master",
        "build_dir": "gui/third-party/uibot-antd"
    },
    "gui-uibotd": {
        "sequence_number": 16,
        "repo_url": "https://git.laiye.com/laiye-rpa-client/gui-uibotd.git",
        "repo_path": "gui/third-party",
        "include_sub_repo": False,
        "rename": "gui-uibotd",
        "branch_type": "branch",
        "branch": "master",
        "build_dir": "gui/third-party/gui-uibotd"
    }
}

repositories = dict(
    sorted(repositories.items(), key=lambda d: d[1]["sequence_number"])
)
