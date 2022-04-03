//SPDX-License-Identifier: Unlicense
pragma solidity >=0.8.0;

import "hardhat/console.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/utils/Address.sol";
import "@openzeppelin/contracts/utils/math/Math.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@prb/math/contracts/PRBMathSD59x18.sol";


abstract contract Algo is ERC721 {
    using PRBMathSD59x18 for int256;

    uint256 public immutable targetWTS;
    uint256[] public wtsArray;
    uint public immutable updateFrequency;
    uint256 public currTokenId = 0;
    uint public immutable initialPrice;
    int256 currentWTS;
    int256 currentEMA;
    int256 lastEMA;
    uint256 public deploymentBlock;

    error InsufficientPayment();
    error FailedToSendEther();

    function calculateWTS() public {
        if (block.number - deploymentBlock <= updateFrequency) {
            currentEMA = 0;
            currentWTS = 0;
        } else {

        }
    }

    function getPrice() public view returns(int256 price) {

    }

    constructor(
    string memory _name,
    string memory _symbol
    ) ERC721(_name, _symbol) {
        if(currTokenId == 0) {
            deploymentBlock = block.number;
        }
    }


    function mint() public payable {
        int256 price = getPrice();
        uint256 intPrice = uint256(price.toInt());
        if (msg.value < intPrice) {
            revert InsufficientPayment();
        }
        _mint(msg.sender, currTokenId++);

        uint256 refund = msg.value - intPrice;
        (bool sent, ) = msg.sender.call{value: refund}("");
        if (!sent) {
            revert FailedToSendEther();
        }
    }
}