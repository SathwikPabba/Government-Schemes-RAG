import { useState } from "react";
import axios from "axios";

const API_URL = "https://government-schemes-rag.onrender.com";

const SAMPLE_QUESTIONS = [
  "Who is eligible for PM-KISAN?",
  "How to apply for Ayushman Bharat?",
  "Schemes for women entrepreneurs",
  "PM Awas Yojana benefits",
  "Scholarship for SC/ST students",
  "What is Kisan Credit Card?",
  "How to get MUDRA loan?",
  "Schemes for unemployed youth",
];

const CATEGORIES = ["All", "Agriculture", "Health", "Housing", "Finance", "Education", "Employment", "Insurance", "Entrepreneurship"];

const CATEGORY_COLORS = {
  "Agriculture": "#22c55e",
  "Health": "#ef4444",
  "Housing": "#f59e0b",
  "Finance": "#3b82f6",
  "Education": "#8b5cf6",
  "Employment": "#06b6d4",
  "Insurance": "#ec4899",
  "Entrepreneurship": "#f97316",
  "Pension": "#a78bfa",
  "Skill Development": "#10b981",
  "default": "#6366f1",
};

const CATEGORY_ICONS = {
  "Agriculture": "🌾", "Health": "🏥", "Housing": "🏠",
  "Finance": "💰", "Education": "📚", "Employment": "👷",
  "Insurance": "🛡️", "Entrepreneurship": "🚀", "Pension": "👴",
  "Skill Development": "🎓", "default": "🏛️"
};

function getCategoryColor(str) {
  for (const [key, color] of Object.entries(CATEGORY_COLORS)) {
    if (str && str.toLowerCase().includes(key.toLowerCase())) return color;
  }
  return CATEGORY_COLORS.default;
}

function getCategoryIcon(str) {
  for (const [key, icon] of Object.entries(CATEGORY_ICONS)) {
    if (str && str.toLowerCase().includes(key.toLowerCase())) return icon;
  }
  return CATEGORY_ICONS.default;
}

