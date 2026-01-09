index.html
<div style="background: #1a1a1a; color: #f3ba2f; padding: 10px; font-family: Arial, sans-serif; overflow: hidden; white-space: nowrap; border-bottom: 2px solid #333;">
    <marquee behavior="scroll" direction="left" scrollamount="5">
        <strong>LIVE MARKET:</strong> 
        <span id="btc-price">BITCOIN (BTC): Loading...</span> | 
        <span id="sol-price" style="margin-left: 20px;">SOLANA (SOL): Loading...</span> | 
        <span style="margin-left: 20px; color: #00ff00;">SDN News DAO: Active 🌐</span>
    </marquee>
</div>

<script>
    async function getPrices() {
        try {
            const response = await fetch('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,solana&vs_currencies=usd');
            const data = await response.json();
            document.getElementById('btc-price').innerHTML = `BITCOIN (BTC): $${data.bitcoin.usd.toLocaleString()}`;
            document.getElementById('sol-price').innerHTML = `SOLANA (SOL): $${data.solana.usd.toLocaleString()}`;
        } catch (error) {
            console.log("Error fetching prices");
        }
    }
    getPrices();
    setInterval(getPrices, 30000); // ہر 30 سیکنڈ بعد قیمت اپ ڈیٹ ہوگی
</script>




