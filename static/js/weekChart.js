function criarGraficoSemanal(config) {
    let chart = null;
    let ultimoHash = '';

    function carregar() {
        fetch(config.endpoint)
            .then(r => r.json())
            .then(json => {
                const hash = JSON.stringify(json.data);

                if (hash !== ultimoHash) {
                    ultimoHash = hash;

                    if (!chart) {
                        const ctx = document.getElementById(config.canvasId)?.getContext('2d');
                        if (!ctx) return;

                        chart = new Chart(ctx, {
                            type: 'line',
                            data: {
                                labels: json.labels,
                                datasets: [{
                                    label: config.label,
                                    data: json.data,
                                    tension: 0.4,
                                    fill: true,
                                    borderWidth: 2
                                }]
                            },
                            options: {
                                responsive: true,
                                animation: false,
                                scales: {
                                    y: { beginAtZero: true }
                                }
                            }
                        });
                    } else {
                        chart.data.labels = json.labels;
                        chart.data.datasets[0].data = json.data;
                        chart.update();
                    }
                }
            });
    }

    carregar();
    setInterval(carregar, 30000);
}
