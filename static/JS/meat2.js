(function() {
    d3.csv('static/data/Wine Pairings - Protein.csv')
        .then(data => {
            console.log(data)
            console.log(data.forEach(entry => entry.wine))            
            const trace1 = {
                x: data.map(entry => entry.wine),
                y: data.map(entry => entry.red_meat),
                name: "Red Meat",
                type: 'bar'
            }
            const trace2 = {
                x: data.map(entry => entry.wine),
                y: data.map(entry => entry.cured_meat),
                name: "Cured Meat",
                type: 'bar'
            }
            const trace3 = {
                x: data.map(entry => entry.wine),
                y: data.map(entry => entry.game),
                name: "Game",
                type: 'bar'
            }
            const trace4 = {
                x: data.map(entry => entry.wine),
                y: data.map(entry => entry.pork),
                name: "Pork",
                type: 'bar'
            }
            const trace5 = {
                x: data.map(entry => entry.wine),
                y: data.map(entry => entry.poultry),
                name: "Poultry",
                type: 'bar'
            }
            const trace6 = {
                x: data.map(entry => entry.wine),
                y: data.map(entry => entry.fish),
                name: "Fish",
                type: 'bar'
            }
            const trace7 = {
                x: data.map(entry => entry.wine),
                y: data.map(entry => entry.shellfish),
                name: "Shellfish",
                type: 'bar'
            }
            const trace8 = {
                x: data.map(entry => entry.wine),
                y: data.map(entry => entry.mollusk),
                name: "Mollusk",
                type: 'bar'
            }          
            const layout = {
                title: 'Pairing Ratings by Meat Groups(Grapes)',
                barmode: 'group',
                xaxis: {
                    title: 'Wine Grapes',
                  },
                  yaxis: {
                    title: 'Pairing Rating',
                  }
            }
            Plotly.newPlot('meat2', [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8], layout, {displayModeBar: false})
        })
        .catch(err => console.log(err))       
})()