export default function ComboList({ data }) {
return (
<div className="mt-6">
<h2 className="text-xl mb-2">Best Combos</h2>
{data.combos.map((c, i) => (
<div key={i} className="bg-gray-800 rounded p-2 mb-2">
<p>{c.skills.join(' + ')}</p>
<p className="text-sm text-gray-400">Score: {c.score}</p>
</div>
))}
</div>
);
}