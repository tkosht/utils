#!/usr/bin/sh

mkdir -p conf

echo "test_params:
  a: 2
  b: 7
" > conf/params.yml

echo "import utils


@utils.params.add_args(params_file="conf/params.yml", root_key="/test_params")
def run(a, b):
    print(f"{a=}, {b=}")


if __name__ == "__main__":
    run()

" > example.py

echo "Done."
