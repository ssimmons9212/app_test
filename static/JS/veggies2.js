(function() {
    d3.csv('static/data/Wine Pairings - Veg.csv')
        .then(data => {
            console.log(data)
            console.log(data.forEach(entry => entry.wine))            
            const trace1 = {
                x: data.map(entry => entry.wine),
                y: data.map(entry => entry.green_veg),
                name: "Green",
                type: 'bar'
            }
            const trace2 = {
                x: data.map(entry => entry.wine),
                y: data.map(entry => entry.root_veg),
                name: "Root",
                type: 'bar'
            }
            const trace3 = {
                x: data.map(entry => entry.wine),
                y: data.map(entry => entry.allium),
                name: "Allium",
                type: 'bar'
            }
            const trace4 = {
                x: data.map(entry => entry.wine),
                y: data.map(entry => entry.nightshade),
                name: "Nightshade",
                type: 'bar'
            }
            const trace5 = {
                x: data.map(entry => entry.wine),
                y: data.map(entry => entry.bean),
                name: "Bean",
                type: 'bar'
            }
            const trace6 = {
                x: data.map(entry => entry.wine),
                y: data.map(entry => entry.fungi),
                name: "Fungi",
                type: 'bar'
            }          
            const layout = {
                title: 'Pairing Ratings by Vegetable Groups(Grapes)',
                barmode: 'group',
                xaxis: {
                    title: 'Wine Grapes',
                  },
                  yaxis: {
                    title: 'Pairing Rating',
                  }
            }
            Plotly.newPlot('veggies2', [trace1, trace2, trace3, trace4, trace5, trace6], layout ,{displayModeBar: false})
        })
        .catch(err => console.log(err))       
})()