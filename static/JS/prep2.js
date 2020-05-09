(function() {
    d3.csv('static/data/Wine Pairings - Cooking.csv')
        .then(data => {
            console.log(data)
            console.log(data.forEach(entry => entry.wine))            
            const trace1 = {
                x: data.map(entry => entry.wine),
                y: data.map(entry => entry.grilledbbq),
                name: "BBQ",
                type: 'bar'
            }
            const trace2 = {
                x: data.map(entry => entry.wine),
                y: data.map(entry => entry.sauteedfried),
                name: "Fried",
                type: 'bar'
            }
            const trace3 = {
                x: data.map(entry => entry.wine),
                y: data.map(entry => entry.roasted),
                name: "Roasted",
                type: 'bar'
            }
            const trace4 = {
                x: data.map(entry => entry.wine),
                y: data.map(entry => entry.smoked),
                name: "Smoked",
                type: 'bar'
            }
            const trace5 = {
                x: data.map(entry => entry.wine),
                y: data.map(entry => entry.poachedsteamed),
                name: "Poached",
                type: 'bar'
            }
            const trace6 = {
                x: data.map(entry => entry.wine),
                y: data.map(entry => entry.raw),
                name: "Raw",
                type: 'bar'
            }         
            const layout = {
                title: 'Pairing Ratings by Cooking Method(Grapes)',
                barmode: 'group',
                xaxis: {
                    title: 'Wine Grapes',
                  },
                  yaxis: {
                    title: 'Pairing Rating',
                  }
            }
            Plotly.newPlot('prep2', [trace1, trace2, trace3, trace4, trace5, trace6], layout, {displayModeBar: false})
        })
        .catch(err => console.log(err))       
})()