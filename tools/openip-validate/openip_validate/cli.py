import argparse, json, sys, pathlib
from jsonschema import Draft202012Validator

def validate(schema_path: pathlib.Path, examples_dir: pathlib.Path) -> int:
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    errors = []
    for p in examples_dir.glob("*.json"):
        instance = json.loads(p.read_text(encoding="utf-8"))
        for err in validator.iter_errors(instance):
            errors.append(f"{p.name}: {err.message} (at {list(err.path)})")
    if errors:
        print("Validation failed:")
        for e in errors:
            print(" -", e)
        return 1
    print(f"All examples in {examples_dir} valid against {schema_path.name}.")
    return 0

def main(argv=None):
    parser = argparse.ArgumentParser(prog="openip-validate")
    sub = parser.add_subparsers(dest="cmd", required=True)
    v = sub.add_parser("validate", help="Validate examples against a schema")
    v.add_argument("--schema", required=True, type=pathlib.Path)
    v.add_argument("--examples", required=True, type=pathlib.Path)
    args = parser.parse_args(argv)
    if args.cmd == "validate":
        sys.exit(validate(args.schema, args.examples))

if __name__ == "__main__":
    main()