import os
from typing import Union
from pathlib import Path
import shutil
from _init_ import Editions
import glob
from log import logger
from execute import execute_cmd
import json
import configparser

SHORT_ARCH = Editions["SHORT_ARCH"]


class CopyException:
    pass


def copy_to_target(src_path: Union[Path, str], dst_path: Union[Path, str]):
    src_path = Path(src_path)
    dst_path = Path(dst_path)

    logger.info(f"copy {src_path} to {dst_path}")
    if src_path.is_file():
        shutil.copy(src_path, dst_path)
    elif src_path.is_dir():
        shutil.copytree(src_path, dst_path, ignore=shutil.ignore_patterns(".git"), copy_function=shutil.copy,
                        dirs_exist_ok=True)
    else:
        err_msg = f"{src_path}路径错误！"
        logger.error(err_msg)
        raise CopyException(err_msg)


def delete_target(target_path: Union[Path, str]):
    target_path = Path(target_path)

    logger.info(f"开始删除 {target_path}")
    if target_path.is_file():
        os.remove(target_path)
    elif target_path.is_dir():
        shutil.rmtree(target_path, ignore_errors=True)
    else:
        err_msg = f"{target_path} 不存在"
        logger.error(err_msg)


def alter(file, old_str, new_str):
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if old_str in line:
                line = new_str
                # line = line.replace(old_str,new_str)
            file_data += line
    with open(file, "w", encoding="utf-8") as f:
        f.write(file_data)


def alter_json(file, **key_newValues):
    with open(file, "r") as jsonFile:
        data = json.load(jsonFile)

    for key, new_value in key_newValues.items():
        data[key] = new_value

    with open(file, "w") as jsonFile:
        json.dump(data, jsonFile, indent=4)


def alter_ini(file, **key_newValues):
    config = configparser.ConfigParser(comment_prefixes='/', allow_no_value=True, strict=False)
    config.read(file)
    a = config.sections()
    for section, key_newValue in key_newValues.items():
        for key, new_value in key_newValue.items():
            config.set(section, key, new_value)

    with open(file, 'w') as configfile:
        config.write(configfile)