export default function App() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [activeTab, setActiveTab] = useState("ask");
  const [schemes, setSchemes] = useState([]);
  const [schemeSearch, setSchemeSearch] = useState("");
  const [selectedCategory, setSelectedCategory] = useState("All");
  const [history, setHistory] = useState([]);

  const askQuestion = async () => {
    if (!question.trim()) return;
    setLoading(true);
    setError(null);
    setAnswer(null);
    try {
      const res = await axios.post(`${API_URL}/query`, { question, max_sources: 3 });
      setAnswer(res.data);
      setHistory(prev => [{ question, answer: res.data }, ...prev.slice(0, 4)]);
    } catch {
      setError("Cannot connect to API. Make sure FastAPI is running on port 8000!");
    }
    setLoading(false);
  };

  const loadSchemes = async () => {
    try {
      const res = await axios.get(`${API_URL}/schemes`);
      setSchemes(res.data.schemes);
    } catch {
      setError("Cannot connect to API.");
    }
  };

  const handleTabChange = (tab) => {
    setActiveTab(tab);
    if (tab === "browse" && schemes.length === 0) loadSchemes();
  };

  const filteredSchemes = schemes.filter(s => {
    const matchSearch = s.toLowerCase().includes(schemeSearch.toLowerCase());
    const matchCat = selectedCategory === "All" || s.toLowerCase().includes(selectedCategory.toLowerCase());
    return matchSearch && matchCat;
  });

  return (
    <div style={S.app}>
      <style>{`
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
        @keyframes bounce { 0%,80%,100%{transform:translateY(0)} 40%{transform:translateY(-10px)} }
        @keyframes fadeIn { from{opacity:0;transform:translateY(12px)} to{opacity:1;transform:translateY(0)} }
        @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:0.5} }
        * { box-sizing:border-box; margin:0; padding:0; }
        body { background:#080b14; }
        textarea:focus, input:focus { outline: none; border-color: #4f46e5 !important; box-shadow: 0 0 0 3px rgba(79,70,229,0.15) !important; }
        button:hover { opacity: 0.85; }
        ::-webkit-scrollbar { width:5px; }
        ::-webkit-scrollbar-track { background:#0d1117; }
        ::-webkit-scrollbar-thumb { background:#2d3148; border-radius:3px; }
      `}</style>

      {/* HEADER */}
      <header style={S.header}>
        <div style={S.headerGlow} />
        <div style={S.headerInner}>
          <div style={S.headerLeft}>
            <div style={S.logo}>
              <span style={{fontSize:26}}>🇮🇳</span>
            </div>
            <div>
              <h1 style={S.title}>Government Scheme Assistant</h1>
              <p style={S.subtitle}>AI-powered guide to Indian Government Welfare Programs</p>
            </div>
          </div>
          <div style={S.headerRight}>
            <div style={S.statusDot} />
            <span style={S.statusText}>Live</span>
            <div style={S.divider} />
            <span style={S.badge}>⚡ Groq LLaMA 3.1</span>
          </div>
        </div>
      </header>

      {/* HERO */}
      <div style={S.hero}>
        <div style={S.heroGlow1} />
        <div style={S.heroGlow2} />
        <div style={S.heroInner}>
          <div style={S.heroTag}>🏛️ 15 Government Schemes Indexed</div>
          <h2 style={S.heroTitle}>Find the Right Government<br />Scheme for You</h2>
          <p style={S.heroDesc}>Ask in plain English. Get instant, accurate answers about eligibility, benefits, and how to apply.</p>
        </div>
      </div>

      {/* MAIN CONTENT */}
      <div style={S.container}>
        <div style={S.grid}>
          {/* SIDEBAR */}
          <aside style={S.sidebar}>
            <div style={S.sideCard}>
              <p style={S.sideCardTitle}>Quick Questions</p>
              <div style={S.sideList}>
                {SAMPLE_QUESTIONS.map(q => (
                  <button key={q} style={S.sideItem} onClick={() => { setQuestion(q); setActiveTab("ask"); }}>
                    <span style={S.sideItemDot} />
                    <span style={S.sideItemText}>{q}</span>
                  </button>
                ))}
              </div>
            </div>

            {history.length > 0 && (
              <div style={S.sideCard}>
                <p style={S.sideCardTitle}>Recent Searches</p>
                <div style={S.sideList}>
                  {history.map((h, i) => (
                    <button key={i} style={S.sideItem} onClick={() => { setQuestion(h.question); setAnswer(h.answer); setActiveTab("ask"); }}>
                      <span style={{...S.sideItemDot, background:"#f59e0b"}} />
                      <span style={{...S.sideItemText, maxWidth:170, overflow:"hidden", textOverflow:"ellipsis", whiteSpace:"nowrap"}}>{h.question}</span>
                    </button>
                  ))}
                </div>
              </div>
            )}
          </aside>

          {/* MAIN PANEL */}
          <div style={S.panel}>
            {/* TABS */}
            <div style={S.tabBar}>
              {[["ask","💬","Ask a Question"], ["browse","📋","Browse Schemes"]].map(([id, icon, label]) => (
                <button key={id} style={activeTab===id ? {...S.tabBtn, ...S.tabBtnActive} : S.tabBtn} onClick={() => handleTabChange(id)}>
                  <span>{icon}</span> {label}
                  {activeTab===id && <div style={S.tabIndicator} />}
                </button>
              ))}
            </div>

            {activeTab === "ask" && (
              <div style={{animation:"fadeIn 0.3s ease"}}>
                {/* INPUT AREA */}
                <div style={S.inputCard}>
                  <div style={S.inputTop}>
                    <span style={S.inputLabel}>Ask your question</span>
                    <span style={S.inputHint}>Ctrl+Enter to submit</span>
                  </div>
                  <textarea
                    style={S.textarea}
                    value={question}
                    onChange={e => setQuestion(e.target.value)}
                    placeholder="e.g. What schemes are available for farmers in India?"
                    rows={4}
                    onKeyDown={e => e.key==="Enter" && e.ctrlKey && askQuestion()}
                  />
                  <div style={S.inputBottom}>
                    <div style={S.chips}>
                      {SAMPLE_QUESTIONS.slice(0,4).map(q => (
                        <button key={q} style={S.chip} onClick={() => setQuestion(q)}>{q}</button>
                      ))}
                    </div>
                    <button style={loading ? {...S.askBtn, opacity:0.6} : S.askBtn} onClick={askQuestion} disabled={loading}>
                      {loading ? "Searching..." : "Ask →"}
                    </button>
                  </div>
                </div>

                {/* ERROR */}
                {error && (
                  <div style={S.errorCard}>
                    <span style={{fontSize:20}}>⚠️</span>
                    <div>
                      <p style={S.errorTitle}>Connection Error</p>
                      <p style={S.errorMsg}>{error}</p>
                    </div>
                  </div>
                )}

                {/* LOADING */}
                {loading && (
                  <div style={S.loadingCard}>
                    <div style={S.dots}>
                      {[0,0.15,0.3].map((d,i) => (
                        <div key={i} style={{...S.dot, animationDelay:`${d}s`}} />
                      ))}
                    </div>
                    <p style={S.loadingMsg}>Searching through government scheme database...</p>
                  </div>
                )}

                {/* ANSWER */}
                {answer && !loading && (
                  <div style={{animation:"fadeIn 0.4s ease", display:"flex", flexDirection:"column", gap:20}}>
                    {/* ANSWER BOX */}
                    <div style={S.answerCard}>
                      <div style={S.answerCardHeader}>
                        <div style={S.answerIconBox}>✦</div>
                        <span style={S.answerCardTitle}>AI Answer</span>
                        <div style={S.answerMeta}>{answer.num_sources} sources</div>
                      </div>
                      <div style={S.answerBody}>
                        {answer.answer.split("\n").map((line, i) => line.trim() && (
                          <p key={i} style={S.answerLine}>{line}</p>
                        ))}
                      </div>
                    </div>

                    {/* SOURCE CARDS */}
                    {answer.sources?.length > 0 && (
                      <div>
                        <p style={S.sourcesTitle}>📚 Referenced Schemes</p>
                        <div style={S.sourcesGrid}>
                          {answer.sources.map((src, i) => {
                            const color = getCategoryColor(src.category);
                            const icon = getCategoryIcon(src.category);
                            return (
                              <div key={i} style={{...S.sourceCard, borderTop:`3px solid ${color}`}}>
                                <div style={S.sourceHead}>
                                  <div style={{...S.sourceIconBox, background:`${color}22`}}>
                                    <span style={{fontSize:22}}>{icon}</span>
                                  </div>
                                  <div style={{flex:1}}>
                                    <p style={S.sourceName}>{src.scheme_name.replace(/-/g," ")}</p>
                                    <p style={S.sourceMinistry}>{src.ministry !== "N/A" ? src.ministry : "Government of India"}</p>
                                  </div>
                                </div>
                                <p style={S.sourcePreview}>{src.preview.slice(0,130)}...</p>
                                <div style={{...S.sourceCat, color, borderColor:`${color}44`, background:`${color}11`}}>
                                  {src.category !== "N/A" ? src.category : "General"}
                                </div>
                              </div>
                            );
                          })}
                        </div>
                      </div>
                    )}

                    {/* FEEDBACK */}
                    <div style={S.feedbackBar}>
                      <span style={S.feedbackText}>Was this answer helpful?</span>
                      <button style={S.fbBtnYes}>👍 Yes, helpful</button>
                      <button style={S.fbBtnNo}>👎 Not helpful</button>
                    </div>
                  </div>
                )}
              </div>
            )}

            {activeTab === "browse" && (
              <div style={{animation:"fadeIn 0.3s ease"}}>
                <div style={S.browseHeader}>
                  <input style={S.searchBox} placeholder="Search schemes by name..." value={schemeSearch} onChange={e => setSchemeSearch(e.target.value)} />
                </div>
                <div style={S.catFilters}>
                  {CATEGORIES.map(cat => (
                    <button key={cat} style={selectedCategory===cat ? {...S.catBtn, ...S.catBtnOn} : S.catBtn} onClick={() => setSelectedCategory(cat)}>
                      {cat}
                    </button>
                  ))}
                </div>
                <p style={S.schemeCount}>{filteredSchemes.length} schemes found</p>
                <div style={S.schemeGrid}>
                  {filteredSchemes.map((s, i) => {
                    const color = getCategoryColor(s);
                    const icon = getCategoryIcon(s);
                    return (
                      <div key={i} style={{...S.schemeCard, borderLeft:`3px solid ${color}`}}
                        onClick={() => { setQuestion(`Tell me about ${s.replace(/-/g," ")}`); setActiveTab("ask"); }}>
                        <span style={{fontSize:22}}>{icon}</span>
                        <span style={S.schemeCardName}>{s.replace(/-/g," ")}</span>
                        <span style={{color:"#3d4168", fontSize:18}}>›</span>
                      </div>
                    );
                  })}
                </div>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}

const S = {
  app: { minHeight:"100vh", background:"#080b14", color:"#e2e8f0", fontFamily:"'Inter','Segoe UI',sans-serif" },
  header: { position:"relative", background:"#0d1117", borderBottom:"1px solid #1e2433", padding:"14px 0", overflow:"hidden" },
  headerGlow: { position:"absolute", top:-60, left:"50%", transform:"translateX(-50%)", width:600, height:120, background:"radial-gradient(ellipse,rgba(79,70,229,0.15) 0%,transparent 70%)", pointerEvents:"none" },
  headerInner: { maxWidth:1200, margin:"0 auto", padding:"0 32px", display:"flex", justifyContent:"space-between", alignItems:"center", position:"relative" },
  headerLeft: { display:"flex", alignItems:"center", gap:16 },
  logo: { width:48, height:48, background:"linear-gradient(135deg,#1e2235,#252a3d)", borderRadius:12, display:"flex", alignItems:"center", justifyContent:"center", border:"1px solid #2d3148" },
  title: { fontSize:20, fontWeight:700, color:"#f1f5f9", letterSpacing:"-0.4px" },
  subtitle: { fontSize:12, color:"#475569", marginTop:2 },
  headerRight: { display:"flex", alignItems:"center", gap:12 },
  statusDot: { width:8, height:8, borderRadius:"50%", background:"#22c55e", boxShadow:"0 0 8px #22c55e" },
  statusText: { fontSize:13, color:"#22c55e", fontWeight:500 },
  divider: { width:1, height:20, background:"#2d3148" },
  badge: { background:"#1e2235", border:"1px solid #3d4168", color:"#818cf8", padding:"6px 14px", borderRadius:20, fontSize:13, fontWeight:500 },
  hero: { position:"relative", background:"#0d1117", borderBottom:"1px solid #1e2433", padding:"48px 32px", overflow:"hidden", textAlign:"center" },
  heroGlow1: { position:"absolute", top:-80, left:"30%", width:400, height:300, background:"radial-gradient(ellipse,rgba(79,70,229,0.12) 0%,transparent 70%)", pointerEvents:"none" },
  heroGlow2: { position:"absolute", top:-80, right:"30%", width:400, height:300, background:"radial-gradient(ellipse,rgba(99,102,241,0.08) 0%,transparent 70%)", pointerEvents:"none" },
  heroInner: { position:"relative", maxWidth:700, margin:"0 auto" },
  heroTag: { display:"inline-block", background:"#1e2235", border:"1px solid #3d4168", color:"#818cf8", padding:"6px 16px", borderRadius:20, fontSize:13, marginBottom:20 },
  heroTitle: { fontSize:36, fontWeight:700, color:"#f1f5f9", lineHeight:1.25, letterSpacing:"-0.8px", marginBottom:16 },
  heroDesc: { fontSize:16, color:"#64748b", lineHeight:1.7 },
  container: { maxWidth:1200, margin:"0 auto", padding:"32px" },
  grid: { display:"grid", gridTemplateColumns:"260px 1fr", gap:24 },
  sidebar: { display:"flex", flexDirection:"column", gap:16 },
  sideCard: { background:"#0d1117", border:"1px solid #1e2433", borderRadius:16, padding:20 },
  sideCardTitle: { fontSize:12, fontWeight:600, color:"#475569", letterSpacing:"0.6px", textTransform:"uppercase", marginBottom:14 },
  sideList: { display:"flex", flexDirection:"column", gap:2 },
  sideItem: { background:"transparent", border:"none", color:"#94a3b8", padding:"8px 10px", borderRadius:8, cursor:"pointer", fontSize:13, textAlign:"left", display:"flex", alignItems:"center", gap:10 },
  sideItemDot: { width:6, height:6, borderRadius:"50%", background:"#4f46e5", flexShrink:0 },
  sideItemText: { lineHeight:1.4 },
  panel: { display:"flex", flexDirection:"column", gap:20 },
  tabBar: { display:"flex", gap:4, background:"#0d1117", border:"1px solid #1e2433", borderRadius:14, padding:6 },
  tabBtn: { flex:1, padding:"10px 20px", borderRadius:10, border:"none", background:"transparent", cursor:"pointer", fontSize:14, color:"#64748b", fontWeight:500, position:"relative", display:"flex", alignItems:"center", justifyContent:"center", gap:8 },
  tabBtnActive: { background:"#161d2e", color:"#e2e8f0" },
  tabIndicator: { position:"absolute", bottom:6, left:"50%", transform:"translateX(-50%)", width:24, height:3, background:"#4f46e5", borderRadius:2 },
  inputCard: { background:"#0d1117", border:"1px solid #1e2433", borderRadius:16, padding:24 },
  inputTop: { display:"flex", justifyContent:"space-between", alignItems:"center", marginBottom:12 },
  inputLabel: { fontSize:15, fontWeight:600, color:"#cbd5e1" },
  inputHint: { fontSize:12, color:"#475569" },
  textarea: { width:"100%", background:"#080b14", border:"1px solid #1e2433", borderRadius:12, color:"#e2e8f0", padding:"14px 16px", fontSize:15, resize:"vertical", fontFamily:"inherit", lineHeight:1.7, transition:"all 0.2s" },
  inputBottom: { display:"flex", justifyContent:"space-between", alignItems:"center", marginTop:16, flexWrap:"wrap", gap:12 },
  chips: { display:"flex", flexWrap:"wrap", gap:8 },
  chip: { padding:"5px 14px", borderRadius:20, border:"1px solid #1e2433", background:"#161d2e", color:"#94a3b8", cursor:"pointer", fontSize:12, transition:"all 0.15s" },
  askBtn: { padding:"12px 28px", background:"linear-gradient(135deg,#4f46e5,#6366f1)", color:"white", border:"none", borderRadius:12, fontSize:15, cursor:"pointer", fontWeight:600, letterSpacing:"-0.2px", whiteSpace:"nowrap" },
  errorCard: { background:"#1a0f0f", border:"1px solid #7f1d1d", borderRadius:14, padding:20, display:"flex", gap:14, alignItems:"flex-start" },
  errorTitle: { fontSize:15, fontWeight:600, color:"#fca5a5", marginBottom:4 },
  errorMsg: { fontSize:13, color:"#f87171" },
  loadingCard: { background:"#0d1117", border:"1px solid #1e2433", borderRadius:16, padding:40, display:"flex", flexDirection:"column", alignItems:"center", gap:16 },
  dots: { display:"flex", gap:10 },
  dot: { width:12, height:12, borderRadius:"50%", background:"#4f46e5", animation:"bounce 1.2s infinite" },
  loadingMsg: { color:"#475569", fontSize:14 },
  answerCard: { background:"#0d1117", border:"1px solid #1e2433", borderRadius:16, overflow:"hidden" },
  answerCardHeader: { background:"#161d2e", padding:"16px 24px", display:"flex", alignItems:"center", gap:12, borderBottom:"1px solid #1e2433" },
  answerIconBox: { width:32, height:32, background:"linear-gradient(135deg,#4f46e5,#818cf8)", borderRadius:8, display:"flex", alignItems:"center", justifyContent:"center", color:"white", fontSize:16, fontWeight:700 },
  answerCardTitle: { fontSize:15, fontWeight:600, color:"#e2e8f0", flex:1 },
  answerMeta: { fontSize:12, color:"#475569", background:"#0d1117", padding:"4px 12px", borderRadius:20, border:"1px solid #1e2433" },
  answerBody: { padding:24, display:"flex", flexDirection:"column", gap:10 },
  answerLine: { color:"#cbd5e1", fontSize:15, lineHeight:1.8 },
  sourcesTitle: { fontSize:14, fontWeight:600, color:"#475569", marginBottom:14 },
  sourcesGrid: { display:"grid", gridTemplateColumns:"repeat(auto-fill,minmax(260px,1fr))", gap:14 },
  sourceCard: { background:"#0d1117", border:"1px solid #1e2433", borderRadius:14, padding:18, display:"flex", flexDirection:"column", gap:12, transition:"border-color 0.2s" },
  sourceHead: { display:"flex", gap:12, alignItems:"flex-start" },
  sourceIconBox: { width:44, height:44, borderRadius:12, display:"flex", alignItems:"center", justifyContent:"center", flexShrink:0 },
  sourceName: { fontSize:14, fontWeight:600, color:"#e2e8f0", lineHeight:1.4 },
  sourceMinistry: { fontSize:11, color:"#475569", marginTop:3 },
  sourcePreview: { fontSize:12, color:"#64748b", lineHeight:1.65 },
  sourceCat: { display:"inline-block", padding:"3px 12px", borderRadius:20, fontSize:11, fontWeight:500, border:"1px solid", alignSelf:"flex-start" },
  feedbackBar: { background:"#0d1117", border:"1px solid #1e2433", borderRadius:14, padding:"16px 20px", display:"flex", alignItems:"center", gap:12 },
  feedbackText: { fontSize:14, color:"#475569", flex:1 },
  fbBtnYes: { padding:"7px 18px", borderRadius:20, border:"1px solid #166534", background:"#052e16", color:"#4ade80", cursor:"pointer", fontSize:13, fontWeight:500 },
  fbBtnNo: { padding:"7px 18px", borderRadius:20, border:"1px solid #7f1d1d", background:"#1a0f0f", color:"#f87171", cursor:"pointer", fontSize:13, fontWeight:500 },
  browseHeader: { marginBottom:16 },
  searchBox: { width:"100%", background:"#0d1117", border:"1px solid #1e2433", borderRadius:12, color:"#e2e8f0", padding:"12px 18px", fontSize:14, fontFamily:"inherit", transition:"all 0.2s" },
  catFilters: { display:"flex", flexWrap:"wrap", gap:8, marginBottom:20 },
  catBtn: { padding:"6px 16px", borderRadius:20, border:"1px solid #1e2433", background:"transparent", color:"#64748b", cursor:"pointer", fontSize:13, fontWeight:500 },
  catBtnOn: { background:"#1e2235", color:"#818cf8", border:"1px solid #3d4168" },
  schemeCount: { fontSize:13, color:"#475569", marginBottom:14 },
  schemeGrid: { display:"grid", gridTemplateColumns:"repeat(auto-fill,minmax(220px,1fr))", gap:10 },
  schemeCard: { background:"#0d1117", border:"1px solid #1e2433", borderRadius:12, padding:"14px 18px", display:"flex", alignItems:"center", gap:12, cursor:"pointer", transition:"all 0.15s" },
  schemeCardName: { flex:1, fontSize:13, color:"#94a3b8", lineHeight:1.4 },
};
