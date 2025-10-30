import axios from "axios";

// Use environment variable first, fall back to localhost
const API_URL = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";

export async function predict(file) {
  const form = new FormData();
  form.append("file", file);

  try {
    const res = await axios.post(`${API_URL}/predict`, form, {
      headers: { "Content-Type": "multipart/form-data" },
    });
    return res.data;
  } catch (error) {
    console.error("❌ API error:", error);
    throw new Error(
      error.response?.data?.detail ||
        "Failed to connect to Ability Draft API"
    );
  }
}
