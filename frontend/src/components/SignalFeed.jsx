const DIRECTION_COLOR = {
  bullish_overcorrection: "#22c55e",
  bearish_overcorrection: "#ef4444",
  proportionate: "#94a3b8"
}

export default function SignalFeed({ signals }) {
  return (
    <div className="signal-feed">
      <h2>Live Signals</h2>
      {signals.map(signal => (
        <div key={signal.id} className="signal-card" style={{
          borderLeft: `4px solid ${DIRECTION_COLOR[signal.direction] || "#94a3b8"}`
        }}>
          <div className="signal-source">{signal.source}</div>
          <div className="signal-headline">{signal.headline}</div>
          <div className="signal-meta">
            <span>Disproportion: {Math.round(signal.disproportion_score * 100)}%</span>
            <span>Confidence: {Math.round(signal.confidence * 100)}%</span>
            <span>~{signal.timeframe_days}d to revert</span>
          </div>
          <div className="signal-reasoning">{signal.reasoning}</div>
        </div>
      ))}
    </div>
  )
}
