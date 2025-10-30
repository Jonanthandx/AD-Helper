import { useState } from "react";
import axios from "axios";
import { Upload, Loader2 } from "lucide-react";

// 👇 Use environment variable for backend API URL
const API_URL = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async () => {
    if (!file) return alert("Please upload an image first!");
    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);
      const res = await axios.post(`${API_URL}/predict`, formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      setResult(res.data);
    } catch (err) {
      console.error(err);
      alert("Error uploading image: " + (err.response?.data?.detail || err.message));
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-dotaDark text-dotaGold flex flex-col items-center justify-center font-dota">
      <h1 className="text-4xl font-extrabold mb-8 text-dotaGold tracking-wide drop-shadow-[0_0_10px_#C49A00]">
        DOTA 2 ABILITY DRAFT ADVISOR
      </h1>

      <div className="bg-dotaRed/40 border border-dotaGold rounded-2xl p-8 shadow-[0_0_15px_#C49A00] w-[420px] flex flex-col items-center">
        <input
          type="file"
          accept="image/*"
          onChange={(e) => setFile(e.target.files[0])}
          className="text-sm text-gray-300 mb-4 file:mr-4 file:py-2 file:px-4 
            file:rounded-full file:border-0 file:text-sm file:font-semibold
            file:bg-dotaGold file:text-dotaDark hover:file:bg-yellow-400"
        />

        <button
          onClick={handleUpload}
          disabled={loading}
          className="flex items-center justify-center gap-2 bg-dotaGold text-dotaDark px-6 py-2 rounded-full 
          hover:bg-yellow-400 transition-transform transform hover:scale-105 disabled:opacity-60"
        >
          {loading ? (
            <>
              <Loader2 className="animate-spin" /> Processing...
            </>
          ) : (
            <>
              <Upload /> Upload & Predict
            </>
          )}
        </button>

        {result && (
          <div className="mt-6 bg-black/50 border border-dotaGold rounded-xl p-4 w-full text-left">
            <h2 className="text-xl font-bold mb-2 text-dotaGold drop-shadow-[0_0_6px_#C49A00]">
              Recommended Combo:
            </h2>
            <pre className="text-sm text-gray-200 bg-black/30 p-2 rounded max-h-64 overflow-y-auto">
              {JSON.stringify(result, null, 2)}
            </pre>
          </div>
        )}
      </div>

      <footer className="mt-8 text-gray-400 text-sm">
        Made for Dota 2 Players • by Luong ⚔️
      </footer>
    </div>
  );
}

export default App;
