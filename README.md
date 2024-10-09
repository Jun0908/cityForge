# CityForge

### Overview
This project aims to empower individuals to invest in and shape their own cities using decentralized technology. By utilizing Real World Assets (RWA) such as automated and unmanned systems, and combining them with data monetization through DePIN (Decentralized Physical Infrastructure Network), this initiative offers a way to revitalize local communities, create new revenue streams, and allow citizens to take control of their environments. 


### Problems
Investors face several significant challenges when it comes to urban infrastructure investments:

Low Returns: Traditional urban infrastructure investments often yield low financial returns, discouraging participation.
Unpredictable Revenues: Revenue streams can be difficult to predict, making it hard for investors to gauge risk and reward.
High Initial Costs: Many urban infrastructure projects require a large upfront investment, which creates barriers to entry, especially for smaller investors or community-driven projects.
These challenges hinder innovation, limit local development, and concentrate control in the hands of large corporations, leaving ordinary citizens with little involvement or benefit.


### Solution
The solution is to introduce decentralized investments in automated and unmanned systems as Real World Assets (RWA), combined with data monetization through DePIN. This approach:

Reduces Costs: Automation and decentralization lower operational costs, making it accessible for smaller investors.
Increases Transparency: The decentralized model ensures greater transparency in operations and revenue distribution.
Creates New Revenue Streams: By leveraging IoT data and other monetizable information, this model introduces additional streams of income for investors.
Additionally, incorporating liquid staking and Miner Extractable Value (MEV) into the investment model ensures higher returns, making urban infrastructure projects more financially viable and attractive to a broader range of investors.


### Technologies I used
<img width="715" alt="スクリーンショット 2024-10-09 12 46 30" src="https://github.com/user-attachments/assets/5321dffb-e2f7-493c-b6f7-9f3d26dd96b0">





### Implementation Status

| Title          |                                                              URL |
| :------------- | ---------------------------------------------------------------: |
| Demo Movie      |  [cityForge-Movie](https://www.youtube.com/watch?v=pY5WoDl1_OY)|
| Pitch Doc    |   [cityForge-presentation](https://docs.google.com/presentation/d/1iivj84G9uyN8AYd-u-iq2lXvWZISgpxH/edit?usp=sharing&ouid=100915926369744357011&rtpof=true&sd=true)|
| Demo Site     |                                 [cityForge-demo](https://town-forge.web.app/) | 
| colosseum   | [cityForge-colosseum](https://arena.colosseum.org/projects/hackathon/cityforge) |



### Development
View [`Makefile`](./Makefile)<br>
※ The backend has not been deployed yet. You need to run the backend locally.
```sh
cp frontend/.env.sample frontend/.env
cp scripts/.env.sample scripts/.env

# run tlsn server
make tlsn_server
# run regression server
make regression_server

# run frontend
make ui_install
make ui_dev
```


### Contracts
**Verifier Contract**

| contract                   |                                                                                                                   contract address |
| :------------------------- | ---------------------------------------------------------------------------------------------------------------------------------: |
| NFT contract    | [4idb71pCuJckDM3iJfgDPw94YyGjm4MgWFH1eYzBT7oyxiV6JRx3gtgNFyGUeSc2rS7oBLaxsUbR7PRbLRJFYoWi](https://explorer.solana.com/tx/4idb71pCuJckDM3iJfgDPw94YyGjm4MgWFH1eYzBT7oyxiV6JRx3gtgNFyGUeSc2rS7oBLaxsUbR7PRbLRJFYoWi?cluster=devnet)|
| Token contract    | [2WnjhDNU5LAbhcYWVGvAhzFBWRHKuyDmJmGT2VtNEf9t](https://explorer.solana.com/address/2WnjhDNU5LAbhcYWVGvAhzFBWRHKuyDmJmGT2VtNEf9t)|



### References
- https://github.com/tlsnotary
- https://learn.sanctum.so/docs/ecosystem/setting-up-an-lst-with-sanctum/creating-the-token-mint
- https://docs.irys.xyz/learn/learn-about-irys/what-is-irys
- https://spl.solana.com/token
