pragma solidity >=0.4.22 <0.6.0;


contract Ballot {
    address admin;

    constructor() public {
        admin = msg.sender;
    }

    function sum(int a, int b) public returns(int) {
        return a + b;
    }
}
