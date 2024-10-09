# cityForge

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


### Usecase
- Under-collateralized lending protocols leveraging off-chain credit data.
- Whitelisting for GameFi projects and NFT marketplace launchpads using users' off-chain activities.
- Selective disclosure with privacy-preserving data through DID/VC.

### Technologies I used
<img width="723" alt="スクリーンショット 2024-08-24 20 24 01" src="https://github.com/user-attachments/assets/2c34529d-1f0c-4245-b6ee-932d7fc7fdfc">


### Architecture
```mermaid
  sequenceDiagram
    actor User
    participant BankWebsite as Bank Account Web
    participant ChromeExt as zkCredit (Chrome Extension)
    participant Frontend as zkCredit Dashboard
    participant RustServer as Rust Verify
    participant Verifier as Verifier Contract
    participant ENS as ENS

    User->>BankWebsite: 1. Login
    BankWebsite-->>ChromeExt: HTTPS Response with user data and signature
    ChromeExt->>ChromeExt: 2. Generate zkTLSProof from user data
    ChromeExt-->>User: 3. Provide zkTLSProof for download
    User->>Frontend: 4. Upload zkTLSProof to dashboard
    Frontend->>RustServer: 5. Send zkTLSProof for verification
    RustServer-->>Frontend: 6. Return verification result
    Frontend->>Frontend: 7. Generate zkMLProof<br/>(private input: input data, public input: existing model)
    Frontend->>Verifier: 8. Send zkMLProof to verifier contract
    Verifier-->>Frontend: 9. Return verification result<br/>(public output: inference result)
    Frontend->>ENS: 10. Store verification result on ENS text records

```

### Implementation Status

| Title          |                                                              URL |
| :------------- | ---------------------------------------------------------------: |
| Demo Movie      |  [https://youtu.be/WDGJQbM-rik](https://www.youtube.com/watch?v=pY5WoDl1_OY))|
| Pitch Doc    |   [zkcredit-presentation](https://www.canva.com/design/DAGOvSFvJ4E/SfJTYw3sauGSbj1k4oQdDg/edit?utm_content=DAGOvSFvJ4E&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton) |
| Demo Site     |                                 [zkcredit-demo](https://zk-credit-teal.vercel.app/) | 
| Contract   | [zkcredit-contracts](https://github.com/wasabijiro/zkCredit/tree/main/contracts) |
| Frontend |         [zkcredit-front](https://github.com/wasabijiro/zkCredit/tree/main/frontend) |


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

### What's next for

- Support for Chrome extension
- Generate TLS Notary proof on the client side
- Implement Solidity contract to verify TLS Notary proof
- Integrate TLS Notary and zkML into a single circuit

### Contracts
**Verifier Contract**

| contract                   |                                                                                                                   contract address |
| :------------------------- | ---------------------------------------------------------------------------------------------------------------------------------: |
| Ethereum Sepolia    | [0xf2c9d93716e818bda8fd9cd13b692ec5302d5568](https://sepolia.etherscan.io/address/0xf2c9d93716e818bda8fd9cd13b692ec5302d5568#code)|
| Scroll Sepolia    | [0x677ab31a9d777eedbc88ce2198dce8de9378e78f](https://sepolia.scrollscan.com/address/0x677ab31a9d777eedbc88ce2198dce8de9378e78f)|
| Nero Testnet    | [0x677aB31a9D777eEdbc88CE2198dcE8de9378E78f](https://testnetscan.nerochain.io/address/0x677aB31a9D777eEdbc88CE2198dcE8de9378E78f)|
| NeoX Testnet    | [0xC502e62C2Dc0686044572465A653CdF81Ca15A48](https://neoxt4scan.ngd.network/address/0x677ab31a9d777eedbc88ce2198dce8de9378e78f)|
| Linea Testnet   | [0x677ab31a9d777eedbc88ce2198dce8de9378e78f](https://sepolia.lineascan.build/address/0x677ab31a9d777eedbc88ce2198dce8de9378e78f)|


### References
- https://github.com/tlsnotary
- https://github.com/storswiftlabs/python2noir
- https://github.com/storswiftlabs/zkml-noir
