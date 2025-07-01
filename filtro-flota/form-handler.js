document.getElementById("filterForm").addEventListener("submit", async function (e) {
  e.preventDefault();

  const desde = document.getElementById("cfrDesde").value;
  const hasta = document.getElementById("cfrHasta").value;
  const estados = Array.from(document.getElementById("estados").selectedOptions).map(o => o.value);

  const payload = {
    event_type: "trigger-cfr-filter",
    client_payload: {
      cfr_desde: desde,
      cfr_hasta: hasta,
      estados: estados
    }
  };

  const token = "REEMPLAZAR_CON_TOKEN"; // Usa GitHub Actions secret o backend proxy

  const res = await fetch("https://api.github.com/repos/tu-org/filtro-flota/dispatches", {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${token}`,
      "Accept": "application/vnd.github+json",
      "Content-Type": "application/json"
    },
    body: JSON.stringify(payload)
  });

  if (res.ok) {
    alert("✅ Acción activada con éxito. Revisa la pestaña Actions en GitHub.");
  } else {
    alert("❌ Error al activar el workflow. Revisa la consola del navegador.");
    console.error(await res.text());
  }
});