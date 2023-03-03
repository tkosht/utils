#!/usr/bin/sh

mkdir -p conf

cat << YML > conf/params.yml
test_params:
  a: 2
  b: 7
YML

cat << PYSCRIPT > run.py
import utils


@utils.params.add_args(params_file="conf/params.yml", root_key="/test_params")
def run(a, b):
    print(f"{a=}, {b=}")


if __name__ == "__main__":
    run()
PYSCRIPT

echo "Done."
