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
    mapping(uint => uint256) private sales;
    uint256 public immutable updateFrequency;
    uint256 public currTokenId = 0;
    uint256 public immutable initialPrice;
    uint256 public price;
    uint256 k;
    uint256 currentWTS;
    uint256 currentEMA;
    uint256 lastEMA;
    uint256 lastWTS;
    uint256 public deploymentBlock;

    error InsufficientPayment();
    error FailedToSendEther();

    function calculateWTS() public {
        if (block.number - deploymentBlock <= updateFrequency) {
            currentEMA = 0;
            currentWTS = 0;
        } else {
            if ((block.number - deploymentBlock) % updateFrequency == 1) {
                lastEMA = currentEMA;
                lastWTS = currentWTS;
                currentEMA = k * sales[block.number] + currentEMA * (1000 - k);
                currentWTS = 2000 * currentEMA - (k * lastEMA + lastWTS * (1000 - k));
            }
        }
    }

    function calculatePrice() private {
        uint256 ratio = currentWTS / targetWTS;
        if (ratio > 1000) {
            price = price * ratio;
        } else if (ratio < 1000) {
            price = price * (1000 - (250 * k));
        }
    }

    constructor(
    string memory _name,
    string memory _symbol,
    uint256 _targetWTS,
    uint256 _initialPrice,
    uint256 _updateFrequency
    ) ERC721(_name, _symbol) {
        if(currTokenId == 0) {
            deploymentBlock = block.number;
        }
        updateFrequency = _updateFrequency;
        targetWTS = _targetWTS;
        initialPrice = _initialPrice;
        calculateWTS();
    }


    function mint() public payable {
        if (msg.value < price) {
            revert InsufficientPayment();
        }
        
        unchecked {
            _mint(msg.sender, currTokenId++);
        }
        sales[block.number]++;
        calculateWTS();
        calculatePrice();

        uint256 refund = msg.value - price;
        (bool sent, ) = msg.sender.call{value: refund}("Refund");
        if (!sent) {
            revert FailedToSendEther();
        }
    }
}