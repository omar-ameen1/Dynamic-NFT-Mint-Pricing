# Real Time NFT Mint Price Optimization

This repo was my submission to LionHacks 2022.

# Problem Explanation:

NFT Launches are almost always statically priced, usually anywhere from 0.05ETH to 0.5ETH per mint. However, this has always stricken me as extremely inefficient and poorly optimized. Launches that are extremely well received and sell out in seconds are leaving a lot of money on the table with a statically priced model. And NFT launches that are not as well received or hyped often struggle to sell out partially because of a mispriced launch price. 

# Solution:

My algorithm adjusts the price of minting in real time in response to demand. I've included a PDF file called Lionhacks(1) explaining the specifics, but here's a broad overview:
The NFT team will estimate what they think is a fair amount of time (measured in blocks) for their launch to sell out in, given their perceived hype and demand. The algorithm will then compare the selling rate, which is calculated using an algorithm I developed, to the target selling rate. If there's a mismatch in either direction, the algorithm will increase or decrease the price accordingly. 

I've included a Python implementation and a Python notebook in python_sims that simulates NFT launches with my algorithm and without. Consistently, the total profit/revenue received by the team is about twice as high as they would've received with a statically priced launch. 
