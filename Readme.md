# Flaterra

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![CircleCI](https://circleci.com/gh/cleanunicorn/flaterra/tree/master.svg?style=shield)](https://circleci.com/gh/cleanunicorn/flaterra)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/98178f0ea4ce44ecbb5dc7a918ba94f7)](https://www.codacy.com/app/lucadanielcostin/flaterra)
[![PyPI](https://img.shields.io/pypi/v/flaterra.svg)](https://pypi.org/project/flaterra/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=cleanunicorn_flaterra&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=cleanunicorn_flaterra)

Inspired by "earth" in Portuguese, terra and the flatness of the Earth.

Flaterra parses the provided Solidity source file and adds any other `imported` files. This is useful if you want to upload your source code to a block explorer for verification, use it with [Remix](https://remix.ethereum.org) or to run analysis on it, for example with [MythX](https://mythx.io/) or [Mythril](https://github.com/ConsenSys/mythril-classic/).

A way to make Solidity source code flat like the earth.

![Flat Earth](./static/flat-earth.png)

## Install

Install it with `pip` from PyPI.

```console
$ pip install --user flaterra
```

## Usage

Specify the main contract you want flatten with `--contract=`.

```console
$ flaterra --contract=ERC20.sol
INFO:root:Reading file .//ERC20.sol
INFO:root:Reading file .//./IERC20.sol
INFO:root:Reading file .//../../math/SafeMath.sol
INFO:root:Writing flattened file ERC20_flat.sol
```

It assumes the contract is in the current folder. If the contract is in another folder specify it with `--folder=contracts/`.

## Details

It is able to read import formats like

```solidity
import "./contract.sol";
import './another_contract.sol';
import {Contract1, Contract2} from "contracts.sol";
```

Pragmas are added only from the main Solidity file. These formats are supported.

```solidity
pragma solidity 0.5.0;
pragma experimental ABIEncoderV2;
```