repo_copy_path = {
    "gui-extend": [
        {
            "src_path": Editions["root_dir"] / "gui-extend/output",
            "dst_path": Editions["root_dir"] / "pack/deb-files/opt/UiBotEnterprise/contents/gui/resources/node_modules"
        }
    ],
    "rpc": [
        {
            "src_path": Editions["root_dir"] / "rpc/dotnet/rpc/output",
            "dst_path": Editions["root_dir"] / "pack/deb-files/opt/UiBotEnterprise/contents"
        },
        {
            "src_path": Editions["root_dir"] / "rpc/dotnet/rpc/output",
            "dst_path": Editions["root_dir"] / "pack/deb-files/opt/UiBotEnterprise/contents/service"
        }
    ],
    "deputy": [
        {
            "src_path": str(Editions["root_dir"]) + "/deputy/Output/netcoreapp2.1/linux-" + SHORT_ARCH + "/publish",
            "dst_path": Editions["root_dir"] / "pack/deb-files/opt/UiBotEnterprise/contents"
        },
        {
            "src_path": Editions["root_dir"] / "deputy/Output/linux",
            "dst_path": Editions["root_dir"] / "pack/deb-files/opt/UiBotEnterprise/contents"
        }
    ],
    "loader": [
        {
            "src_path": Editions["root_dir"] / "loader/config/*.desktop",
            "dst_path": Editions["root_dir"] / "pack/deb-files/usr/share/applications",
            "is_need_glob": True
        },
        {
            "src_path": Editions["root_dir"] / "loader/output",
            "dst_path": Editions["root_dir"] / "pack/deb-files/opt/UiBotEnterprise"
        }
    ],
    "browser-extension": [
        {
            "src_path": str(
                Editions["root_dir"]) + "/browser-extension/output/netcoreapp2.1/linux-" + SHORT_ARCH + "/publish",
            "dst_path": Editions["root_dir"] / "pack/deb-files/opt/UiBotEnterprise/contents/extensions/browser"
        }
    ],
    "bot-script": [
        {
            "src_path": Editions["root_dir"] / "bot-script/output/lib",
            "dst_path": Editions["root_dir"] / "pack/deb-files/opt/UiBotEnterprise/contents"
        },
        {
            "src_path": Editions["root_dir"] / "bot-script/output/dotnet",
            "dst_path": Editions["root_dir"] / "pack/deb-files/opt/UiBotEnterprise/contents"
        },
        {
            "src_path": Editions["root_dir"] / "bot-script/output/python/lib/StringLibHelper.py",
            "dst_path": Editions["root_dir"] / "pack/deb-files/opt/UiBotEnterprise/contents/extend/python"
        },
        {
            "src_path": Editions["root_dir"] / "bot-script/output/python/lib/StringLibHelper.py",
            "dst_path": Editions[
                            "root_dir"] / "pack/deb-files/opt/UiBotEnterprise/contents/python37/usr/local/lib/python3.7/StringLib.py"
        },
        {
            "src_path": Editions["root_dir"] / "bot-script/output/lang",
            "dst_path": Editions["root_dir"] / "pack/deb-files/opt/UiBotEnterprise/contents/lang"
        },
        {
            "src_path": Editions["root_dir"] / "bot-script/output/config",
            "dst_path": Editions["root_dir"] / "pack/deb-files/opt/UiBotEnterprise/contents"
        }
    ],
    "extend": [
        {
            "src_path": Editions["root_dir"] / "extend/common/Wps/wps-excel/images",
            "dst_path": Editions[
                            "root_dir"] / "pack/deb-files/opt/UiBotEnterprise/contents/extensions/wps/UiBotEt_1.0.0/images"
        },
        {
            "src_path": Editions["root_dir"] / "extend/common/Wps/wps-excel/js",
            "dst_path": Editions[
                            "root_dir"] / "pack/deb-files/opt/UiBotEnterprise/contents/extensions/wps/UiBotEt_1.0.0/js/"
        },
        {
            "src_path": Editions["root_dir"] / "extend/common/Wps/wps-excel/ui",
            "dst_path": Editions[
                            "root_dir"] / "pack/deb-files/opt/UiBotEnterprise/contents/extensions/wps/UiBotEt_1.0.0/ui"
        },
        {
            "src_path": Editions["root_dir"] / "extend/common/Wps/wps-excel/*.js",
            "dst_path": Editions[
                            "root_dir"] / "pack/deb-files/opt/UiBotEnterprise/contents/extensions/wps/UiBotEt_1.0.0/",
            "is_need_glob": True
        },
        {
            "src_path": Editions["root_dir"] / "extend/common/Wps/wps-excel/*.xml",
            "dst_path": Editions[
                            "root_dir"] / "pack/deb-files/opt/UiBotEnterprise/contents/extensions/wps/UiBotEt_1.0.0/",
            "is_need_glob": True
        },
        {
            "src_path": Editions["root_dir"] / "extend/common/Wps/wps-excel/*.html",
            "dst_path": Editions[
                            "root_dir"] / "pack/deb-files/opt/UiBotEnterprise/contents/extensions/wps/UiBotEt_1.0.0/",
            "is_need_glob": True
        },
        {
            "src_path": str(
                Editions["root_dir"]) + "/extend/common/ImageHelper/" + SHORT_ARCH + "/lib/python3.7/site-packages",
            "dst_path": Editions[
                            "root_dir"] / "pack/deb-files/opt/UiBotEnterprise/contents/python37/usr/local/lib/python3.7/site-packages"
        },
        {
            "src_path": Editions["root_dir"] / "extend/lua_mod/TimePlugin/Time.so",
            "dst_path": Editions["root_dir"] / "pack/deb-files/opt/UiBotEnterprise/contents/extend/lua_mod"
        },
        {
            "src_path": Editions["root_dir"] / "extend/lua_mod/ImagePlugin/Image.so",
            "dst_path": Editions["root_dir"] / "pack/deb-files/opt/UiBotEnterprise/contents/extend/lua_mod"
        },
        {
            "src_path": Editions["root_dir"] / "extend/Output/netcoreapp2.1/*.dll",
            "dst_path": Editions["root_dir"] / "pack/deb-files/opt/UiBotEnterprise/contents/extend/NetCore",
            "is_need_glob": True
        },
        {
            "src_path": Editions["root_dir"] / "extend/Output/python",
            "dst_path": Editions["root_dir"] / "pack/deb-files/opt/UiBotEnterprise/contents/extend/python"
        },
        {
            "src_path": Editions["root_dir"] / "extend/lang/zh-CN",
            "dst_path": Editions["root_dir"] / "pack/deb-files/opt/UiBotEnterprise/contents/lang/zh-CN"
        },
        {
            "src_path": Editions["root_dir"] / "extend/lang/zh-TW",
            "dst_path": Editions["root_dir"] / "pack/deb-files/opt/UiBotEnterprise/contents/lang/zh-TW"
        },
        {
            "src_path": Editions["root_dir"] / "extend/lang/en-US",
            "dst_path": Editions["root_dir"] / "pack/deb-files/opt/UiBotEnterprise/contents/lang/en-US"
        }
    ],
    "service": [
        {
            "src_path": Editions["root_dir"] / "service/output/laiye.service",
            "dst_path": Editions["root_dir"] / "pack/deb-files/lib/systemd/system/laiye.service"
        },
        {
            "src_path": Editions["root_dir"] / "service/output/uibot.autostart.desktop",
            "dst_path": Editions["root_dir"] / "pack/deb-files/etc/xdg/autostart/uibot.autostart.desktop"
        },
        {
            "src_path": Editions["root_dir"] / "service/output",
            "dst_path": Editions["root_dir"] / "pack/deb-files/opt/UiBotEnterprise/contents/service"
        }
    ],
    "gui": [
        {
            "src_path": Editions["root_dir"] / "gui/output-creator/contents",
            "dst_path": Editions["root_dir"] / "pack/deb-files/opt/UiBotEnterprise/contents"
        },
        {
            "src_path": Editions["root_dir"] / "gui/output-worker/contents",
            "dst_path": Editions["root_dir"] / "pack/deb-files/opt/UiBotEnterprise/contents"
        }
    ],
    "debian": [
        {
            "src_path": Editions["root_dir"] / "debian-stuff",
            "dst_path": Editions["root_dir"] / "pack/deb-files/DEBIAN"
        }
    ],
    "third-libs": [
        {
            "src_path": Editions["root_dir"] / "third-libs/dotnet-core",
            "dst_path": Editions["root_dir"] / "pack/deb-files/opt/UiBotEnterprise/contents"
        },
        {
            "src_path": Editions["root_dir"] / "third-libs/dotnet-core",
            "dst_path": Editions["root_dir"] / "pack/deb-files/opt/UiBotEnterprise/contents/service"
        }
    ]
}


