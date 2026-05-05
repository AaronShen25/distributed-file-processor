import { useState } from "react";

function App() {
  const [file, setFile] = useState(null);
  const [status, setStatus] = useState("");

  const handleUpload = async () => {
    if (!file) {
      setStatus("Please select a file");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      setStatus("Uploading...");

      const response = await fetch("http://127.0.0.1:5000/convert", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        setStatus("Conversion failed");
        return;
      }

      const blob = await response.blob();

      const url = window.URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = "converted.jpg";
      document.body.appendChild(a);
      a.click();
      a.remove();

      setStatus("Download complete");
    } catch (error) {
      setStatus("Error occurred");
    }
  };

  return (
    <div style={{ padding: "40px" }}>
      <h1>PNG to JPG Converter</h1>

      <input
        type="file"
        accept=".png"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <br /><br />

      <button onClick={handleUpload}>Convert</button>

      <p>{status}</p>
    </div>
  );
}

export default App;