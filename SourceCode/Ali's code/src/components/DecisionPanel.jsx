export default function DecisionPanel() {
  return (
    <aside style={styles.panel}>
      <h2>AI Recommendation</h2>

      <div style={styles.buy}>BUY</div>

      <p><strong>Confidence:</strong> 78%</p>
      <p><strong>Risk Level:</strong> Moderate</p>

      <p style={styles.text}>
        The model predicts a short-term upward trend based on historical
        price patterns and positive news sentiment.
      </p>
    </aside>
  );
}

const styles = {
  panel: {
    backgroundColor: "#020617",
    padding: "20px",
    borderLeft: "1px solid #1e293b",
  },
  buy: {
    textAlign: "center",
    padding: "15px",
    backgroundColor: "#14532d",
    color: "#22c55e",
    fontSize: "1.5rem",
    fontWeight: "bold",
    marginBottom: "15px",
  },
  text: {
    fontSize: "0.9rem",
    color: "#cbd5f5",
  },
};
