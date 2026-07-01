import { useState } from "react";

const API = "http://localhost:8000";

const INTENSITIES = ["Gentle", "Mild", "Savage", "Brutal"];

function StatBox({ val, label }) {
  return (
    <div style={{
      background: "#0e1318", border: "1px solid #1e2530",
      borderRadius: 10, padding: "14px 12px", textAlign: "center"
    }}>
      <div style={{ fontFamily: "'Bebas Neue', sans-serif", fontSize: 28, color: "#fff", letterSpacing: 1, marginBottom: 4 }}>{val}</div>
      <div style={{ fontFamily: "'JetBrains Mono', monospace", fontSize: 10, color: "#4b5563", textTransform: "uppercase", letterSpacing: 1.5 }}>{label}</div>
    </div>
  );
}

function ProfileCard({ data, username }) {
  const initials = (data.name || username).slice(0, 2).toUpperCase();
  return (
    <div style={{ background: "#0e1318", border: "1px solid #1e2530", borderRadius: 16, padding: 24, marginBottom: 16, display: "flex", alignItems: "center", gap: 20 }}>
      <div style={{
        width: 64, height: 64, borderRadius: "50%", border: "2px solid #ff4f1e44",
        background: "#140a07", display: "flex", alignItems: "center", justifyContent: "center",
        fontFamily: "'Bebas Neue', sans-serif", fontSize: 24, color: "#ff4f1e", flexShrink: 0, letterSpacing: 2
      }}>{initials}</div>
      <div>
        <div style={{ fontFamily: "'Outfit', sans-serif", fontSize: 20, fontWeight: 800, color: "#fff", marginBottom: 2 }}>{data.name}</div>
        <div style={{ fontFamily: "'JetBrains Mono', monospace", fontSize: 12, color: "#ff4f1e", marginBottom: 6 }}>@{username}</div>
        <div style={{ fontSize: 13, color: "#6b7280" }}>{data.bio}</div>
      </div>
    </div>
  );
}

function RoastOutput({ username, roast }) {
  return (
    <div style={{ background: "#0e1318", border: "1px solid #ff4f1e44", borderRadius: 16, padding: 28, position: "relative", overflow: "hidden" }}>
      <div style={{ position: "absolute", top: 0, left: 0, right: 0, height: 2, background: "linear-gradient(90deg, transparent, #ff4f1e, transparent)" }} />
      <div style={{ fontFamily: "'JetBrains Mono', monospace", fontSize: 11, letterSpacing: 3, color: "#ff4f1e", textTransform: "uppercase", marginBottom: 16, display: "flex", alignItems: "center", gap: 8 }}>
        roast — @{username}
        <span style={{ flex: 1, height: 1, background: "#1e2530", display: "block" }} />
      </div>
      <div style={{ fontFamily: "'Outfit', sans-serif", fontSize: 15, lineHeight: 1.9, color: "#9ca3af", whiteSpace: "pre-wrap" }}>{roast}</div>
    </div>
  );
}

