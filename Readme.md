# Flat Earth

A way to make Solidity source code flat like the earth.

Imports referenced

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