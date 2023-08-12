import os
import sys
import subprocess
import pyinstaller


def navigate_to_script_directory():
    script_path = os.path.abspath(__file__)  # 获取当前脚本的绝对路径
    script_directory = os.path.dirname(script_path)  # 获取脚本所在的目录
    os.chdir(script_directory)  # 切换当前工作目录到脚本所在的目录
    return script_directory

#创建虚拟环境
def create_virtual_environment(target_virtual="D:\Langchain大模型\packge_result",
                               environment_name= "package_exe"):
    try:
        os.chdir(target_virtual)
        subprocess.run(f"python3.8 -m venv {environment_name}", shell=True,check=True)
        print("Virtual environment created successfully.")
    except Exception as e:
        print("An error occurred:", e)

#激活虚拟环境
def activate_virtual_environment(environment_name):
    #windows下的虚拟机
    if os.name == "nt":
        activate_command = f"{environment_name}\\Scripts\\activate"
    else:
        activate_command = f"source {environment_name}/bin/activate"
    run_command(activate_command)
    print("Virtual environment activated.")

def package_python_script(script_name,target_virtual="D:\Langchain大模型\packge_result",working_directory):
    #创建虚拟环境
    os.chdir(target_virtual)
    subprocess.run(["python", "-m", "venv", "package_exe"], check=True)
    try:
        subprocess.run(pyinstaller --onefile --add-data "path/to/resource;." --hidden-import "module_name" your_script.py,
        cwd=working_directory,
        shell=True)

        print("Packaging completed successfully.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    script_name = "my_script.py"  # 替换成你要打包的脚本文件名
    package_python_script(script_name)


#关于可执行文件的打包
def exe_packge():
    #开辟虚拟环境
    if os.
    run("virtualenv venv")
    #将配置写入reqirements.txt：
    # pip stall -r reqirements.txt
    #安装项目依赖
    # pip install -reqirements.txt
    #打包操作(产出exe文件)
    pyinstaller -F xxxx


