import re
import argparse
import logging
import sys

# Save what files were already imported
imported_files = {}


def flat_file(path, file, main=False):
    logging.info("Reading file {path}/{file}".format(path=path, file=file))

    flat_source = ""
    global imported_files

    with open("{path}/{file}".format(path=path, file=file)) as f:
        read_data = f.readlines()

    # Match for pragma at level >0
    # ex: pragma solidity 0.5.0;
    # ex: pragma experimental ABIEncoderV2;
    pragma_regex = r"\s*pragma\s*[solidity|experimental].*;"

    for l in read_data:
        # Skip other pragma definitions for included files
        if main is False:
            pragma_match = re.search(pragma_regex, l)
            if pragma_match is not None:
                continue

        # Import files that are referenced
        # ex: import "./contract.sol";
        # ex: import {Contract, Contract2} from "./contracts.sol";
        import_match = re.findall(
            r"^\s*import\s+|(?!{.*}\s*from\s*)[\"|\'](.*)[\"|\']\s*;\s*$", l
        )
        if len(import_match) == 2:
            imported_file = import_match[1]

            if (imported_file is not None) and (
                imported_files.get(imported_file) is None
            ):
                imported_files[imported_file] = True
                logging.debug("Importing file {file}".format(file=imported_file))
                flat_source += flat_file(path=path, file=imported_file)
                flat_source += "\n"
            else:
                logging.debug("Skipping file {file}".format(file=imported_file))

            # Do not add the import clause
            continue

        # Add line
        flat_source += l

    return flat_source


def main():
    class CliParser(argparse.ArgumentParser):
        def error(self, message):
            sys.stderr.write('Error: {}\n'.format(message))
            self.print_help()
            sys.exit(2)

    parser = CliParser()
    parser.add_argument(
        "--folder", help="Folder with contracts", default="./"
    )
    parser.add_argument("--contract", help="Main source Solidity file")
    parser.add_argument("--output", help="Output flattened Solidity file. Otherwise it appends `_flat.sol` to the contract filename.")
    parser.add_argument("--verbose", "-v", action="count", default=0, help="Show details")
    args = parser.parse_args()

    contracts_dir = args.folder
    main_sol = args.contract
    output_sol = args.output
    verbose = args.verbose

    # Set verbosity
    logging.basicConfig(level=logging.INFO)
    if verbose >= 1:
        logging.basicConfig(level=logging.DEBUG)

    source = flat_file(path=contracts_dir, file=main_sol, main=True)

    if not output_sol:
        output_sol = main_sol.split(".")
        output_sol.pop()
        output_sol[-1] += "_flat"
        output_sol.append("sol")
        output_sol = ".".join(output_sol)

    logging.info("Writing flattened file {file}".format(file=output_sol))
    with open(output_sol, "w") as f:
        f.write(source)


if __name__ == "__main__":
    main()
