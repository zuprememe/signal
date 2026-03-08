export default function AccuracyTracker({ signals }) {
  const resolved = signals.filter(s => s.resolved)
  const correct = resolved.filter(s => s.was_correct)
  const accuracy = resolved.length > 0
    ? Math.round((correct.length / resolved.length) * 100)
    : null

  return (
    <div className="accuracy-tracker">
      <h2>Prediction Accuracy</h2>
      {accuracy !== null ? (
        <div className="accuracy-score">
          <span className="big-number">{accuracy}%</span>
          <span className="sub-label">across {resolved.length} resolved signals</span>
        </div>
      ) : (
        <p>Accuracy builds over time as signals resolve. Check back in a week.</p>
      )}
    </div>
  )
}
