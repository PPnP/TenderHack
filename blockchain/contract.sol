pragma solidity >=0.4.22 <0.6.0;


contract PPnP {
    address admin;
    uint counter = 0;

    constructor() public {
        admin = msg.sender;
    }

    modifier onlyAdmin {
        require(msg.sender == admin);
        _;
    }

    struct User {
        string name;
        string login;
        string email;
        string hashedPassword;
    }

    mapping (uint=>User) public Users;

    function addUser(string memory _name, string memory _email, string memory _login, string memory _hashedPassword) public {
        Users[counter].name=_name;
        Users[counter].email=_email;
        Users[counter].login=_login;
        Users[counter].hashedPassword=_hashedPassword;
        counter++;
    }
}