# 复制工程编译后生成的文件到打包模板
def copy_output_to_pack():
    for repo_name, copy_path in repo_copy_path.items():
        logger.info(f"复制 {repo_name}")
        for path in copy_path:
            if "is_need_glob" in path:
                dst = path["dst_path"]
                file_path_list = glob.glob(str(path["src_path"]))
                for src in file_path_list:
                    copy_to_target(src, dst)
            else:
                copy_to_target(path["src_path"], path["dst_path"])


pdb_file_path = [
    "/pack/deb-files/opt/UiBotEnterprise",
    "/pack/deb-files/opt/UiBotEnterprise/contents",
    "/pack/deb-files/opt/UiBotEnterprise/contents/service",
    "/pack/deb-files/opt/UiBotEnterprise/contents/extensions/browser"
]


def copy_pdb_file():
    logger.info("移动 pdb 文件到 pack/pdbs 作为备份")
    dst_path = Editions["root_dir"] / "pack/pdbs"
    if not dst_path.exists():
        os.mkdir(Editions["root_dir"] / "pack/pdbs")

    for path in pdb_file_path:
        src_path = str(Editions["root_dir"]) + path + "/*.pdb"
        pdb_file_list = glob.glob(src_path)
        for pdb_file in pdb_file_list:
            copy_to_target(pdb_file, dst_path)


