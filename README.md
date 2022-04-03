# Responsive NFT Mint Price Optimization

This repo is my submission to LionHacks 2022. I worked alone on it, and received 0 outside help. 

# Problem Explanation:

NFT Launches are almost always statically priced, usually anywhere from 0.05ETH to 0.5ETH per mint. However, this has always stricken me as extremely inefficient and poorly optimized. Launches that are extremely well received and sell out in seconds are leaving a lot of money on the table with a statically priced model. And NFT launches that are not as well received or hyped often struggle to sell out partially because of a mispriced launch price. 

# Solution:

My algorithm adjusts the price of minting in real time in response to demand. I've included a PDF file called Lionhacks explaining the specifics, but here's a broad overview:
The NFT team will estimate what they think is a fair amount of time (measured in blocks) for their launch to sell out in, given their perceived hype and demand. The algorithm will then compare the selling rate, which is calculated using an algorithm I developed, to the target selling rate. If there's a mismatch in either direction, the algorithm will increase or decrease the price accordingly. 

I've included a Python notebook in python_sims that simulates NFT launches with my algorithm and without. Consistently, the total profit/revenue received by the team is about twice as high as they would've received with a statically priced launch. 

Unfortunately, due to time constraints (and the fact that I'm working alone), I wasn't able to finish the solidity implementation. However, I am certain it can be done in a gas efficient manner, and I plan to continue working on this afterwards.

# What I learned:

Before this hackathon, I had never in my life used Python. During the hackathon, I taught myself Python, I taught myself the matplotlib Library, which I used to create and plot my simulations. I conducted a ton of research into NFT launches, Price adjustment algorithms, and Moving Average algorithms in order to create my final product. I think it definitely needs refinement, and there are aspects I would love to have had the chance to implement (A Price Elasticity of Demand based price adjustment model is an idea I've been toying around with.) 

If you're a judge and you're reading this, I hope you enjoy reading my work, and I thank you for taking the time to help out with the hackathon!
