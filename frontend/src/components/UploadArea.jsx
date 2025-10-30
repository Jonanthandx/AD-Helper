export default function UploadArea({ onUpload }) {
const handleFile = async (e) => {
const file = e.target.files[0];
if (file) onUpload(file);
};
return (
<div className="mb-4">
<input type="file" onChange={handleFile} accept="image/*" />
</div>
);
}