delete_file_path = [
    "pack/deb-files/opt/UiBotEnterprise/contents/Deputy.Base.deps.json",
    "pack/deb-files/opt/UiBotEnterprise/contents/Deputy.Robot.deps.json",
    "pack/deb-files/opt/UiBotEnterprise/contents/UiBot.Rpc.DotNet.deps.json",
    "pack/deb-files/opt/UiBotEnterprise/contents/X11Wrapper.deps.json",
    "pack/deb-files/opt/UiBotEnterprise/contents/service/UiBot.Rpc.DotNet.deps.json"
]


def delete_file():
    logger.info("删除不需要的文件")
    for path in delete_file_path:
        path = Editions["root_dir"] / path
        delete_target(path)


dependency_files = [
    "pack/deb-files/opt/UiBotEnterprise/contents/dotnet-deps/Dynamitey.dll",
    "pack/deb-files/opt/UiBotEnterprise/contents/dotnet-deps/ImpromptuInterface.dll",
]


def extract_NetCore():
    os.chdir(Editions["root_dir"])

    execute_cmd(["chmod", "+x", "tools/ncbeauty"])
    url = '"https://gitee.com/liesauer/HostFXRPatcher"'
    logger.info("使用 NetCoreBeauty 来整理 .NetCore 成一份")
    execute_cmd(
        ["./tools/ncbeauty", "-force", "-gitcdn", url, "pack/deb-files/opt/UiBotEnterprise", "contents/dotnet-deps"])
    execute_cmd(
        ["./tools/ncbeauty", "-force", "-gitcdn", url, "pack/deb-files/opt/UiBotEnterprise/contents", "dotnet-deps"])
    execute_cmd(["./tools/ncbeauty", "-force", "-gitcdn", url, "pack/deb-files/opt/UiBotEnterprise/contents/service",
                 "../dotnet-deps"])

    logger.info(f"把一些依赖的文件移回去")
    dst_path = Editions["root_dir"] / "pack/deb-files/opt/UiBotEnterprise/contents/service"

    for dependency_file in dependency_files:
        src_path = Editions["root_dir"] / dependency_file
        copy_to_target(src_path, dst_path)

    src_path = str(Editions["root_dir"]) + "/pack/deb-files/opt/UiBotEnterprise/contents/dotnet-deps/UiBot.Service.*"
    file_list = glob.glob(src_path)
    for file in file_list:
        logger.info(f"move {file} to {dst_path}")
        shutil.move(file, dst_path)


# config_files = [
#     "pack/deb-files/opt/UiBotEnterprise/config.json",
#     "pack/deb-files/opt/UiBotEnterprise/Loader.runtimeconfig.json",
#     "pack/deb-files/lib/systemd/system/laiye.service",
#     "pack/deb-files/etc/xdg/autostart/uibot.autostart.desktop",
#     "pack/deb-files/DEBIAN/control",
#     "pack/deb-files/DEBIAN/postinst"
# ]


