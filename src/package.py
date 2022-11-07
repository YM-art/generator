from map_version_repo import repositories
import _init_
import git
import build
import assemble


def pull_all_repo():
    for repo_name, repo in repositories.items():
        repo_url = repo["repo_url"]
        repo_path = _init_.Editions["root_dir"] / repo["repo_path"]
        include_sub_repo = repo["include_sub_repo"]
        rename = repo["rename"]
        branch = repo["branch"]

        git.pull_repo(repo_name, repo_url, repo_path, include_sub_repo, rename, branch)


def assemble_pack():
    src_pack_path = _init_.Editions["root_dir"] / "pack-template"
    dst_pack_path = _init_.Editions["root_dir"] / "pack"
    assemble.delete_target(dst_pack_path)
    assemble.copy_to_target(src_pack_path, dst_pack_path)

    assemble.copy_output_to_pack()
    assemble.copy_pdb_file()
    assemble.delete_file()
    assemble.extract_NetCore()
    assemble.modify_config_files()


def main():
    # 步骤一： 拉取仓库
    pull_all_repo()
    # 步骤二： 编译
    build.build_repo()
    # 步骤三：组装与修改配置文件
    assemble_pack()
    #步骤四：打包成deb文件
    assemble.pack_deb()


if __name__ == '__main__':
    main()
