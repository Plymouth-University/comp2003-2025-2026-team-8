import { useState } from "react";
import Header from "./components/header";
import Sidebar from "./components/Sidebar";
import ChartPanel from "./components/ChartPanel";
import DecisionPanel from "./components/DecisionPanel";

export default function App() {
  const [market, setMarket] = useState("BTC");

  return (
    <>
      <Header />
      <div className="container">
        <Sidebar market={market} setMarket={setMarket} />
        <ChartPanel market={market} />
        <DecisionPanel market={market} />
      </div>
    </>
  );
}