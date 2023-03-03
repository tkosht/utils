import utils


def run():
    ulid_list = []
    for idx in range(10):
        ulid = utils.build_ulid(prefix="EXM")
        print(f"{idx=}: {ulid=}")
        ulid_list.append(ulid)
    
    # NOTE: ソートしても生成した順(ソート前のulid_list)と一致する
    assert sorted(ulid_list) == ulid_list

if __name__ == "__main__":
    run()
