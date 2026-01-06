import {
  Chart as ChartJS,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement,
  Tooltip,
  Legend,
} from "chart.js";
import { Line } from "react-chartjs-2";

ChartJS.register(
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement,
  Tooltip,
  Legend
);

export default function ChartPanel({ market }) {
  const exampleData = {
    BTC: {
      historical: [42000, 42500, 43000, 42800, 43200],
      predicted: 44500,
    },
    ETH: {
      historical: [2200, 2250, 2300, 2280, 2350],
      predicted: 2450,
    },
    AAPL: {
      historical: [180, 182, 185, 183, 186],
      predicted: 190,
    },
    TSLA: {
      historical: [240, 245, 250, 248, 255],
      predicted: 265,
    },
  };

  const selected = exampleData[market];

  const data = {
    labels: ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Prediction"],
    datasets: [
      {
        label: "Historical Price",
        data: [...selected.historical, null],
        borderColor: "#38bdf8",
        tension: 0.4,
      },
      {
        label: "Predicted Price",
        data: [
          null,
          null,
          null,
          null,
          selected.historical[4],
          selected.predicted,
        ],
        borderColor: "#22c55e",
        borderDash: [5, 5],
        tension: 0.4,
      },
    ],
  };

  const options = {
    responsive: true,
    plugins: {
      legend: {
        labels: {
          color: "#e5e7eb",
        },
      },
    },
    scales: {
      x: {
        ticks: { color: "#94a3b8" },
        grid: { color: "#1e293b" },
      },
      y: {
        ticks: { color: "#94a3b8" },
        grid: { color: "#1e293b" },
      },
    },
  };

  return (
    <main style={styles.main}>
      <h2>{market} / USD</h2>

      <div style={styles.chartBox}>
        <Line data={data} options={options} />
      </div>

      <div style={styles.news}>
        <h3>News Sentiment</h3>
        <p style={{ color: "#22c55e" }}>Overall sentiment: Positive</p>
      </div>
    </main>
  );
}

const styles = {
  main: {
    padding: "20px",
  },
  chartBox: {
    backgroundColor: "#020617",
    padding: "20px",
    border: "1px solid #1e293b",
    marginBottom: "20px",
  },
  news: {
    backgroundColor: "#020617",
    padding: "15px",
    border: "1px solid #1e293b",
  },
};

  // keep the rest of your component (options, JSX, styles) the same

