import argparse


def add(a: int, b: int) -> int:
    return a + b


def subtract(a: int, b: int) -> int:
    return a - b


def main() -> None:
    parser = argparse.ArgumentParser(description="Simple math CLI")
    parser.add_argument("operation", choices=["add", "sub"])
    parser.add_argument("a", type=int)
    parser.add_argument("b", type=int)
    args = parser.parse_args()

    if args.operation == "add":
        print(add(args.a, args.b))
    else:
        print(subtract(args.a, args.b))


if __name__ == "__main__":
    main()
