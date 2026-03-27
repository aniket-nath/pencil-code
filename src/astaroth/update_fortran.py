import os
import argparse
def main():
    argparser = argparse.ArgumentParser(description="Update *.f90 files to be GPU ready",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    argparser.add_argument("-p", "--pencil-home", help="Where PC is installed", required=True)
    args = argparser.parse_args()
    config = vars(args)
    PC_HOME = config["pencil_home"]
    os.environ["PENCIL_USER"] = "GPU_AUTOTEST"
    #source_command = f"cd {PC_HOME} && source sourceme.sh"
    source_command = ""
    submodule_command = "git submodule update --init --remote"
    build_command = f"cd {PC_HOME}/samples/build-samples/sample0 && pc_build -f GNU-GCC_MPI+GNU-GCC_GPU+GNU-GCC_debug MODIFY_SOURCE_CODE=on"
    command = f"{submodule_command} && {build_command}"
    os.system(command)
    return os.system(f"cd {PC_HOME} && git diff")

if __name__ == "__main__":
    main()
