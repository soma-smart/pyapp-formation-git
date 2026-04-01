import argparse


def calculate(operation: str, a: int, b: int) -> int:
    if operation == "add":
        return a + b
    return a - b


def main() -> None:
    parser = argparse.ArgumentParser(description="Simple math CLI")
    parser.add_argument("operation", choices=["add", "sub"])
    parser.add_argument("a", type=int)
    parser.add_argument("b", type=int)
    args = parser.parse_args()

    print(calculate(args.operation, args.a, args.b))


if __name__ == "__main__":
    main()
