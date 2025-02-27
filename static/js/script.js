<script>
    fetch('/get_bus_routes')
        .then(response => response.json())
        .then(data => {
            data.forEach(bus => {
                console.log(`Route: ${bus.route}, Bus: ${bus.bus_number}`);
                // Add dynamic markers if needed
            });
        })
        .catch(error => console.error('Error fetching bus routes:', error));
</script>
