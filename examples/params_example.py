import utils


@utils.add_args(params_file="conf/params.yml", root_key="/test_params")
def run(a, b):
    print(f"{a=}, {b=}")


if __name__ == "__main__":
    run()
