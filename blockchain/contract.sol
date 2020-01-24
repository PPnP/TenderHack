pragma solidity >=0.4.22 <0.6.0;


contract Ballot {
    address admin;

    constructor() public {
        admin = msg.sender;
        countOfData = 0;
    }

    mapping(uint=>int) public dataStorage;
    uint public countOfData;

    function sum(int a, int b) public returns(int) {
        return a + b;
    }

    function addNumber(int a) public {
        dataStorage[countOfData] = a;
        countOfData++;
    }
}