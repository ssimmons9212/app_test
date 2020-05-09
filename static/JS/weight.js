(function() {
    d3.csv('static/data/weight.csv')
        .then(data => {
            console.log(data)
            console.log(data.forEach(entry => entry.weight))            
            const trace1 = {
                x: data.map(entry => entry.weight),
                y: data.map(entry => entry.bold_red),
                name: "Bold Red",
                mode: 'lines+markers'
            }
            const trace2 = {
                x: data.map(entry => entry.weight),
                y: data.map(entry => entry.medium_Red),
                name: "Medium Red",
                mode: 'lines+markers'
            }
            const trace3 = {
                x: data.map(entry => entry.weight),
                y: data.map(entry => entry.light_red),
                name: "Light Red",
                mode: 'lines+markers'
            }
            const trace4 = {
                x: data.map(entry => entry.weight),
                y: data.map(entry => entry.rose),
                name: "Rose",
                mode: 'lines+markers'
            }
            const trace5 = {
                x: data.map(entry => entry.weight),
                y: data.map(entry => entry.rich_white),
                name: "Rich White",
                mode: 'lines+markers'
            }
            const trace6 = {
                x: data.map(entry => entry.weight),
                y: data.map(entry => entry.light_white),
                name: "Light White",
                mode: 'lines+markers'
            }
            const trace7 = {
                x: data.map(entry => entry.weight),
                y: data.map(entry => entry.sparkling),
                name: "Sparkling",
                mode: 'lines+markers'
            }
            const trace8 = {
                x: data.map(entry => entry.weight),
                y: data.map(entry => entry.sweet_white),
                name: "Sweet White",
                mode: 'lines+markers'
            }
            const trace9 = {
                x: data.map(entry => entry.weight),
                y: data.map(entry => entry.dessert),
                name: "Dessert",
                mode: 'lines+markers'
            }           
            const layout = {
                title: 'Pairing Ratings by Food Weight',
                xaxis: {
                    title: 'Food Weight',
                  },
                  yaxis: {
                    title: 'Pairing Rating',
                  },
                  height: 750
            }
            Plotly.newPlot('weight', [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9], layout, {displayModeBar: false})
        })
        .catch(err => console.log(err))       
})()