// SPDX-License-Identifier: MIT
pragma solidity >=0.7.0 <0.9.0;

import "./SimpleStorage.sol"; //

contract StorageFactory is SimpleStorage {
    SimpleStorage[] public simpleStorateArray;

    function createSimpleStorageContract() public {
        SimpleStorage simpleStorage = new SimpleStorage();
        simpleStorateArray.push(simpleStorage);
    }

    function sfStore(uint256 _simpleStorageIndex, uint256 _simpleStorageNumber)
        public
    {
        /// Address
        /// ABI (application binary interface)
        SimpleStorage(address(simpleStorateArray[_simpleStorageIndex])).store(
            _simpleStorageNumber
        );
    }

    function sfGet(uint256 _simpleStorageIndex) public view returns (uint256) {
        SimpleStorage(address(simpleStorateArray[_simpleStorageIndex]))
            .retrieve();
    }
}
