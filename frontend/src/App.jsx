import { useState, useEffect } from "react"
import { createClient } from "@supabase/supabase-js"
import SignalFeed from "./components/SignalFeed"
import AccuracyTracker from "./components/AccuracyTracker"
import Header from "./components/Header"

const supabase = createClient(
  import.meta.env.VITE_SUPABASE_URL,
  import.meta.env.VITE_SUPABASE_KEY
)

export default function App() {
  const [signals, setSignals] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetchSignals()
    const subscription = supabase
      .channel("signals")
      .on("postgres_changes", { event: "INSERT", schema: "public", table: "signals" },
        payload => setSignals(prev => [payload.new, ...prev]))
      .subscribe()
    return () => supabase.removeChannel(subscription)
  }, [])

  async function fetchSignals() {
    const { data } = await supabase
      .from("signals")
      .select("*")
      .order("created_at", { ascending: false })
      .limit(50)
    setSignals(data || [])
    setLoading(false)
  }

  return (
    <div className="app">
      <Header />
      {loading ? <p>Loading signals...</p> : (
        <>
          <AccuracyTracker signals={signals} />
          <SignalFeed signals={signals} />
        </>
      )}
    </div>
  )
}
