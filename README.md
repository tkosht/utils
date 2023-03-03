# utils

## installation

```
pip install git+https://github.com/tkosht/utils.git
```

## Usage in Python

```



```

## Sample Code


### `conf/params.yml` を作成

```yml: conf/params.yml
test_params:
  a: 2
  b: 7
```

### `run.py` を作成

```python: run.py
import utils


@utils.params.add_args(params_file="conf/params.yml", root_key="/test_params")
def run(a, b):
    print(f"{a=}, {b=}")


if __name__ == "__main__":
    run()

```

### `run.py` を実行

```bash
python run.py 
a=2, b=7
```