def modify_config_files():
    logger.info("开始修改配置文件")
    version = Editions["version"]
    SHORT_ARCH = Editions["SHORT_ARCH"]

    # base_path = "/home/laiye/PycharmProjects/Test"

    base_config_file1 = Editions["root_dir"] / "pack/deb-files/opt/UiBotEnterprise/"
    config_file1 = base_config_file1 / "config.json"
    backup_file1 = base_config_file1 / "config(1).json"
    if not backup_file1.exists():
        copy_to_target(config_file1, backup_file1)
    else:
        copy_to_target(backup_file1, config_file1)
    # config_file1 = base_path + "/config.json"
    key_newValues1 = {"instructionSet": SHORT_ARCH, "currentVersion": version}
    alter_json(config_file1, **key_newValues1)

    base_config_file2 = Editions["root_dir"] / "pack/deb-files/opt/UiBotEnterprise/"
    config_file2 = base_config_file2 / "Loader.runtimeconfig.json"
    backup_file2 = base_config_file2 / "Loader.runtimeconfig(1).json"
    if not backup_file2.exists():
        copy_to_target(config_file2, backup_file2)
    else:
        copy_to_target(backup_file2, config_file2)
    # config_file2 = base_path + "/Loader.runtimeconfig.json"
    key_newValues2 = {"runtimeOptions": {"additionalProbingPaths": [version + "/dotnet-deps"], "tfm": "netcoreapp2.1"}}
    alter_json(config_file2, **key_newValues2)

    base_config_file3 = Editions["root_dir"] / "pack/deb-files/lib/systemd/system/"
    config_file3 = base_config_file3 / "laiye.service"
    backup_file3 = base_config_file3 / "laiye(1).service"
    if not backup_file3.exists():
        copy_to_target(config_file3, backup_file3)
    else:
        copy_to_target(backup_file3, config_file3)
    # config_file3 = base_path + "/laiye.service"
    old_value1 = "ExecStart"
    new_value1 = "ExecStart=/opt/UiBotEnterprise/" + version + "/service/UiBot.Service.Main\n"
    alter(config_file3, old_value1, new_value1)
    old_value2 = '#Environment="LD_LIBRARY_PATH=$LD_LIBRARY_PATH:'
    new_value2 = 'Environment="LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/UiBotEnterprise/' + version + '/python37/usr/local/lib:/opt/UiBotEnterprise/' + version + "\n"
    alter(config_file3, old_value2, new_value2)

    base_config_file4 = Editions["root_dir"] / "pack/deb-files/etc/xdg/autostart/"
    config_file4 = base_config_file4 / "uibot.autostart.desktop"
    backup_file4 = base_config_file4 / "uibot.autostart(1).desktop"
    if not backup_file4.exists():
        copy_to_target(config_file4, backup_file4)
    else:
        copy_to_target(backup_file4, config_file4)
    # config_file4 = base_path + "/uibot.autostart.desktop"
    key_newValues3 = {
        "Desktop Entry": {
            "Exec": "/opt/UiBotEnterprise/" + version + "/service/UiBot.Service.AutoStart"
        }
    }
    alter_ini(config_file4, **key_newValues3)

    base_config_file5 = Editions["root_dir"] / "pack/deb-files/DEBIAN/"
    config_file5 = base_config_file5 / "control"
    backup_file5 = base_config_file5 / "control(1)"
    if not backup_file5.exists():
        copy_to_target(config_file5, backup_file5)
    else:
        copy_to_target(backup_file5, config_file5)
    # config_file5 = base_path + "/control"
    old_value3 = "Version"
    new_value3 = "Version: " + version + "\n"
    alter(config_file5, old_value3, new_value3)
    old_value4 = "Architecture"
    if SHORT_ARCH == "x64":
        new_value4 = "Architecture: " + "amd64\n"
    else:
        new_value4 = "Architecture: " + SHORT_ARCH + "\n"
    alter(config_file5, old_value4, new_value4)
    os.chdir(Editions["root_dir"] / "pack/deb-files")
    res = execute_cmd(["du", "-s", "."])
    out = res.stdout
    index = out.index("\t")
    new_value5 = out[:index]
    old_value5 = "Installed-Size"
    alter(config_file5, old_value5, new_value5)

    base_config_file6 = Editions["root_dir"] / "pack/deb-files/DEBIAN/"
    config_file6 = base_config_file6 / "postinst"
    backup_file6 = base_config_file6 / "postinst(1)"
    if not backup_file6.exists():
        copy_to_target(config_file6, backup_file6)
    else:
        copy_to_target(backup_file6, config_file6)
    # config_file6 = base_path + "/postinst"
    old_value6 = "UIBOT_VERSION"
    new_value6 = "UIBOT_VERSION='" + version + "'"
    alter(config_file6, old_value6, new_value6)


# copy_output_to_pack()
# copy_pdb_file()
# delete_file()
# extract_NetCore()
# modify_config_files()
