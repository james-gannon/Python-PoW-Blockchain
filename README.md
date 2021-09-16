# Python-PoW-Blockchain
Interactive Proof of Work blockchain using Flask-based web application and Postman

Two Get requests are performed:
1) A "mine block" request to mine the next block on the blockchain; and a
2) "Get chain" request to display each block and its data in the Postman application

First let's start off with the "get_chain" request, and append to the http://127.0.0.1:5000 request URL in Postman:

![image](https://user-images.githubusercontent.com/50316657/133530419-1d43a6a4-6f7c-4fc4-a9ec-4d55ce14ef56.png)

The "get_chain" request has been added to the request URL, the "Send" button is clicked, and our genesis block is created on-chain, indicated by the arrow in red. Each block contains data detailing "index" (block #), "previous hash", "proof" (required for mining consensus), and "timestamp". These blocks can be built to be more complex, containing more data such as transaction amount, user identity...etc.

To mine some new blocks, we change the URL request extension from "get_chain", to "mine_block", and press enter:

![image](https://user-images.githubusercontent.com/50316657/133531004-2afa3bda-5be9-4ecb-a822-68e6218268e0.png)

The second block is mined, as indicated by "index": 2, and our nonce, or, "proof" value is 533.
This means that the mathematical solution to generating a cryptographic hash of the square of the new proof, minus the square of 1, starting with four leading zeros (0000), is **533**.
In other words, the cryptographic hash of the encoded string of the square of 533 minus the square of 1, starts with four leading zeros.

We call a "get_chain" request and can now see both the genesis block, and the second block that we just mined, with a "length": of 2:

![image](https://user-images.githubusercontent.com/50316657/133531972-2aa0f009-93a3-4264-9b80-c46e40a8ef25.png)

Let's call a "mine_block" request 10 times and generate 10 more blocks:

![image](https://user-images.githubusercontent.com/50316657/133532122-fe539085-31c3-4817-bc8d-b387a65762d8.png)

The "index" now reads "12".

Let's call one last "get_chain" request to see our entire blockchain of our recently mined blocks!

![image](https://user-images.githubusercontent.com/50316657/133532415-1d30ad09-0d31-4b53-8798-925c0e6d1f23.png)
![image](https://user-images.githubusercontent.com/50316657/133532439-aa09714e-11f1-4b97-80ff-eb21c04936df.png)
![image](https://user-images.githubusercontent.com/50316657/133532484-303ba355-d83c-4571-bcb2-8bf86a963e9b.png)

Our entire blockchain is visible, and has a "length" of 12 as expected.
