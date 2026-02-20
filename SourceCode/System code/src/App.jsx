import { useState } from "react";
import Header from "./components/header";
import Sidebar from "./components/Sidebar";
import ChartPanel from "./components/ChartPanel";
import DecisionPanel from "./components/DecisionPanel";
import marketData from "./marketData.json"; // Your AI Data

export default function App() {
  // Set default to AAPL since BTC/ETH aren't in your ML script
  const [market, setMarket] = useState("AAPL");

  // Fetch the specific data for the chosen ticker
  const selectedData = marketData[market];

  return (
    <>
      <Header />
      <div className="container">
        <Sidebar market={market} setMarket={setMarket} />
        {/* Pass selectedData as a prop to both panels */}
        <ChartPanel market={market} data={selectedData} />
        <DecisionPanel market={market} data={selectedData} />
      </div>
    </>
  );
}