export default function App() {
  const [mode, setMode] = useState("single");
  const [intensity, setIntensity] = useState("Savage");
  const [username, setUsername] = useState("");
  const [username1, setUsername1] = useState("");
  const [username2, setUsername2] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [result, setResult] = useState(null);

  async function handleRoast() {
    if (!username.trim()) return;
    setLoading(true); setError(""); setResult(null);
    try {
      const res = await fetch(`${API}/roast`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username: username.trim(), intensity }),
      });
      const json = await res.json();
      if (json.error) { setError(json.error); }
      else { setResult({ type: "single", ...json }); }
    } catch {
      setError("Cannot connect to backend. Is it running?");
    }
    setLoading(false);
  }

  async function handleCompare() {
    if (!username1.trim() || !username2.trim()) return;
    setLoading(true); setError(""); setResult(null);
    try {
      const res = await fetch(`${API}/compare`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username1: username1.trim(), username2: username2.trim(), intensity }),
      });
      const json = await res.json();
      if (json.error) { setError(json.error); }
      else { setResult({ type: "compare", ...json }); }
    } catch {
      setError("Cannot connect to backend. Is it running?");
    }
    setLoading(false);
  }

  const gridBg = {
    position: "fixed", inset: 0, pointerEvents: "none",
    backgroundImage: "linear-gradient(rgba(255,80,30,0.04) 1px, transparent 1px), linear-gradient(90deg, rgba(255,80,30,0.04) 1px, transparent 1px)",
    backgroundSize: "40px 40px"
  };

  const inputStyle = {
    flex: 1, background: "transparent", border: "none", outline: "none",
    color: "#e8eaf0", fontFamily: "'JetBrains Mono', monospace", fontSize: 13, padding: "9px 0"
  };

  return (
    <div style={{ background: "#080b0f", minHeight: "100vh", color: "#e8eaf0", fontFamily: "'Outfit', sans-serif" }}>
      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=JetBrains+Mono:wght@400;700&family=Outfit:wght@400;600;800&display=swap');
        * { box-sizing: border-box; margin: 0; padding: 0; }
        ::placeholder { color: #2d3748; }
        input { caret-color: #ff4f1e; }
      `}</style>

      <div style={gridBg} />

      <div style={{ position: "relative", maxWidth: 760, margin: "0 auto", padding: "60px 24px 80px" }}>

        {/* Header */}
        <div style={{ textAlign: "center", marginBottom: 56 }}>
          <div style={{ fontFamily: "'JetBrains Mono', monospace", fontSize: 11, letterSpacing: 4, color: "#ff4f1e", textTransform: "uppercase", marginBottom: 16, opacity: 0.8 }}>
            // ai-powered destruction
          </div>
          <div style={{ fontFamily: "'Bebas Neue', sans-serif", fontSize: "clamp(72px, 14vw, 120px)", lineHeight: 0.9, letterSpacing: 3, color: "#fff" }}>
            GITHUB<br /><span style={{ color: "#ff4f1e" }}>ROASTER</span>
          </div>
          <div style={{ marginTop: 18, fontFamily: "'JetBrains Mono', monospace", fontSize: 13, color: "#4b5563" }}>
            $ enter username — we handle the rest
          </div>
        </div>

        {/* Mode toggle */}
        <div style={{ display: "flex", gap: 10, marginBottom: 32 }}>
          {[["single", "Single Roast"], ["compare", "Compare Devs"]].map(([val, label]) => (
            <button key={val} onClick={() => { setMode(val); setResult(null); setError(""); }}
              style={{
                flex: 1, padding: "13px 16px", background: mode === val ? "#140a07" : "#0e1318",
                border: `1px solid ${mode === val ? "#ff4f1e" : "#1e2530"}`,
                borderRadius: 10, color: mode === val ? "#fff" : "#4b5563",
                fontFamily: "'Outfit', sans-serif", fontSize: 14, fontWeight: 600,
                cursor: "pointer", display: "flex", alignItems: "center", justifyContent: "center", gap: 8, transition: "all 0.2s"
              }}>
              <span style={{ width: 7, height: 7, borderRadius: "50%", background: mode === val ? "#ff4f1e" : "#1e2530", display: "inline-block", transition: "all 0.2s" }} />
              {label}
            </button>
          ))}
        </div>

        {/* Intensity */}
        <div style={{ marginBottom: 28 }}>
          <div style={{ fontFamily: "'JetBrains Mono', monospace", fontSize: 11, letterSpacing: 3, color: "#4b5563", textTransform: "uppercase", marginBottom: 10 }}>// intensity</div>
          <div style={{ display: "flex", background: "#0e1318", border: "1px solid #1e2530", borderRadius: 10, padding: 5, gap: 4 }}>
            {INTENSITIES.map(i => (
              <button key={i} onClick={() => setIntensity(i)}
                style={{
                  flex: 1, padding: "9px 8px", background: intensity === i ? "#ff4f1e" : "transparent",
                  border: "none", borderRadius: 7, color: intensity === i ? "#fff" : "#4b5563",
                  fontFamily: "'JetBrains Mono', monospace", fontSize: 11, cursor: "pointer",
                  fontWeight: 700, letterSpacing: 0.5, transition: "all 0.18s"
                }}>{i}</button>
            ))}
          </div>
        </div>

        {/* Search */}
        {mode === "single" ? (
          <div style={{ display: "flex", gap: 10, marginBottom: 32, alignItems: "center" }}>
            <div style={{ flex: 1, display: "flex", alignItems: "center", background: "#0e1318", border: "1px solid #1e2530", borderRadius: 12, padding: "6px 6px 6px 18px", gap: 10 }}>
              <span style={{ color: "#4b5563", fontFamily: "'JetBrains Mono', monospace", fontSize: 13, flexShrink: 0 }}>$_</span>
              <input style={inputStyle} placeholder="enter github username..."
                value={username} onChange={e => setUsername(e.target.value)}
                onKeyDown={e => e.key === "Enter" && handleRoast()} />
            </div>
            <button onClick={handleRoast} disabled={loading}
              style={{ padding: "0 22px", height: 46, background: loading ? "#7a2a10" : "#ff4f1e", border: "none", borderRadius: 12, color: "#fff", fontFamily: "'Bebas Neue', sans-serif", fontSize: 18, letterSpacing: 2, cursor: loading ? "not-allowed" : "pointer", whiteSpace: "nowrap", transition: "all 0.15s" }}>
              {loading ? "Roasting..." : "Roast →"}
            </button>
          </div>
        ) : (
          <div style={{ marginBottom: 32 }}>
            <div style={{ display: "flex", gap: 10, marginBottom: 10 }}>
              {[[username1, setUsername1, "first developer..."], [username2, setUsername2, "second developer..."]].map(([val, setter, ph], i) => (
                <div key={i} style={{ flex: 1, display: "flex", alignItems: "center", background: "#0e1318", border: "1px solid #1e2530", borderRadius: 12, padding: "6px 6px 6px 18px", gap: 10 }}>
                  <span style={{ color: "#4b5563", fontFamily: "'JetBrains Mono', monospace", fontSize: 13 }}>$_</span>
                  <input style={inputStyle} placeholder={ph} value={val} onChange={e => setter(e.target.value)} />
                </div>
              ))}
            </div>
            <button onClick={handleCompare} disabled={loading}
              style={{ width: "100%", padding: "0 22px", height: 46, background: loading ? "#7a2a10" : "#ff4f1e", border: "none", borderRadius: 12, color: "#fff", fontFamily: "'Bebas Neue', sans-serif", fontSize: 18, letterSpacing: 2, cursor: loading ? "not-allowed" : "pointer", transition: "all 0.15s" }}>
              {loading ? "Roasting Both..." : "Compare & Roast →"}
            </button>
          </div>
        )}

        {error && (
          <div style={{ background: "#1a0808", border: "1px solid #7a2a10", borderRadius: 10, padding: "12px 18px", marginBottom: 16, fontFamily: "'JetBrains Mono', monospace", fontSize: 13, color: "#f87171" }}>
            ✗ {error}
          </div>
        )}

        {/* Results - Single */}
        {result?.type === "single" && (
          <>
            <hr style={{ border: "none", borderTop: "1px solid #1e2530", margin: "0 0 24px" }} />
            <ProfileCard data={result.data} username={username} />
            <div style={{ display: "grid", gridTemplateColumns: "repeat(4, minmax(0, 1fr))", gap: 10, marginBottom: 16 }}>
              <StatBox val={result.data.total_repos} label="Repos" />
              <StatBox val={result.data.followers} label="Followers" />
              <StatBox val={result.data.total_stars} label="Stars" />
              <StatBox val={result.data.empty_repos} label="Empty" />
            </div>
            {result.data.languages.length > 0 && (
              <div style={{ display: "flex", flexWrap: "wrap", gap: 6, marginBottom: 16 }}>
                {result.data.languages.map(l => (
                  <span key={l} style={{ padding: "4px 14px", background: "#0e1318", border: "1px solid #1e2530", borderRadius: 20, fontFamily: "'JetBrains Mono', monospace", fontSize: 11, color: "#6b7280" }}>{l}</span>
                ))}
              </div>
            )}
            <RoastOutput username={username} roast={result.roast} />
          </>
        )}

        {/* Results - Compare */}
        {result?.type === "compare" && (
          <>
            <hr style={{ border: "none", borderTop: "1px solid #1e2530", margin: "0 0 24px" }} />
            <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 12, marginBottom: 16 }}>
              {[[result.data1, username1, result.score1], [result.data2, username2, result.score2]].map(([data, uname, score], i) => (
                <div key={i} style={{ background: "#0e1318", border: `1px solid ${result.winner === uname ? "#ff4f1e" : "#1e2530"}`, borderRadius: 16, padding: 20 }}>
                  <div style={{ fontFamily: "'Outfit', sans-serif", fontWeight: 800, fontSize: 16, color: "#fff", marginBottom: 2 }}>{data.name}</div>
                  <div style={{ fontFamily: "'JetBrains Mono', monospace", fontSize: 11, color: "#ff4f1e", marginBottom: 12 }}>@{uname}</div>
                  <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 8 }}>
                    <StatBox val={data.total_repos} label="Repos" />
                    <StatBox val={data.followers} label="Followers" />
                    <StatBox val={data.total_stars} label="Stars" />
                    <StatBox val={score} label="Score" />
                  </div>
                </div>
              ))}
            </div>
            <div style={{ background: "#140a07", border: "1px solid #ff4f1e44", borderRadius: 12, padding: "16px 20px", textAlign: "center", marginBottom: 16 }}>
              <div style={{ fontFamily: "'JetBrains Mono', monospace", fontSize: 10, color: "#ff4f1e", letterSpacing: 3, textTransform: "uppercase", marginBottom: 6 }}>winner</div>
              <div style={{ fontFamily: "'Bebas Neue', sans-serif", fontSize: 28, color: "#fff", letterSpacing: 2 }}>🏆 {result.winner}</div>
            </div>
            <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 12 }}>
              <RoastOutput username={username1} roast={result.roast1} />
              <RoastOutput username={username2} roast={result.roast2} />
            </div>
          </>
        )}

        <div style={{ textAlign: "center", marginTop: 20, fontFamily: "'JetBrains Mono', monospace", fontSize: 10, color: "#2d3748", letterSpacing: 1 }}>
          // all in good fun · no developers were harmed · probably
        </div>
      </div>
    </div>
  );
}