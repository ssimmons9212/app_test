(function() {
    d3.csv('static/data/Wine Pairings - Herb_Spice.csv')
        .then(data => {
            console.log(data)
            console.log(data.forEach(entry => entry.wine))            
            const trace1 = {
                x: data.map(entry => entry.wine),
                y: data.map(entry => entry.fresh_green),
                name: "Fresh Green",
                type: 'bar'
            }
            const trace2 = {
                x: data.map(entry => entry.wine),
                y: data.map(entry => entry.earthy_green),
                name: "Earthy Green",
                type: 'bar'
            }
            const trace3 = {
                x: data.map(entry => entry.wine),
                y: data.map(entry => entry.bitter_floral),
                name: "Bitter Floral",
                type: 'bar'
            }
            const trace4 = {
                x: data.map(entry => entry.wine),
                y: data.map(entry => entry.allium),
                name: "Allium",
                type: 'bar'
            }
            const trace5 = {
                x: data.map(entry => entry.wine),
                y: data.map(entry => entry.savory_brown),
                name: "Savory Brown",
                type: 'bar'
            }
            const trace6 = {
                x: data.map(entry => entry.wine),
                y: data.map(entry => entry.sharp_spicy),
                name: "Sharp",
                type: 'bar'
            }
            const trace7 = {
                x: data.map(entry => entry.wine),
                y: data.map(entry => entry.perfumedcitrus_spicy),
                name: "Citrus",
                type: 'bar'
            }
            const trace8 = {
                x: data.map(entry => entry.wine),
                y: data.map(entry => entry.smoky_spicy),
                name: "Smokey",
                type: 'bar'
            }
            const trace9 = {
                x: data.map(entry => entry.wine),
                y: data.map(entry => entry.umami_spicy),
                name: "Umami",
                type: 'bar'
            }
            const trace10 = {
                x: data.map(entry => entry.wine),
                y: data.map(entry => entry.baking_spice),
                name: "Baking",
                type: 'bar'
            }
            const trace11 = {
                x: data.map(entry => entry.wine),
                y: data.map(entry => entry.anise),
                name: "Anise",
                type: 'bar'
            }          
            const layout = {
                title: 'Pairing Ratings by Spice Groups(Grapes)',
                barmode: 'group',
                xaxis: {
                    title: 'Wine Grapes',
                  },
                  yaxis: {
                    title: 'Pairing Rating',
                  }
            }
            Plotly.newPlot('spices2', [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9, trace10, trace11], layout, {displayModeBar: false})
        })
        .catch(err => console.log(err))       
})()