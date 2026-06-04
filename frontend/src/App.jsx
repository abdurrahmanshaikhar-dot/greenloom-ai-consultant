import { useState } from "react";

function App() {
  const [company, setCompany] = useState("");
  const [problem, setProblem] = useState("");
  const [report, setReport] = useState("");
  const [loading, setLoading] = useState(false);

  const handleAnalyze = async () => {
    setLoading(true);

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/analyze",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            company,
            problem
          })
        }
      );

      const data = await response.json();

      setReport(data.report);
    } catch (error) {
      console.error(error);
      setReport("Error connecting to backend.");
    }

    setLoading(false);
  };

  return (
    <div
      style={{
        padding: "40px",
        maxWidth: "900px",
        margin: "auto"
      }}
    >
      <h1>AI Business Consultant</h1>

      <p>
        Enter a company and business problem.
      </p>

      <input
        type="text"
        placeholder="Company Name"
        value={company}
        onChange={(e) => setCompany(e.target.value)}
        style={{
          width: "100%",
          padding: "10px",
          marginBottom: "15px"
        }}
      />

      <textarea
        placeholder="Describe the business problem"
        value={problem}
        onChange={(e) => setProblem(e.target.value)}
        style={{
          width: "100%",
          height: "120px",
          padding: "10px",
          marginBottom: "15px"
        }}
      />

      <button
        onClick={handleAnalyze}
        style={{
          padding: "10px 20px"
        }}
      >
        {loading ? "Analyzing..." : "Analyze Business"}
      </button>

      {report && (
        <div
          style={{
            marginTop: "30px",
            border: "1px solid #ccc",
            padding: "20px",
            borderRadius: "10px",
            whiteSpace: "pre-wrap"
          }}
        >
          <h2>Generated Report</h2>
          {report}
        </div>
      )}
    </div>
  );
}

export default App;